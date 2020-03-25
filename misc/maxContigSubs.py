def maxContig(a):
	sumSoFar = -1000000
	best = sumSoFar
	for n in a:
		if sumSoFar + n < 0 or sumSoFar < 0:
			sumSoFar = n
		else:
			sumSoFar += n
		best = sumSoFar if sumSoFar > best else best
	return best

if __name__ == '__main__':
	arr = [1,2,-4,1, 3,-2,3,-1]
	print(maxContig(arr))
