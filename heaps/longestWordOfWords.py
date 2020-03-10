class Longest():
	def __init__(self):	
		self.maxSoFar = 0
		self.word = ""
		self.words = set()
		self.words.add("cat")
		self.words.add("dog")
		self.words.add("walk")
		self.words.add("nana")
		self.words.add("walker")
		self.words.add("dogwalker")
		self.words.add("banana")
		self.maxLen = max([len(word) for word in self.words])
		for w in self.words:
			self.longest(w)
		print(self.word, self.maxSoFar)

	def longest(self, current):
		if len(current) > self.maxLen:
			return
		print(current)
		if current in self.words:
			print(current)
			if len(current) > self.maxSoFar:
				self.word = current
				self.maxSoFar = len(current)
		for w in self.words:
			self.longest(current+w)

if __name__ == '__main__':
	Longest()