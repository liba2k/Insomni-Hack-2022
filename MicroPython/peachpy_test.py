import sys
sys.path.append('Lib')
from Uefi import uefi
from peachpy.x86_64 import *

def main():
  shellcode = uefi.mem(1000)
  shellcode.TYPE = 'A'
  shellcode_ptr = uefi.mem('FN()')
  shellcode_ptr.VALUE = shellcode.ADDR

  shellcode.VALUE = bytes(MOV(ebx, 0xDEADBEEF).encode() + \
      MOV(eax, ebx).encode() + RET().encode())
  val = shellcode_ptr()
  print('Value: 0x{:08X}'.format(val))
  
if __name__ == "__main__":
  main()
