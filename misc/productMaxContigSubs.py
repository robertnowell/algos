
def productMaxContig(a):
	curMin = a[0]
	curMax = a[0]
	best = a[0]
	for n in a[1:]:
		if n < 0:
			tmp = curMax
			curMax = max(curMin * n, n)
			curMin = min(tmp * n, n)
		else:
			curMax = max(curMax * n, n)
			curMin = max(curMin * n, n)

		best = best if best > curMax else curMax
	return best

"""Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -3, 0, -2, -40}
Output:   80  // The subarray is {-2, -40}"""

if __name__ == '__main__':
	a = [6, -3, -10, 0, 2]
	print(productMaxContig(a))
	b = [-1, -3, -10, 0, 60]
	print(productMaxContig(b))
	c = [-2, -3, 0, -2, -40]
	print(productMaxContig(c))
