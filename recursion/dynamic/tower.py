class Tower():
	def __init__(self, input):
		self.input = input
		self.memo = {}
		print(self.tower([]))

	def lessThan(self, choice, final):
		if final is None:
			return True
		if choice[0] < final[0] and choice[1] < final[1]:
			return True
		return False

	def tower(self, soFar):
		maxLen = len(soFar)
		final = soFar[maxLen-1] if maxLen > 0 else None
		maxSoFar = list(soFar)
		for choice in self.input:
			if self.lessThan(choice, final) and choice not in soFar:
				soFar += [choice]
				if not tuple(soFar) in self.memo:
					self.memo[tuple(soFar)] = self.tower(soFar)
				res = self.memo[tuple(soFar)]
				if len(res) > maxLen:
					maxLen = len(res)
					maxSoFar = res
				try:
					del soFar[len(soFar)-1]
				except:
					import pdb; pdb.set_trace()
		return maxSoFar

if __name__ == '__main__':
	input = [
		(65, 100),
		(70, 150),
		(56, 90),
		(75, 190),
		(1, 93),
		(2, 94),
		(60, 95),
		(68, 110),
	]
	t = Tower(input)
