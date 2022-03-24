## @file
# Definitions of UEFI public services.
#
# Copyright (c) 2018, Intel Corporation. All rights reserved.<BR>
# This program and the accompanying materials
# are licensed and made available under the terms and conditions of the BSD License
# which accompanies this distribution.  The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#

from _uefi import *
from ucollections import OrderedDict

# INT8:           'b'
# UINT8:          'B'
# INT16:          'h'
# UINT16:         'H'
# INT32:          'l'
# UINT32:         'L'
# INT64:          'q'
# UINT64:         'Q'
# int:            'i'
# unsigned int:   'I'
# INTN:           'n'
# UINTN:          'N'
# EFI_GUID:       'G' (16B)
# VOID*:          'P'
# CHAR8[]:        'a'
# CHAR16[]:       'u'
# function*:      'F'
# EFI_STATUS:     'E'
# EFI_HANDLE:     'T'
# struct:         'O'

EFI_PCI_IO_PROTOCOL_ACCESS = OrderedDict([
    ("Read",  'FE(PO#EFI_PCI_IO_PROTOCOL,n,B,Q,N,P)'),
    ("Write", 'FE(PO#EFI_PCI_IO_PROTOCOL,n,B,Q,N,P)')
])

EFI_PCI_IO_PROTOCOL_CONFIG_ACCESS = OrderedDict([
    ("Read",  'FE(PO#EFI_PCI_IO_PROTOCOL,n,L,N,P)'),
    ("Write", 'FE(PO#EFI_PCI_IO_PROTOCOL,n,L,N,P)')
])

EFI_PCI_IO_PROTOCOL = OrderedDict([
    ("PollMem",         'FE(PO#EFI_PCI_IO_PROTOCOL,n,B,Q,Q,Q,Q,PQ)'),
    ("PollIo",          'FE(PO#EFI_PCI_IO_PROTOCOL,n,B,Q,Q,Q,Q,PQ)'),
    ("Mem",             'O#EFI_PCI_IO_PROTOCOL_ACCESS'),
    ("Io",              'O#EFI_PCI_IO_PROTOCOL_ACCESS'),
    ("Pci",             'O#EFI_PCI_IO_PROTOCOL_CONFIG_ACCESS'),
    ("CopyMem",         'FE(PO#EFI_PCI_IO_PROTOCOL,n,B,Q,B,Q,N)'),
    ("Map",             'FE(PO#EFI_PCI_IO_PROTOCOL,n,P,PN,PQ,PP)'),
    ("Unmap",           'FE(PO#EFI_PCI_IO_PROTOCOL,P)'),
    ("AllocateBuffer",  'FE(PO#EFI_PCI_IO_PROTOCOL,n,n,N,PP,Q)'),
    ("FreeBuffer",      'FE(PO#EFI_PCI_IO_PROTOCOL,N,P)'),
    ("Flush",           'FE(PO#EFI_PCI_IO_PROTOCOL)'),
    ("GetLocation",     'FE(PO#EFI_PCI_IO_PROTOCOL,PN,PN,PN,PN)'),
    ("Attributes",      'FE(PO#EFI_PCI_IO_PROTOCOL,n,Q,PQ)'),
    ("GetBarAttributes",'FE(PO#EFI_PCI_IO_PROTOCOL,B,PQ,PP)'),
    ("SetBarAttributes",'FE(PO#EFI_PCI_IO_PROTOCOL,Q,B,PQ,PQ)'),
    ("RomSize",         'Q'),
    ("RomImage",        'P'),
])

EFI_TABLE_HEADER = OrderedDict([
    ("Signature",   "Q"),
    ("Revision",    "L"),
    ("HeaderSize",  "L"),
    ("CRC32",       "L"),
    ("Reserved",    "L"),
])

EFI_DEVICE_PATH_PROTOCOL = OrderedDict([
    ("Type",    "B"),
    ("SubType", "B"),
    ("Length",  "2B"),
])

PCI_DEVICE_PATH = OrderedDict([
    ("Header",      'O#EFI_DEVICE_PATH_PROTOCOL'),
    ("Function",    'B'),
    ("Device",      'B'),
])

PCCARD_DEVICE_PATH = OrderedDict([
    ("Header",          'O#EFI_DEVICE_PATH_PROTOCOL'),
    ("FunctionNumber",  'B')
])

MEMMAP_DEVICE_PATH = OrderedDict([
    ("Header",          'O#EFI_DEVICE_PATH_PROTOCOL'),
    ("MemoryType",      'L'),
    ("StartingAddress", 'Q'),
    ("EndingAddress",   'Q'),
])

