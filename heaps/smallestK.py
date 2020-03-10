def smallestK(l, k):
	pqueue = MaxHeap(k)
	for n in l:
		if not pqueue.full():
			pqueue.add(n)
		else:
			if pqueue.max() > n:
				pqueue.pop()
				pqueue.add(n)
	return pqueue.toArray()
