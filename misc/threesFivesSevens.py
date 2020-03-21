from collections import deque
def threesFivesSevens(k):
	threes = deque()
	fives = deque()
	sevens = deque()
	threes.append(1)
	for _ in range(k):
		v3 = threes[0] if len(threes) > 0 else 1000000
		v5 = fives[0] if len(fives) > 0 else 1000000
		v7 = sevens[0] if len(sevens) > 0 else 1000000
		val= min(v3, min(v5, v7))
		if val == v3:
			threes.append(val*3)
			threes.popleft()
			fives.append(val*5)
		if val == v5:
			fives.append(val*5)
			fives.popleft()
		if val == v7:
			sevens.popleft()
		sevens.append(val*7)
	return val

if __name__ == '__main__':
	print(threesFivesSevens(500000))
