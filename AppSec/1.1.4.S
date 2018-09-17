.global your_asm_fn
.section .text


your_asm_fn:


pushl %ebp

movl %esp,%ebp
pushl $0x0
pushl $0x646f6f66
pushl $0x6c6f6f63

movl %esp, %eax
pushl $0xc105ed
movl %esp,%ebx
pushl %eax
pushl %ebx

pushl $0xacce55ed
call practice


leave
ret