EFI_OPEN_PROTOCOL_INFORMATION_ENTRY = OrderedDict([
    ("AgentHandle",         "T"),
    ("ControllerHandle",    "T"),
    ("Attributes",          "L"),
    ("OpenCount",           "L"),
])

EFI_FILE_IO_TOKEN = OrderedDict([
    ("Event",       "P"),
    ("Status",      "E"),
    ("BufferSize",  "N"),
    ("Buffer",      "P")
])

EFI_FILE_PROTOCOL = OrderedDict([
    ("Revision",    "Q"),
    ("Open",        "FE(PO#EFI_FILE_PROTOCOL,PPO#EFI_FILE_PROTOCOL,u,Q,Q)"),
    ("Close",       "FE(PO#EFI_FILE_PROTOCOL)"),
    ("Delete",      "FE(PO#EFI_FILE_PROTOCOL)"),
    ("Read",        "FE(PO#EFI_FILE_PROTOCOL,PN,P)"),
    ("Write",       "FE(PO#EFI_FILE_PROTOCOL,PN,P)"),
    ("GetPosition", "FE(PO#EFI_FILE_PROTOCOL,PQ)"),
    ("SetPosition", "FE(PO#EFI_FILE_PROTOCOL,Q)"),
    ("GetInfo",     "FE(PO#EFI_FILE_PROTOCOL,PG,PN,P)"),
    ("SetInfo",     "FE(PO#EFI_FILE_PROTOCOL,PG,N,P)"),
    ("Flush",       "FE(PO#EFI_FILE_PROTOCOL)"),
    ("OpenEx",      "FE(PO#EFI_FILE_PROTOCOL,PPO#EFI_FILE_PROTOCOL,u,Q,Q,PO#EFI_FILE_IO_TOKEN)"),
    ("ReadEx",      "FE(PO#EFI_FILE_PROTOCOL,PO#EFI_FILE_IO_TOKEN)"),
    ("WriteEx",     "FE(PO#EFI_FILE_PROTOCOL,PO#EFI_FILE_IO_TOKEN)"),
    ("FlushEx",     "FE(PO#EFI_FILE_PROTOCOL,PO#EFI_FILE_IO_TOKEN)")
])

EFI_SIMPLE_FILE_SYSTEM_PROTOCOL = OrderedDict([
    ("Revision",    "Q"),
    ("OpenVolume",  "FE(PO#EFI_SIMPLE_FILE_SYSTEM_PROTOCOL,PPO#EFI_FILE_PROTOCOL)")
])

EFI_TIME = OrderedDict([
    ("Year",        'H'),
    ("Month",       'B'),
    ("Day",         'B'),
    ("Hour",        'B'),
    ("Minute",      'B'),
    ("Second",      'B'),
    ("Pad1",        'B'),
    ("Nanosecond",  'L'),
    ("TimeZone",    'h'),
    ("Daylight",    'B'),
    ("Pad2",        'B'),
])

EFI_TIME_CAPABILITIES = OrderedDict([
  ("Resolution",    'L'),
  ("Accuracy",      'L'),
  ("SetsToZero",    'B'),
])

EFI_MEMORY_DESCRIPTOR = OrderedDict([
  ("Type",          'L'),
  ("PhysicalStart", 'Q'),
  ("VirtualStart",  'Q'),
  ("NumberOfPages", 'Q'),
  ("Attribute",     'Q'),
])

EFI_CAPSULE_HEADER = OrderedDict([
    ("CapsuleGuid",         'G'),
    ("HeaderSize",          'L'),
    ("Flags",               'L'),
    ("CapsuleImageSize",    'L'),
])

EFI_INPUT_KEY = OrderedDict([
    ("ScanCode",    'H'),
    ("UnicodeChar", 'h'),
])

EFI_SIMPLE_TEXT_INPUT_PROTOCOL = OrderedDict([
    ("Reset",           'FE(PO#EFI_SIMPLE_TEXT_INPUT_PROTOCOL,B)'),
    ("ReadKeyStroke",   'FE(PO#EFI_SIMPLE_TEXT_INPUT_PROTOCOL,PO#EFI_INPUT_KEY)'),
    ("WaitForKey",      'P'),
])

EFI_SIMPLE_TEXT_OUTPUT_MODE = OrderedDict([
    ("MaxMode",         'l'),
    ("Mode",            'l'),
    ("Attribute",       'l'),
    ("CursorColumn",    'l'),
    ("CursorRow",       'l'),
    ("CursorVisible",   'B'),
])

EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL = OrderedDict([
    ("Reset",               'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,B)'),
    ("OutputString",        'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,u)'),
    ("TestString",          'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,u)'),
    ("QueryMode",           'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,N,PN,PN)'),
    ("SetMode",             'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,N)'),
    ("SetAttribute",        'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,N)'),
    ("ClearScreen",         'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL)'),
    ("SetCursorPosition",   'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,N,N)'),
    ("EnableCursor",        'FE(PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL,B)'),
    ("Mode",                'PO#EFI_SIMPLE_TEXT_OUTPUT_MODE'),
])

EFI_CONFIGURATION_TABLE = OrderedDict([
    ("VendorGuid",  'G'),
    ("VendorTable", 'P'),
])

EFI_GCD_MEMORY_SPACE_DESCRIPTOR = OrderedDict([
    ("BaseAddress",     'Q'),
    ("Length",          'Q'),
    ("Capabilities",    'Q'),
    ("Attributes",      'Q'),
    ("GcdMemoryType",   'n'),
    ("ImageHandle",     'T'),
    ("DeviceHandle",    'T'),
])

EFI_GCD_IO_SPACE_DESCRIPTOR = OrderedDict([
    ("BaseAddress", 'Q'),
    ("Length",      'Q'),
    ("GcdIoType",   'n'),
    ("ImageHandle", 'T'),
    ("DeviceHandle",'T'),
])

EFI_BOOT_SERVICES = OrderedDict([
    ("Hdr",             "O#EFI_TABLE_HEADER"),

    # Task Priority Services
    ("RaiseTPL",        "FN(N)"),
    ("RestoreTPL",      "F(N)"),

    # Memory Services
    ("AllocatePages",   "FE(n,n,N,PQ)"),
    ("FreePages",       "FE(Q,N)"),
    ("GetMemoryMap",    "FE(PN,PO#EFI_MEMORY_DESCRIPTOR,PN,PN,PI)"),
    ("AllocatePool",    "FE(n,N,PP)"),
    ("FreePool",        "FE(P)"),

    # Event & Timer Services
    ("CreateEvent",     "FE(L,N,P,F,PP)"),
    ("SetTimer",        "FE(P,n,Q)"),
    ("WaitForEvent",    "FE(N,PP,PN)"),
    ("SignalEvent",     "FE(P)"),
    ("CloseEvent",      "FE(P)"),
    ("CheckEvent",      "FE(P)"),

    # Protocol Handler Services
    ("InstallProtocolInterface",    "FE(PT,PG,n,P)"),
    ("ReinstallProtocolInterface",  "FE(T,PG,P,P)"),
    ("UninstallProtocolInterface",  "FE(T,PG,P)"),
    ("HandleProtocol",              "FE(T,PG,PP)"),
    ("Reserved",                    "P"),
    ("RegisterProtocolNotify",      "FE(PG,P,PP)"),
    ("LocateHandle",                "FE(n,PG,P,PN,PT)"),
    ("LocateDevicePath",            "FE(PG,PPO#EFI_DEVICE_PATH_PROTOCOL,PT)"),
    ("InstallConfigurationTable",   "FE(PG,P)"),

    # Image Services
    ("LoadImage",           "FE(B,T,PO#EFI_DEVICE_PATH_PROTOCOL,P,N,PT)"),
    ("StartImage",          "FE(T,PN,PU)"),
    ("Exit",                "FE(T,E,N,u)"),
    ("UnloadImage",         "FE(T)"),
    ("ExitBootServices",    "FE(T,N)"),

    # Miscellaneous Services
    ("GetNextMonotonicCount",   "FE(PQ)"),
    ("Stall",                   "FE(N)"),
    ("SetWatchdogTimer",        "FE(N,Q,N,u)"),

    # DriverSupport Services
    ("ConnectController",       "FE(T,PT,PO#EFI_DEVICE_PATH_PROTOCOL,B)"),
    ("DisconnectController",    "FE(T,T,T)"),

    # Open and Close Protocol Services
    ("OpenProtocol",            "FE(T,PG,PP,T,T,L)"),
    ("CloseProtocol",           "FE(T,PG,T,T)"),
    ("OpenProtocolInformation", "FE(T,PG,PPO#EFI_OPEN_PROTOCOL_INFORMATION_ENTRY,PN)"),

    # Library Services
    ("ProtocolsPerHandle",                  "FE(T,PPPG,PN)"),
    ("LocateHandleBuffer",                  "FE(n,PG,P,PN,PPT)"),
    ("LocateProtocol",                      "FE(PG,P,PP)"),
    ("InstallMultipleProtocolInterfaces",   "FE(PT,V)"),
    ("UninstallMultipleProtocolInterfaces", "FE(PT,V)"),

    # 32-bit CRC Services
    ("CalculateCrc32", "FE(P,N,PI)"),

    # Miscellaneous Services
    ("CopyMem",         "F(P,P,N)"),
    ("SetMem",          "F(P,N,B)"),
    ("CreateEventEx",   "FE(L,N,F,P,PG,PP)"),
])

