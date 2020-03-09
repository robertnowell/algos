def count2s(n):
	count = 0
	div = 10
	while n / div > 0:
		m = n / div
		for i in range(m):
			count += div/10
		div *= 10
	print (n, div, div/10, n%(div/10))
	for i in range(n % (div/10) +1):
		if i == 2:
			print(div/100 if div > 100 else 1, (div/100 if div > 10 else 1))
			count += (div/100 if div > 10 else 1) * (div/1000 if div > 100 else 1)
	print (count)
if __name__ == '__main__':
	count2s(102)
