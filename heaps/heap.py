from collections import deque 

class Heap():
	def getRight(self, i):
		return i*2+1 if i*2+1 < len(self.heap) else -1

	def getLeft(self, i):
		return i*2 if i*2 < len(self.heap) else -1
	
	def setCap(n):
		self.cap = n

	def p(self):
		if len(self.heap) < 2:
			print('empty')
			return
		q = deque()
		q.append(1)
		n = 1
		s = ""
		while len(q) > 0:
			cur = q.popleft()
			n-=1
			s += str(self.heap[cur]) + ", "
			left = cur*2
			if left < len(self.heap):
				q.append(left)
			right = cur*2+1
			if right < len(self.heap):
				q.append(right)
			if n == 0:
				n = len(q)
				print(s)
				s = ""

	def getSorted(self):
		arr = []
		while (len(self.heap) > 1):
			arr.append(self.delete())
		for c in arr:
			self.insert(c)
		print(self.heap)
		print(arr)
		return arr

class MinHeap(Heap):
	def __init__(self, cap):
		self.heap = [None]
		self.cap = cap

	def insert(self, n):
		if len(self.heap) > self.cap:
			raise Exception('cannot insert, at capacity {}'.format(self.cap))
		self.heap.append(n)
		i = len(self.heap)-1
		parent = i/2
		while(self.heap[parent] > self.heap[i]):
			tmp = self.heap[i]
			self.heap[i] = self.heap[parent]
			self.heap[parent] = tmp
			i = parent
			parent /= 2

	def minIndex(self, l, r):
		return l if self.heap[l] < self.heap[r] else r

	def delete(self):
		toPop = self.heap[1]
		self.heap[1] = self.heap[-1]
		del self.heap[-1]
		cur = 1
		while (1):
			left = self.getLeft(cur)
			right = self.getRight(cur)
			if (left == -1):
				break;
			lower = left if right == -1 else self.minIndex(left, right)
			if self.heap[lower] < self.heap[cur]:
				tmp = self.heap[cur]
				self.heap[cur] = self.heap[lower]
				self.heap[lower] = tmp
				cur = lower
			else:
				break
		return toPop

class MaxHeap(Heap):
	def __init__(self, cap):
		self.heap = [None]
		self.cap = cap

	def peek(self):
		return self.heap[1] if len(self.heap) > 1 else None

	def insert(self, n):
		if len(self.heap) > self.cap:
			raise Exception('cannot insert, at capacity {}'.format(self.cap))
		self.heap.append(n)
		i = len(self.heap)-1
		parent = i/2
		while(self.heap[parent] is not None and self.heap[parent] < self.heap[i]):
			tmp = self.heap[i]
			self.heap[i] = self.heap[parent]
			self.heap[parent] = tmp
			i = parent
			parent /= 2

	def maxIndex(self, l, r):
		return l if self.heap[l] > self.heap[r] else r


	def delete(self):
		toPop = self.heap[1]
		self.heap[1] = self.heap[-1]
		del self.heap[-1]
		cur = 1
		while (1):
			left = self.getLeft(cur)
			right = self.getRight(cur)
			if (left == -1):
				break;
			# print(left, right, self.heap[left], min(self.heap[left], self.heap[right]))
			greater = left if right == -1 else self.maxIndex(left, right)
			if self.heap[greater] > self.heap[cur]:
				tmp = self.heap[cur]
				self.heap[cur] = self.heap[greater]
				self.heap[greater] = tmp
				cur = greater
			else:
				break

		return toPop


if __name__ == '__main__':
	h = MaxHeap(6)
	for c in [1, 2, 4, 5, 3, 6]:
		h.insert(c)
	h.p()
	h.insert(-1)
	# p()
	h.insert(0)
	# p()
	h.insert(3)
	arr = []
	h.p()
	print(h.getSorted())
	print(h.getSorted())

	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	arr.append(h.delete())
	h.p()
	# arr.append(delete())
	print (arr)