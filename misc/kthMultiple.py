from collections import deque

def kth(k):
	threes = deque()
	fives = deque()
	sevens = deque()
	threes.append(1)
	for i in range(0, k):
		v3 = threes[0] if len(threes) > 0 else 10000000
		v5 = fives[0] if len(fives) > 0 else 10000000
		v7 = sevens[0] if len(sevens) > 0 else 10000000
		val = min(v3, min(v5, v7))
		print threes
		print fives
		print sevens
		print(v3, v5, v7, val)
		if val == v3:
			threes.popleft()
			threes.append(val*3)
			fives.append(val*5)
		elif val == v5:
			fives.popleft()
			fives.append(val*5)
		elif val == v7:
			sevens.popleft()
		sevens.append(val*7)
	return val

if __name__ == '__main__':
	print(kth(5))
