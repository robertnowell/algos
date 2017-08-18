import sys

def super_reduced_string(s):
    if s == '':
        return 'Empty String'
    s = list(s)
    ignore = []
    res = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1] and i not in ignore and i + 1 not in ignore:
            ignore.extend([i, i+1])
    for i in range(len(s)):
        if i not in ignore:
            res += s[i]
    if ignore != []:
        return super_reduced_string(res)
    elif res == '':
        return 'Empty String'
    else:
        return res

s = raw_input().strip()
result = super_reduced_string(s)
print(result)