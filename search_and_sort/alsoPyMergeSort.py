import random
def merge(arr, low, mid, high):
	aux = arr[low:high+1]
	offset = low
	left = 0
	right = mid+1-low
	i = low
	while left <= mid-low and right <= high-low:
		if aux[left] < aux[right]:
			arr[i] = aux[left]
			left+=1
		else:
			arr[i] = aux[right]
			right+=1
		i+=1
	while left <= mid-low:
		arr[i] = aux[left]
		left+=1
		i+=1

def helper(arr, low, high):
	if low == high:
		return low, high
	mid = (low+high)/2
	helper(arr, low, mid)
	helper(arr, mid+1, high)
	merge(arr, low, mid, high)

def mergeSort(arr):
	helper(arr, 0, len(arr)-1)

if __name__ == '__main__':
	arr = []

	for i in range(100000):
		arr.append(random.randint(0, 1000000))
	# print arr
	mergeSort(arr)
	print (arr == sorted(arr))
	print(arr)
