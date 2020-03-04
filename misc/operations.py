class ops():
	def __init__(self, arr):
		self.arr = arr
		self.stackNums = []
		self.stackOps = []
		self.operations = ['/', '+', '*', '-']
		self.priorities = {'/': 1, '*': 1, '+':0, '-': 0}
		print (self.execOps())

	def execOps(self):
		for elem in self.arr:
			# print("elem ", elem)
			if elem in self.operations:
				while(len(self.stackOps) > 0 and self.priorities[elem] <= self.priorities[self.stackOps[len(self.stackOps) -1]]):
					op = self.stackOps.pop()
					op2 = self.stackNums.pop()
					op1 = self.stackNums.pop()
					res = self.ex(op, op1, op2)
					# print (op1, op, op2, res)
					self.stackNums.append(res)
				self.stackOps.append(elem)
			else:
				self.stackNums.append(elem)
			# print("after")
			# print (self.stackNums)
			# print (self.stackOps)
			# print("")
		op = self.stackOps.pop()
		op1 = self.stackNums.pop()
		op2 = self.stackNums.pop()
		return self.ex(op, op1, op2)

	def ex(self, op, op1, op2):
		if (op == '/'):
			return float(op1)/float(op2)
		if (op == '*'):
			return float(op1)*float(op2)
		if (op == '+'):
			return float(op1) + float(op2)
		if (op == '-'):
			return float(op1) - float(op2)

if __name__ == '__main__':
	# ops([2, '-', 6, '-', 7, '*', 8, '/', 2, '+', 5])
	ops([2, '*', 3, '+', 5, '/', 6, '*', 3, '+', 15])