EFI_RUNTIME_SERVICES = OrderedDict([
    ("Hdr", 'O#EFI_TABLE_HEADER'),

    #
    # Time Services
    #
    ("GetTime",         'FE(PO#EFI_TIME,PO#EFI_TIME_CAPABILITIES)'),
    ("SetTime",         'FE(PO#EFI_TIME)'),
    ("GetWakeupTime",   'FE(PB,PB,PO#EFI_TIME)'),
    ("SetWakeupTime",   'FE(B,PO#EFI_TIME)'),

    #
    # Virtual Memory Services
    #
    ("SetVirtualAddressMap",    'FE(N,N,L,PO#EFI_MEMORY_DESCRIPTOR)'),
    ("ConvertPointer",          'FE(N,PP)'),

    #
    # Variable Services
    #
    ("GetVariable",         'FE(u,PG,PI,PN,P)'),
    ("GetNextVariableName", 'FE(PN,u,PG)'),
    ("SetVariable",         'FE(u,PG,L,N,P)'),

    #
    # Miscellaneous Services
    #
    ("GetNextHighMonotonicCount",   'FE(PI)'),
    ("ResetSystem",                 'FE(n,E,N,P)'),

    #
    # UEFI 2.0 Capsule Services
    #
    ("UpdateCapsule",               'FE(PO#EFI_CAPSULE_HEADER,N,Q)'),
    ("QueryCapsuleCapabilities",    'FE(PO#EFI_CAPSULE_HEADER,N,PQ,Pn)'),

    #
    # Miscellaneous UEFI 2.0 Service
    #
    ("QueryVariableInfo", 'FE(L,PQ,PQ,PQ)'),
])

EFI_DXE_SERVICES = OrderedDict([
    ("Hdr", 'O#EFI_TABLE_HEADER'),

    #
    # Global Coherency Domain Services
    #
    ("AddMemorySpace",              'FE(n,Q,Q,Q)'),
    ("AllocateMemorySpace",         'FE(n,n,N,Q,PQ,T,T)'),
    ("FreeMemorySpace",             'FE(Q,Q)'),
    ("RemoveMemorySpace",           'FE(Q,Q)'),
    ("GetMemorySpaceDescriptor",    'FE(Q,PO#EFI_GCD_MEMORY_SPACE_DESCRIPTOR)'),
    ("SetMemorySpaceAttributes",    'FE(Q,Q,Q)'),
    ("GetMemorySpaceMap",           'FE(PN,PPO#EFI_GCD_MEMORY_SPACE_DESCRIPTOR)'),
    ("AddIoSpace",                  'FE(n,Q,Q)'),
    ("AllocateIoSpace",             'FE(n,n,N,Q,PQ,T,T)'),
    ("FreeIoSpace",                 'FE(Q,Q)'),
    ("RemoveIoSpace",               'FE(Q,Q)'),
    ("GetIoSpaceDescriptor",        'FE(Q,PO#EFI_GCD_IO_SPACE_DESCRIPTOR)'),
    ("GetIoSpaceMap",               'FE(PN,PPO#EFI_GCD_IO_SPACE_DESCRIPTOR)'),

    #
    # Dispatcher Services
    #
    ("Dispatch",    'FE()'),
    ("Schedule",    'FE(T,PG)'),
    ("Trust",       'FE(T,PG)'),

    #
    # Service to process a single firmware volume found in a capsule
    #
    ("ProcessFirmwareVolume", 'FE(P,N,T)'),

    #
    # Extensions to Global Coherency Domain Services
    #
    ("SetMemorySpaceCapabilities", 'FE(Q,Q,Q)'),
])

