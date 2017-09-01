#!/bin/python

import sys

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
res = ''
for char in s:
    if char.isalpha():
        _ascii = ord(char)
        new_val = ord(char) + (k % 26)
        if _ascii >= 97 and _ascii <= 122:
            if not chr(new_val).isalpha():
                test = chr(new_val - 26)
            else:
                test = chr(new_val)
        else:
            if new_val >= 91:
                test = chr(new_val - 26)
            else:
                test = chr(new_val)
        res += test
    else:
        res += char
print res
