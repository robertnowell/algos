import random
m = 10
def randM(arr, i):
	if i + 1 == m:
		return arr[:m]
	subset = randM(arr, i-1)
	test = random.randint(0,len(arr)-1)
	if test < m:
		subset[test] = arr[i]
	return subset

if __name__ == '__main__':
	arr = [i for i in range(20)]
	_map = {}
	for i in range(100000):
		subs = randM(arr, len(arr)-1)
		for val in subs:
			_map[val] = _map.get(val, 0) + 1
	print(_map)
