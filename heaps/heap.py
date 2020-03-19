from collections import deque 

heap = [None, 1, 2, 4, 5, 3, 6]
def insert(n):
	heap.append(n)
	i = len(heap)-1
	parent = i/2
	while(heap[parent] > heap[i]):
		tmp = heap[i]
		heap[i] = heap[parent]
		heap[parent] = tmp
		i = parent
		parent /= 2

def getLeft(i):
	return i*2 if i*2 < len(heap) else -1

def getRight(i):
	return i*2+1 if i*2+1 < len(heap) else -1

def minIndex(l, r):
	return l if heap[l] < heap[r] else r

def delete():
	toPop = heap[1]
	heap[1] = heap[-1]
	del heap[-1]
	cur = 1
	while (1):
		left = getLeft(cur)
		right = getRight(cur)
		if (left == -1):
			break;
		# print(left, right, heap[left], min(heap[left], heap[right]))
		lower = left if right == -1 else minIndex(left, right)
		if heap[lower] < heap[cur]:
			tmp = heap[cur]
			heap[cur] = heap[lower]
			heap[lower] = tmp
			cur = lower
		else:
			break

	return toPop

def p():
	if len(heap) < 2:
		print('empty')
		return
	q = deque()
	q.append(1)
	n = 1
	s = ""
	while len(q) > 0:
		cur = q.popleft()
		n-=1
		s += str(heap[cur]) + ", "
		left = cur*2
		if left < len(heap):
			q.append(left)
		right = cur*2+1
		if right < len(heap):
			q.append(right)
		if n == 0:
			n = len(q)
			print(s)
			s = ""


if __name__ == '__main__':
	# p()
	insert(-1)
	# p()
	insert(0)
	# p()
	insert(3)
	arr = []
	p()
	print(heap)
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	arr.append(delete())
	p()
	# arr.append(delete())
	print (arr)
