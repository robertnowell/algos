import random
class Rand7FromRand5():
	def __init__(self):
		self.map = {}
		self.combs = []
		self.getCombs()
		self.initMap()
		self.res = {}
		for i in range(200000000):
			val = self.sevenFromFive()
			self.res[val] = self.res.get(val, 0) + 1
		print self.res

	def rand5(self):
		return random.randint(0, 4)

	def sevenFromFive(self):
		one = self.rand5()
		two = self.rand5()
		three = self.rand5()
		return self.map[tuple(sorted([one, two, three]))]

	def initMap(self):
		# combs = set()
		# for i in range(5):
		# 	for j in range(5):
		# 		for k in range(5):
		# 			combs.add(tuple(sorted([i, j, k])))
		l = 0
		for comb in self.combs:
			# print (comb, l)
			self.map[comb] = l
			l = 0 if l == 6 else l+1

	def helper(self, arr, chosen, index, start, end):
		if index == 3:
			comb = (arr[chosen[0]], arr[chosen[1]], arr[chosen[2]])
			self.combs += [comb]
		else:
			for i in range(start, end+1):
				chosen[index] = i
				self.helper(arr ,chosen,  index+1, i, end)			

	def getCombs(self):
		arr = [0, 1, 2, 3, 4]
		chosen = [0, 0, 0]
		self.helper(arr, chosen, 0, 0, 4)
		print(len(self.combs))
		print(self.combs)

if __name__ == '__main__':
	Rand7FromRand5()