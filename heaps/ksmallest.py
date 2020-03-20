from heap import MaxHeap

def smallestK(arr, k):
	h = MaxHeap(k)
	for n in arr:
		try:
			h.insert(n)
		except:
			m = h.peek()
			if n < m:
				h.delete()
				h.insert(n)
	print(h.getSorted())

if __name__ == '__main__':
	smallestK([5, 3, 6, 1, 2, 4], 3)