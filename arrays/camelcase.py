#!/bin/python

import sys


s = raw_input().strip()
count = 1 if s else 0
for char in s:
    if char.isupper():
        count += 1
print count