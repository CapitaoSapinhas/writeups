#!/usr/bin/python3
key = b"XORAMAIS"

with open("input.bin", 'rb') as inp:
    data = inp.read()

xored = bytearray()
for i in range(len(data)):
    xored.append(data[i] ^ key[i % len(key)])

with open("flag.txt", 'wb') as out:
    out.write(xored)
