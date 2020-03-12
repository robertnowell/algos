def vol(a, i, volSoFar, left, negative):
	print("i: ", i, ", vol ", volSoFar, ", left ", left, ", negative ", negative)
	if i == len(a):
		return volSoFar
	if a[i] == 0:
		return vol(a, i+1, volSoFar, left, negative)
	else:
		if left == -1:
			left = i
			return vol(a, i+1, volSoFar, left, negative)
		else:
			# branch

			nochoose = volSoFar
			if a[i] < a[left]:
				print("Branching, ", i, volSoFar, left, negative)
				negative += a[i]
				nochoose = vol(a, i+1, volSoFar, left, negative)
				negative -= a[i]
			width = i-left-1
			height = min(a[i], a[left])
			volSoFar += width * height - negative
			print (width, height, negative, volSoFar)
			choose = vol(a, i+1, volSoFar, i, 0)
			print("Branched, ", i, volSoFar, left, negative)
			print("choose ", choose, ", nochoose ", nochoose)
			return max(nochoose, choose)
if __name__ == '__main__':
	a = [0,0,4,0,0,6,0,0,3,0,1, 0, 5,0,1,0,0,0]
	print (vol(a, 0, 0, -1, 0))