# xoramais
This challenge is an introductory disk forensics challenge.

## Approach
In disk forensics we need to use tools like autopsy (GUI based) or sleuthkit in order to restore the information in the disk. For this challenge we used the sleuthkit.

The first command we alway run is `fsstat` (file system stats) to get a sense of what's going on.
We concluded that the file system is FAT16, which was actually not important for this challenge.

The second command we ran was `fls` and noticed that there were two very interesting files "key.txt" and "secret.bin".

To extract these files we used the `ìcat` command that allows us to extract the contents of those files.

With the "xor" hint in the challenge name, we figured that secret.bin⊕key.txt = flag

Finally, we made a script that did that are we got the flag.
