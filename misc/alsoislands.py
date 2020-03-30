# Given an empty NxN grid where each square is either water or land, write a data structure that can model this grid and exposes a function:

# addLand(row, col): int -> takes a location in the grid, if it is water, converts it to land, otherwise does nothing and then returns the number of islands in the grid.

# Example: 3x3 Grid

# W W W
# W W W
# W W W

# addLand(1, 0) -> 1:

# W W W
# L W W
# W W W

# addLand(1, 2) -> 2:

# W W W
# L W L
# W W W

# addLand(1, 1) -> ?:

# W W W
# L L L
# W W W

class IslandFinder():
	def __init__(self, size):
		self.size = size
		self.grid = [None] * size
		for i in range(size):
			self.grid[i] = [False] * size
		self.visited = set()
		self.seenThisTime = set()
		self.islandsCount = 0

	def inRange(self, x, y):
		return 0 <= x < self.size and 0 <= y < self.size

	def countNeighbors(self, x, y):
		c = 0
		for i in range(-1, 2, 2):
			xx = x+i
			if self.inRange(xx, y) and self.grid[xx][y]:
				c+=1
			yy = y+i
			if self.inRange(x, yy) and self.grid[x][yy]:
				c+=1
		return c

	def isUnseenIsland(self, x, y):
		key = (x, y)
		if key in self.visited:
			return False
		if key in self.seenThisTime:
			return True
		self.seenThisTime.add(key)
		isUnseen = True
		for i in range(-1, 2, 2):
			xx = x+i
			yy = y+i
			if (xx, y) != (self.curX, self.curY) and self.inRange(xx, y) and self.grid[xx][y]:
				isUnseen = self.isUnseenIsland(xx, y)
			if (x, yy) != (self.curX, self.curY) and self.inRange(x, yy) and self.grid[x][yy]:
				isUnseen = self.isUnseenIsland(x, yy)
		return isUnseen

	def countJoinedIslands(self, x, y):
		self.curX = x;
		self.curY = y;
		# import pdb; pdb.set_trace()
		self.visited = set()
		joined = 0
		for i in range(-1, 2, 2):
			xx = x+i
			self.seenThisTime.add((x, y))
			if self.inRange(xx, y) and self.grid[xx][y]:
				if self.isUnseenIsland(xx, y):
					joined += 1
			self.visited.update(self.seenThisTime)
			self.seenThisTime = set()

			yy = y+i
			self.seenThisTime.add((x, y))
			if self.inRange(x, yy) and self.grid[x][yy]:
				if self.isUnseenIsland(x, yy):
					joined += 1
			self.visited.update(self.seenThisTime)
			self.seenThisTime = set()
		return joined

	def addLand(self, x, y):
		# todo check invalid input
		if self.grid[x][y]:
			return self.islandsCount
		self.grid[x][y] = True
		n = self.countNeighbors(x, y)
		if n == 0:
			self.islandsCount += 1
		elif n > 1:
			diff = 1 - self.countJoinedIslands(x, y)
 			self.islandsCount += diff
 		return self.islandsCount

 	def __repr__(self):
 		s = ""
 		for i in range(self.size):
 			s += str(self.grid[i]) + "\n"
 		return s

if __name__ == '__main__':
	islands = IslandFinder(3)
	print "island count = ", islands.addLand(2, 1) # 1
	print islands

	# W W W
	# W W W
	# W L W

	print "island count = ", islands.addLand(1, 0) # 2
	print islands

	# W W W
	# L W W
	# W L W

	print "island count = ", islands.addLand(0, 2) # 3
	print islands

	# W W L
	# L W W
	# W L W
	# print islands

	print "island count = ", islands.addLand(1, 1) # 2
	print islands

	# W W L
	# L L W
	# W L W

	# print islands
	print "island count = ", islands.addLand(1, 2) # 1
	# print islands

	# W W L
	# L L L
	# W L W
	print islands

	print "island count = ", islands.addLand(0, 1) # 1
	print islands

	# W L L
	# L L L
	# W L W