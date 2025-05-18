# xoramais
This challenge is an introductory disk forensics challenge.

## Approach
In disk forensics, we need to use tools like Autopsy (GUI-based) or SleuthKit to restore information from the disk. For this challenge, we used SleuthKit.

The first command we always run is fsstat (file system stats) to get a sense of what's going on.
We concluded that the file system is FAT16, which turned out to be irrelevant for this challenge.

The second command we ran was fls, and we noticed two very interesting files: key.txt and secret.bin.

To extract these files, we used the icat command, which allows us to extract the contents of files by their inode.

Given the "xor" hint in the challenge name, we figured out that secret.bin ⊕ key.txt = flag.

Finally, we wrote a script to perform the XOR operation, and we got the flag.
