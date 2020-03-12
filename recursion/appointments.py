def recurse(l, i, countSoFar, soFar):
	if i >= len(l):
		return (countSoFar, soFar)
	chooseCur, l1 = recurse(l, i+2, countSoFar+l[i], soFar + [l[i]])
	i+=1
	if i >= len(l):
		return (chooseCur, l1)
	chooseNext, l2 = recurse(l, i+2, countSoFar+l[i], soFar + [l[i]])
	return (chooseCur, l1) if chooseCur >= chooseNext else (chooseNext, l2)

if __name__ == '__main__':
	val, l = recurse([30, 15, 60, 75, 45, 15, 15, 45], 0, 0, [])
	print(val, l)
