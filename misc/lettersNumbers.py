"""
[101100111100001]
[-1,1,-1,1,1,1,1,-1,-1,-1]

"""

def getDiffs(a):
	sum = 0
	res = []
	for i in range(len(a)):
		sum += a[i]
		res.append(sum)
	return res

def longestSubarrayWithLettersAndNumbers(a):
	diffs = getDiffs(a)
	print (diffs)
	diffLen = 0
	sumOfDiff = 0
	maxStart = 0
	maxEnd = 0
	if (diffs[-1] == 0):
		maxStart = 0
		maxEnd = len(a)-1
		diffLen = len(a)
	ma = {}
	s = 0
	for i in range(len(a)):
		s += a[i]
		print (s, i, a[i])
		if s in ma:
			if i-ma[s] > diffLen:
				maxDiff = s
				maxStart = ma[s]
				maxEnd = i
				diffLen = maxEnd - maxStart
		else:
			ma[s] = i+1
	print(diffLen, maxStart, maxEnd)

if __name__ == '__main__':
	test1 = [1, 1,-1,1,1,-1, 1,1,-1, -1,-1,-1]
	test2 = [-1, 1]
	longestSubarrayWithLettersAndNumbers(test1)
