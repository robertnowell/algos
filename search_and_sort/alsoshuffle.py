import random
def shuffle(arr):
	i = 0
	while i < len(arr):
		index = random.randint(0, i)
		swap = arr[index]
		arr[index] = arr[i]
		arr[i] = swap
		i+=1
	return arr


def recShuffle(arr, i):
	if i == 0:
		return arr
	rand = random.randint(0, i)
	swap = arr[rand]
	arr[rand] = arr[i]
	arr[i] = swap
	return recShuffle(arr, i-1)

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
		addTomap(recShuffle(arr, len(arr)-1))
	# print(ma)
	for k, v in ma.items():
		# print (k, v)
		for kk, vv in v.items():
			if vv > rounds/52 *2 or vv < rounds/52/2:
				print (k, kk, vv)
