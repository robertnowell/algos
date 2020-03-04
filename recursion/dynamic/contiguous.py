def subsequenceSum(a, sum, start, end, res):
	if start > end:
		print sum, res
		return sum
	if start == end:
		print sum, res
		return max(sum + a[start], sum)
	news = start+1
	newe = end-1
	sval = a[start]
	endval = a[end]

	return max(subsequenceSum(a, sum+sval, news, newe, res + [sval]), max(subsequenceSum(a, sum+endval, news, newe, res+[endval]), subsequenceSum(a, sum+sval+endval, news, newe, res+ [sval, endval])))

a = [1, -8, 3, -2, 4, -10]

# print(subsequenceSum(a, 0, 0, len(a)-1, []))

def contig(a):
	start = 0
	end = len(a)
	bestStart = start
	bestEnd = end
	m = sumBetween(a, start, end)
	for i in range(len(a)):
		for j in range(i, len(a)):
			newM = sumBetween(a, i, j)
			if newM > m:
				bestStart = i
				bestEnd = j
				m = newM
	print(bestStart, bestEnd)
	return m


def sumBetween(a, start, end):
	s = 0
	for i in range(start, end):
		s += a[i]
	return s

a = [1, -8, 3, -2, 4, -10]

print(contig(a))