EFI_SYSTEM_TABLE = OrderedDict([
    ("Hdr",                     'O#EFI_TABLE_HEADER'),
    ("FirmwareVendor",          'u'),
    ("FirmwareRevision",        'L'),
    ("ConsoleInHandle",         'T'),
    ("ConIn",                   'PO#EFI_SIMPLE_TEXT_INPUT_PROTOCOL'),
    ("ConsoleOutHandle",        'T'),
    ("ConOut",                  'PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL'),
    ("StandardErrorHandle",     'T'),
    ("StdErr",                  'PO#EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL'),
    ("RuntimeServices",         'PO#EFI_RUNTIME_SERVICES'),
    ("BootServices",            'PO#EFI_BOOT_SERVICES'),
    ("NumberOfTableEntries",    'N'),
    ("ConfigurationTable",      'PO#EFI_CONFIGURATION_TABLE'),
])

gBS.CAST(EFI_BOOT_SERVICES)
gRT.CAST(EFI_RUNTIME_SERVICES)
gDS.CAST(EFI_DXE_SERVICES)
gST.CAST(EFI_SYSTEM_TABLE)

bs = gBS
rt = gRT
ds = gDS
st = gST

class VariableStorage(object):
    def __init__(self, VendorGuid=""):
        self._VendorGuid = str(VendorGuid).upper()
        self._LastVariable = None

    def __getitem__(self, Key):
        if not self._VendorGuid:
            Name = mem("%du" % (len(Key[0]) + 1))
            Name.VALUE = Key[0]
            Guid = guid(Key[1])
        else:
            Name = mem("%du" % (len(Key) + 1))
            Name.VALUE = Key
            Guid = guid(self._VendorGuid)

        Size = mem('N')
        Size.VALUE = 0

        try:
            rt.GetVariable(Name, Guid, null, Size, null)
        except efistatus as Excpt:
            if "BUFFER_TOO_SMALL" not in Excpt.args[0]:
                return None

        Data = mem("%dB" % Size.VALUE)
        rt.GetVariable(Name, Guid, null, Size, Data)
        Value = bytearray(Data)

        Name.FREE()
        Size.FREE()
        Data.FREE()
        Guid.FREE()

        return Value

    def __setitem__(self, Key, Value):
        if not self._VendorGuid:
            Name = mem("%du" % (len(Key[0]) + 1))
            Name.VALUE = Key[0]
            Guid = guid(Key[1])
        else:
            Name = mem("%du" % (len(Key) + 1))
            Name.VALUE = Key
            Guid = guid(self._VendorGuid)

        Data = mem("%dB" % len(Value))
        Data[:] = Value
        rt.SetVariable(Name, Guid, 0x7, len(Value), Data)

        Name.FREE()
        Guid.FREE()
        Data.FREE()

    def __delitem__(self, Key):
        if not self._VendorGuid:
            Name = mem("%du" % (len(Key[0]) + 1))
            Name.VALUE = Key[0]
            Guid = guid(Key[1])
        else:
            Name = mem("%du" % (len(Key) + 1))
            Name.VALUE = Key
            Guid = guid(self._VendorGuid)

        rt.SetVariable(Name, Guid, 0, 0, null)

        Name.FREE()
        Guid.FREE()

    def __contains__(self, Key):
        if not self._VendorGuid:
            Name = mem("%du" % (len(Key[0]) + 1))
            Name.VALUE = Key[0]
            Guid = guid(Key[1])
        else:
            Name = mem("%du" % (len(Key) + 1))
            Name.VALUE = Key
            Guid = guid(self._VendorGuid)

        Size = mem('N')
        Size.VALUE = 0
        Result = False

        try:
            rt.GetVariable(Name, Guid, null, Size, null)
        except efistatus as Excpt:
            if "BUFFER_TOO_SMALL" in Excpt.args[0]:
                Result = True 

        Name.FREE()
        Guid.FREE()
        Size.FREE()

        return Result

    def __iter__(self):
        NameSize = mem('N')
        Name = mem('128u')
        Guid = guid("00000000-0000-0000-0000-000000000000")

        Name.VALUE = "" # for the first time calling of GetNextVariableName()
        while True:
            try:
                # reset name buffer size
                NameSize.VALUE = len(Name)
                rt.GetNextVariableName(NameSize, Name, Guid)
                if not self._VendorGuid:
                    yield Name.VALUE, Guid.VALUE
                elif self._VendorGuid == Guid.VALUE:
                    yield Name.VALUE
            except efistatus as Excpt:
                break

        Name.FREE()
        NameSize.FREE()
        Guid.FREE()


if __name__ == '__main__':
    pass

