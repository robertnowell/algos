def shortest(l, s):
	start = 0
	s2 = set(s)
 	while l[start] not in s and start < len(l):
		start += 1
	s2.remove(l[start])
	end = start
	while not s2 == set() and end < len(l):
		end += 1
		if l[end] in s2:
			s2.remove(l[end])
	print (start, end)
	minRange = (start, end)
	minSize = end-start

	while start <= end and end < len(l):
		search = l[start]
		start += 1
		while l[start] not in s:
			start+=1
		if l[start] != search:
			while end < len(l) and l[end] != search:
				end += 1
		size = end-start
		if size < minSize:
			minSize = size
			minRange = (start, end)
			print(minSize, minRange)




if __name__ == '__main__':
	shortest([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8], set([1,5,9]))