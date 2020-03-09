class BabyNames():
	def __init__(self, counts, synonyms):
		self.counts = counts
		self.synonyms = synonyms
		self.visited = set()

	def babyNames(self):
		for name in self.counts.keys():
			if not name in self.visited:
				print(name, self.countSimilar(name))

	def countSimilar(self, name):
		n = 0
		if name in self.visited or not self.counts.has_key(name):
			return n
		n += self.counts[name]
		self.visited.add(name)
		for sim in self.getSynonyms(name):
			n += self.countSimilar(sim)
		return n

	def getSynonyms(self, name):
		return self.synonyms[name]

if __name__ == '__main__':
	counts = {
		'John': 15,
		'Jon': 12,
		'Chris': 13,
		'Kris': 4,
		'Christopher': 19,
	}
	synonyms = {
		'Jon': ['John'],
		'John': ['Jon', 'Johnny'],
		'Johnny': ['John'],
		'Chris': ['Kris'],
		'Kris': ['Chris', 'Christopher'],
		'Christopher': ['Chris']
	}
	bn = BabyNames(counts, synonyms)
	bn.babyNames()
