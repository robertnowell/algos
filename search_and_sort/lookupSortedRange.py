def lookup(a, target):
	return search(a, target, 0, len(a)-1)

def search(a, target, low, high):
	print(low, high)
	if low > high:
		if len(a) > low and a[low] > target:
			return a[low]
		else:
			return a[low + 1] if len(a) > low + 1 else a[0]
	mid = (low + high)/2

	if a[mid] == target:
		return a[mid + 1] if len(a) > mid + 1 else a[0]
	if a[mid] > target:
		return search(a, target, 0, mid-1)
	else:
		return search(a, target, mid+1, high)

if __name__ == '__main__':
	a = ['c', 'f', 'j', 'p', 'v']
	print(lookup(a, 'a')) # 	'a' => return 'c'
	print(lookup(a, 'c'))# 'c' => return 'f'
	print(lookup(a, 'k'))# 'k' => return 'p'
	print(lookup(a, 'z'))# 'z' => return 'c'
	a = ['c', 'f', 'k']
	print(lookup(a, 'f')) #'f' => 'k'
	print(lookup(a, 'c')) #'c' => 'f'
	print(lookup(a, 'd')) #'d' => 'f'
