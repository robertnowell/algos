class PatternMatcher():
	def __init__(self, s, p):
		self.astr = ""
		self.bstr = ""
		self.s = s
		self.p = p
		self.aCount = self.getCount('a')
		self.bCount = self.getCount('b')
		self.length = len(s)
		self.possibilities = []
		self.setPossibilities()

	def getCount(self, c):
		return len([char for char in self.p if char == c])

	def testPattern(self):
		for a, b in self.possibilities:
			self.astr = ""
			self.bstr = ""
			if self.isMatch(a, b):
				print ("match found: ", a, b)
				return True
		return False

	def check(self, c, string, n, i):
		print 'here'
		if (len(string) < n):
			if c == 'a':
				self.astr = self.s[i: i+n]
			if c == 'b':
				self.bstr = self.s[i: i+n]
		elif string != self.s[i: i+n]:
			raise Error("bad bad")
		return i+n

	def isMatch(self, a, b):
		i = 0
		for c in self.p:
			try:
				i = self.check(c, self.astr, a, i) if c == 'a' else self.check(c, self.bstr, b, i)
			except:
				return False
		print (a, b)
		return True

	def setPossibilities(self):
		print(self.aCount)
		print(self.bCount)
		if self.aCount == 0:
			maxA = 1
			minA = 0
		else:
			maxA = self.length/self.aCount +1
			minA = 1
		if self.bCount == 0:
			maxB = 1
			minB = 0
		else:
			maxB = self.length/self.bCount + 1
			minB = 1

		for a in range(minA, maxA):
			for b in range(minB, maxB):
				print (a, b)
				if a*self.aCount + b*self.bCount == self.length:
					self.possibilities += [(a, b)]
		print self.possibilities

value = "acgocacgoc"
pattern = "abab"
pm = PatternMatcher(value, pattern)
print(pm.testPattern())
