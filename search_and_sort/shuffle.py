import random
def shuffle(arr):
	# i = 0
	# while i < len(arr):
	# 	n = random.randint(0, i)
	# 	tmp = arr[i]
	# 	arr[i] = arr[n]
	# 	arr[n] = tmp
	# 	i+=1
	# return arr
	return _shuffle(arr, len(arr)-1)

def _shuffle(arr, i):
	if i == 0:
		return arr
	n = random.randint(0, i)
	_shuffle(arr, i-1)
	tmp = arr[n]
	arr[n] = arr[i]
	arr[i] = tmp
	return arr

















ma = {}

def addTomap(arr):
	for i in range(len(arr)):
		ma[i] = ma.get(i, {})
		ma[i][arr[i]] = ma[i].get(arr[i], 0) + 1
if __name__ == '__main__':
	arr = [ i for i in range(52) ]
	rounds = 10000
	for i in range(rounds):
		if (i % 100000 == 0):
			print(i)
		addTomap(shuffle(arr))
	# print(ma)
	for k, v in ma.items():
		# print (k, v)
		for kk, vv in v.items():
			if vv > rounds/52 *2 or vv < rounds/52/2:
				print (k, kk, vv)
 