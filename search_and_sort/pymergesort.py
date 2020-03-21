import random

# def merge(arr1, arr2):
# 	arr = []
# 	i = 0
# 	j = 0
# 	while i < len(arr1) and j < len(arr2):
# 		if arr1[i] < arr2[j]:
# 			arr.append(arr1[i])
# 			i+=1
# 		else:
# 			arr.append(arr2[j])
# 			j+=1
# 	if i == len(arr1):
# 		while j < len(arr2):
# 			arr.append(arr2[j])
# 			j+=1
# 	elif j == len(arr2):
# 		while i < len(arr1):
# 			arr.append(arr1[i])
# 			i+=1
# 	return arr

# def helper(arr, low, high, res):
# 	print (low, high)
# 	if low==high:
# 		return [arr[low]]
# 	mid = (low+high)/2
# 	print (mid)
# 	return merge(helper(arr, low, mid, res), helper(arr, mid+1, high, res))

# def merge(arr, l1, h1, l2, h2):
# 	res = []
# 	i = l1
# 	j = l2
# 	while i <= h1 and j <= h2:
# 		if arr[i] < arr[j]:
# 			res.append(arr[i])
# 			i+=1
# 		else:
# 			res.append(arr[j])
# 			j+=1
# 	if i >= h1:
# 		while j <= h2:
# 			res.append(arr[j])
# 			j+=1
# 	elif j >= h2:
# 		while i <= h1:
# 			res.append(arr[i])
# 			i+=1
# 	p = 0
# 	for q in range(l1, h2+1):
# 		try:
# 			arr[q] = res[p]
# 			p+=1
# 		except:
# 			import pdb; pdb.set_trace()

def merge(arr, aux, low, mid, high):
	for i in range(low, high+1):
		aux[i] = arr[i]

	left = low
	right = mid+1
	i = low
	while left <= mid and right <= high:
		if aux[left] < aux[right]:
			arr[i] = aux[left]
			left+=1
		else:
			arr[i] = aux[right]
			right+=1
		i+=1
	while left <= mid:
		arr[i] = aux[left]
		left+=1
		i+=1





def merge(arr, low, mid, high):
	aux = []
	for i in range(low, high+1):
		aux.append(arr[i])

	offset = low
	left = low
	right = mid+1
	i = low
	while left <= mid and right <= high:
		if aux[left-offset] < aux[right-offset]:
			arr[i] = aux[left-offset]
			left+=1
		else:
			arr[i] = aux[right-offset]
			right+=1
		i+=1
	while left <= mid:
		arr[i] = aux[left-offset]
		left+=1
		i+=1

def helper(arr, low, high):
	if low >= high:
		return
	mid = (low+high)/2
	helper(arr, low, mid)
	helper(arr, mid+1, high)
	merge(arr, low, mid, high)

def mergeSort(arr):
	return helper(arr, 0, len(arr)-1)

if __name__ == '__main__':
	arr = []

	for i in range(1435000):
		arr.append(random.randint(0, 1540050))
	# print arr
	mergeSort(arr)
	print(arr)
