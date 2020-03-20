def twosCountatDigit(n, d):
	powTen = 10 ** d
	nextPowTen = 10 * powTen
	right = n % powTen
	roundDown = n - (n % nextPowTen)
	roundUp = roundDown + nextPowTen
	digit = n/powTen % 10
	print('n', n)
	print('d', d) 
	print('powTen', powTen) 
	print('nextPowTen', nextPowTen) 
	print('right', right) 
	print('roundDown', roundDown) 
	print('roundup', roundUp) 
	print('digit', digit)
	if digit<2:
		return roundDown/10
	elif digit == 2:
		return roundDown/10 + right+1
	else:
		return roundUp/10

def twosCount(n):
	s = 0
	for i in range(len(str(n))):
		res = twosCountatDigit(n, i)
		print('adding to sum: ', res)
		s+=res
	return s

if __name__ == '__main__':
	print(twosCount(212))