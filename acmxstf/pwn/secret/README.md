# Secret

## Prerequisites
None

## What was the vulnerability?
The vulnerability was an improper use of the gets function. When no parameters are given to gets(), the user can input as many bytes as he wants, overflowing the buffer.
There are two fundamental parts to this challenge: 
Firstly, the first eight bytes of the input must be "12345678", so that the program runs the command "/bin/cat secret.txt".
Secondly, there is no secret.txt, so it won't do anything.

Since gets() doesn't have any restrictions, we can overflow the buffer to overwrite the command. There are 16 bytes from s1 to command (we can check that on a debugger or disassembler), so the payload must have the following structure:

`[12345678][8 bytes][command]` 

We weren't sure what the flag file name was, so we used the /bin/sh command, to spawn a shell.
