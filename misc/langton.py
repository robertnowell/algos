class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
FACTOR = .1
class LangtonSim(object):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

	def __init__(self, k):
		super(LangtonSim, self).__init__()
		self.k = k
		self.grid = []
		self.rows = 10
		self.cols = 10

		for i in range(self.rows):
			self.grid += [[True] * self.cols]
		self.antRow = self.rows/2
		self.antCol = self.cols/2
		self.antDir = LangtonSim.WEST
		for i in range(k):
			if (i % 10000 == 0): 
				print(i)
				# self.printGrid()
			self.move()
		self.printGrid()

	def printGrid(self):
		s = ""
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				char = -1
				if i == self.antRow and j == self.antCol:
					char = bcolors.BOLD + 'X'
				else:
					char = bcolors.OKGREEN + '1' if self.grid[i][j] else bcolors.OKBLUE + '0'
				s += char + bcolors.ENDC + ", "
			s += '\n'
		print(s)

	def resize(self):
		if self.antRow == self.rows:
			print("resizing by appending rows")
			rowsToAppend = int(self.rows * FACTOR)
			for i in range(rowsToAppend):
				self.grid += [[True] * self.cols]
			self.rows += rowsToAppend
			self.antRow -= 1
		elif self.antRow < 0:
			print("resizing by prepending rows")
			rowsToPrepend = int(self.rows * FACTOR)
			
			self.antRow += rowsToPrepend + 1
			prependGrid =[]
			for i in range(rowsToPrepend):
				prependGrid += [[True] * self.cols]
			self.grid = prependGrid + self.grid
			self.rows += rowsToPrepend
		if self.antCol == self.cols:
			colsToAppend = int(self.cols * FACTOR)
			print("resising by appending cols")
			for i in range(self.rows):
				self.grid[i] += [True] * colsToAppend
			self.cols += colsToAppend
			self.antCol -= 1
		elif self.antCol < 0:
			colsToPrepend = int(self.cols * FACTOR)
			print("resising by prepending cols: " + str(colsToPrepend))
			print("prev antCol" + str(self.antCol))
			for i in range(self.rows):
				self.grid[i] = [True] * colsToPrepend + self.grid[i]
			self.antCol += colsToPrepend + 1
			self.cols += colsToPrepend
			print("post antCol" + str(self.antCol))

	def move(self):
		isWhite = self.grid[self.antRow][self.antCol]
		self.grid[self.antRow][self.antCol] = not self.grid[self.antRow][self.antCol]
		if isWhite:
			self.antDir = self.antDir - 1 if self.antDir > 0 else 3
		else:
			self.antDir = self.antDir + 1 if self.antDir < 3 else 0
		# print('direction: ' + str(self.antDir))
		if self.antDir == LangtonSim.NORTH:
			self.antCol -= 1
		elif self.antDir == LangtonSim.EAST:
			self.antRow += 1
		elif self.antDir == LangtonSim.SOUTH:
			self.antCol += 1
		elif self.antDir == LangtonSim.WEST:
			self.antRow -= 1
		self.resize()
if __name__ == '__main__':
	LangtonSim(500000)
