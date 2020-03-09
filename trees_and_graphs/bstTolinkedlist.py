class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left or None
		self.right = right or None

	def setLeft(self, node):
		self.left = node

	def setRight(self, node):
		self.right = node

def findLeft(node):
	while node is not None and node.left is not None:
		node = node.left
	return node

def findRight(node):
	while node is not None and node.right is not None:
		node = node.right
	return node

def traverse(node):
	if node is None:
		return None
	left = traverse(node.left)
	if left is not None:
		leftRight = findRight(left)
		node.setLeft(leftRight)
		leftRight.setRight(node)
	right = traverse(node.right)
	if right is not None:
		rightLeft = findLeft(right)
		node.setRight(rightLeft)
		rightLeft.setLeft(node)
	return node

def inorder(node):
	# import pdb; pdb.set_trace();
	if node is not None:
		inorder(node.left)
		print(node.data)
		inorder(node.right)

"""
			8
	3				10
1		6					14
	4		7			13
"""
if __name__ == '__main__':
	eight = Node(8)
	three = Node(3)
	ten = Node(10)
	one = Node(1)
	six = Node(6)
	fourteen = Node(14)
	four = Node(4)
	seven = Node(7)
	thirteen = Node(13)

	eight.setLeft(three)
	eight.setRight(ten)
	three.setLeft(one)
	three.setRight(six)
	six.setLeft(four)
	six.setRight(seven)
	ten.setRight(fourteen)
	fourteen.setLeft(thirteen)
	node = traverse(eight)
	import pdb;pdb.set_trace();
	
