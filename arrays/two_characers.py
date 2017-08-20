import sys


s_len = int(raw_input().strip())
s = raw_input().strip()

collection = []
for char in s:
    if char not in collection:
        collection.append(char)

longest = 0
for char1 in collection:
    for char2 in collection:
        res = ''
        for char in s:
            if char == char1 or char == char2:
                res += char
        valid = 1
        for i in range(len(res)-1):
            if res[i] == res[i+1]:
                valid = 0
        if valid == 1 and len(res) > longest:
            longest = len(res)
print longest if longest > 1 else 0