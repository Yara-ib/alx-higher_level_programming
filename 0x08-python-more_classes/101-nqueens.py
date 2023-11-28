#!/usr/bin/python3
""" Not finished obviously LOL .."""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

np = int(sys.argv[1])
if not isinstance(np, int):
    print("N must be a number")
    sys.exit(1)

if np < 4:
    print("N must be at least 4")
    sys.exit(1)
lis2t = []
for n in range(np):
    for m in range(np):
        if n != m:
            lis2t.append([n, m])
new = []
for item in lis2t:
    for i in item:
        if i =
print(lis2t)
