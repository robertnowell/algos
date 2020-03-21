class MinDist():
	def __init__(self, arr):
		self.arr = arr
		self.mostRecentIndices = {}
		self.map = {}
		self.indices = {}
		self.generateIndices()
		self.findAllDistances()
		print self.map

	def generateIndices(self):
		for i in range(len(self.arr)):
			self.indices[self.arr[i]] = self.indices.get(self.arr[i], []) + [i]

	def mediumSpeedDist(self, w1, w2):
		w1Indices = self.indices.get(w1, None)
		w2Indices = self.indices.get(w2, None)
		if w1Indices is None or w2Indices is None:
			return 10000
		minDist = abs(w1Indices[0] - w2Indices[0])
		w1i = 1
		w2i = 1
		while w1i < len(w1Indices) and w2i < len(w2Indices):
			dist = abs(w1Indices[w1i] - w2Indices[w2i])
			if dist < minDist:
				minDist = dist
			if w1Indices[w1i] < w2Indices[w2i]:
				w1i+=1
			else:
				w2i+=1
		while w1i < len(w1Indices):
			dist = abs(w1Indices[w1i] - w2Indices[-1])
			if dist < minDist:
				minDist = dist
			w1i+=1
		while w2i < len(w2Indices):
			dist = abs(w1Indices[-1] - w2Indices[w2i])
			if dist < minDist:
				minDist = dist
			w2i+=1
		return minDist

	def findAllDistances(self):
		for i in range(len(self.arr)):
			cur = self.arr[i]
			self.mostRecentIndices[cur] = i
			for elem in self.arr:
				if cur!= elem and elem in self.mostRecentIndices:
					index = self.mostRecentIndices.get(elem)
					key = set()
					key.add(elem)
					key.add(cur)
					key = frozenset(key)
					minSoFar = self.map.get(key, i-index)
					self.map[key] = minSoFar if minSoFar < i-index else i-index

	def findSrcAndStart(self, w1, w2):
		for i in range(len(self.arr)):
			w = self.arr[i]
			if w == w1 or w == w2:
				return w, i

	def quickDist(self, w1, w2):
		key = set()
		key.add(w1)
		key.add(w2)
		key = frozenset(key)
		return self.map.get(key, 100000)

	def dist(self, w1, w2):
		src, start = self.findSrcAndStart(w1, w2)
		minDist = 100000 #todo use max int
		dest = w1 if src == w2 else w2
		for i in range(start+1, len(self.arr)):
			if self.arr[i] == src:
				start = i
			if self.arr[i] == dest:
				dist = i-start
				if dist < minDist:
					minDist = dist
				tmp = dest
				dest = src
				src = tmp
				start = i
		return minDist

if __name__ == '__main__':
	md = MinDist(["the", "quick", "brown", "fox", "quick"])
	print(md.dist("fox", "the"))
	print(md.quickDist("fox", "the"))
	print(md.mediumSpeedDist("fox", "the"))
	print(md.dist("quick", "fox"))
	print(md.quickDist("quick", "fox"))
	print(md.mediumSpeedDist("quick", "fox"))
	print(md.dist("fox", "quick"))
	print(md.quickDist("fox", "quick"))
	print(md.mediumSpeedDist("fox", "quick"))