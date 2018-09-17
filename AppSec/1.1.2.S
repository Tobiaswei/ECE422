.global your_asm_fn
.section .text


your_asm_fn:


pushl %ebp

movl %esp,%ebp
pushl $0xc001f00d
pushl $0xc105ed
pushl $0xacce55ed
call practice


leave
ret
