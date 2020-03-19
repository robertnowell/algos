class Node():
	def __init__(self, value):
		self.value = value
		self.nodes = [None] * 26

	def isLeaf(self):
		return self.nodes == [None] * 26

class Trie():
	def __init__(self):
		self.root = Node(None)
		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def letterToInt(self, c):
		return self.alphabet.index(c)

	def containsPrefix(self, s):
		node = self.root
		for char in s:
			i = self.letterToInt(char)
			node = node.nodes[i]
			if node is None:
				return False
		return True

	def add(self, s):
		node = self.root
		for c in s:
			i = self.letterToInt(c)
			newNode = node.nodes[i]
			if newNode is None:
				node.nodes[i] = Node(c)
				newNode = node.nodes[i]
			node = newNode

	def printRecursive(self, node, soFar):
		if soFar != []:
			print(soFar)
		if (node.isLeaf()):
			return

		for n in node.nodes:
			if n is not None:
				self.printRecursive(n, soFar + [n.value])

	def p(self):
		for node in self.root.nodes:
			if node is not None:
				self.printRecursive(node, [node.value])

if __name__ == '__main__':
	t = Trie()
	t.add("test")
	t.add("best")
	t.add("binary")
	t.p()
	print(t.containsPrefix("binar"))
	print(t.containsPrefix("binare"))