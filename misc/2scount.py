def count2sAtD(n, d):
	powerOfTen = 10**d
	nextPow = powerOfTen*10
	right = n % powerOfTen
	roundDown = n - n % nextPow
	roundUp = roundDown + nextPow
	digit = (n / powerOfTen) % 10
	print("")
	print("n", n)
	print("d", d)
	print("powerOfTen", powerOfTen)
	print("nextPow", nextPow)
	print("right", right)
	print("roundDown", roundDown)
	print("roundUp", roundUp)
	print("digit", digit)
	if (digit < 2):
		return roundDown /10
	if digit == 2:
		return roundDown/10 + right + 1
	else:
		return roundUp/10

def count2s(n):
	count = 0
	length = len(str(n))
	for i in range(length):
		res = count2sAtD(n, i)
		print("adding ", res)
		count += res
	return count

if __name__ == '__main__':
	# print(count2s(10))
	print(count2s(121))
	# print(count2s(1200))
	# print(count2s(125))
