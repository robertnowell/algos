import random
def randM(s):
	rand = list(s[0:m])
	for i in range(m+1, len(s)):
		idx = random.randint(0, i)
		if idx < m:
			rand[idx] = s[i]
	return rand

