import sys
sys.path.append('Lib')
from Uefi import uefi
from ucollections import OrderedDict

EFI_MMRAM_DESCRIPTOR = OrderedDict((
  ("PhysicalStart",      'N'),
  ("CpuStart",           'N'),
  ("PhysicalSize",       'N'),
  ("RegionState",        'N'),
))

EFI_SMM_ACCESS2_PROTOCOL = OrderedDict((
  ("Open",                      'FE(PO#EFI_SMM_ACCESS2_PROTOCOL)'),
  ("Close",                     'FE(PO#EFI_SMM_ACCESS2_PROTOCOL)'),
  ("Lock",                      'FE(PO#EFI_SMM_ACCESS2_PROTOCOL)'),
  ("GetCapabilities",           'FE(PO#EFI_SMM_ACCESS2_PROTOCOL,PN,PO#EFI_MMRAM_DESCRIPTOR)'),
))

def GetCapabilities():
  gEfiSmmAccess2ProtocolGuid = uefi.guid("c2702b74-800c-4131-8746-8fb5b89ce4ac")
  Infc = uefi.mem()    # empty object just used to hold the protocol pointer
  uefi.bs.LocateProtocol (gEfiSmmAccess2ProtocolGuid, uefi.null, Infc.REF().REF())
  Infc.CAST("O#EFI_SMM_ACCESS2_PROTOCOL")  # typecast it so we can access its fields

  MmramDescriptor = uefi.mem('O#EFI_MMRAM_DESCRIPTOR')
  EFI_MMRAM_DESCRIPTOR_SIZE = MmramDescriptor.SIZE
  size = uefi.mem('N')
  size.VALUE = EFI_MMRAM_DESCRIPTOR_SIZE*20
  MmramDescriptor = uefi.mem(size.VALUE)
  Infc.GetCapabilities(Infc.REF(), size.REF(), MmramDescriptor.REF())
  capabilities = []
  for i in range(divmod(size.VALUE, EFI_MMRAM_DESCRIPTOR_SIZE)[0]):
      entry = uefi.mem('O#EFI_MMRAM_DESCRIPTOR', MmramDescriptor.ADDR + i*EFI_MMRAM_DESCRIPTOR_SIZE)
      capabilities.append(entry)
  return capabilities

def main():
  for entry in GetCapabilities():
    print('PhysicalStart: ', hex(entry.PhysicalStart))
    print('CpuStart: ', hex(entry.CpuStart))
    print('PhysicalSize: ', hex(entry.PhysicalSize))
    print('ReagionState: ', hex(entry.RegionState))
    print('\n')

if __name__ == "__main__":
  main()
