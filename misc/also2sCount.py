def twosCountAtDigit(n, d):
	powTen = 10**d
	nextPow = powTen*10
	right = n % powTen
	roundDown = n - (n % nextPow)
	roundUp = roundDown + nextPow
	digit = (n / powTen) % 10
	if digit < 2:
		return roundDown/10
	if digit == 2:
		return roundDown/10 + right + 1
	else:
		return roundUp/10

def twosCount(n):
	res =0
	for i in range(len(str(n))):
		r = twosCountAtDigit(n, i)
		res+=r
	return res

if __name__ == '__main__':
	print(twosCount(10))
	print(twosCount(121))
	print(twosCount(1200))
	print(twosCount(125))
