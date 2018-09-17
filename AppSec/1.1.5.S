.global _main

.section .text
shell:
        .string "//bin/sh"

_main:
    
    pushl %ebp

    movl %esp,%ebp
    
    movl $shell,%ebx

    movl $0,%ecx
    
    movl $0,%edx 

    movl $11,%eax

    int $0x80

    leave 

    ret 

    
    
    
   
