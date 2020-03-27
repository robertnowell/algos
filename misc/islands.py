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


"""
if our x,y does not have land north,south,east,west
-result is number of islands plus one

if our x,y has one neighbor:
-result is number of islands

if our x,y has multiple neighbors:

# W W W
# L X L
# W W W
-join two islands, islandscount-1

# W W W
# L W L
# W L W
join three, islandcount-2

# W L W
# L W L
# W L W
join four, islandcount-3

# W L L
# L W L
# L L W
join four, islandcount-1

what we can do is for each land neighbor, recursively search from that neighbor to count number of adjacent islands.
base case: visited: return false
for each land neighbor: visitIsland return false if newIsland = !(recurse)
return true

"""
class Grid:
    def __init__(self, size):
        self.size = size
        self.numberOfIslands = 0
        self.grid = self.initGrid(size)
        print(self.grid)

    def initGrid(self, size):
        grid = [False] * size;
        for i in range(size):
            grid[i] = [False] * size
        return grid

    def isDistinctIsland(self, visited, seenThisExploration, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size or self.grid[x][y] is False or (x,y) in seenThisExploration:
            return True
        if self.grid[x][y] in visited:
            return False
        seenThisExploration.add((x,y))
        # print(seenThisExploration);
        isNewIsland = True
        isNewIsland = self.isDistinctIsland(visited,seenThisExploration, x-1, y)
        isNewIsland = self.isDistinctIsland(visited,seenThisExploration, x, y-1)
        isNewIsland = self.isDistinctIsland(visited,seenThisExploration, x+1, y)
        isNewIsland = self.isDistinctIsland(visited,seenThisExploration, x, y+1)
        return isNewIsland

    def determineJoinedIslands(self, x,y):
        joinedIslands = 0
        visited = set()
        seenThisExploration = set();
        seenThisExploration.add((x,y))

        # print joinedIslands;
        xx = x-1
        yy = y
        if xx >= 0 and xx < self.size and yy >= 0 and yy < self.size and self.grid[xx][yy] and self.isDistinctIsland(visited,seenThisExploration, xx, yy):
            joinedIslands += 1
        print joinedIslands;

        visited.update(seenThisExploration)

        seenThisExploration = set();
        xx = x
        yy = y-1
        import pdb; pdb.set_trace()
        if xx >= 0 and xx < self.size and yy >= 0 and yy < self.size and self.grid[xx][yy]:
            print (xx, yy, self.grid)
            res = self.isDistinctIsland(visited,seenThisExploration, xx, yy)
            joinedIslands += 1 if res else 0
        print joinedIslands;

        visited.update(seenThisExploration)
        seenThisExploration = set();
        xx = x+1
        yy = y
        if xx >= 0 and xx < self.size and yy >= 0 and yy < self.size and self.grid[xx][yy] and self.isDistinctIsland(visited,seenThisExploration, xx, yy):
            joinedIslands += 1
        print joinedIslands;
        visited.update(seenThisExploration)

        seenThisExploration = set();
        xx = x
        yy = y+1
        if xx >= 0 and xx < self.size and yy >= 0 and yy < self.size and self.grid[xx][yy] and self.isDistinctIsland(visited,seenThisExploration, xx, yy):
            joinedIslands += 1
        print joinedIslands;
        return joinedIslands;

    def countNeighbors(self, x, y):
        neighbors = 0;
        xx = x-1
        yy = y
        neighbors += 1 if ((0 <= xx < self.size) and (0 <= yy < self.size) and self.grid[xx][yy]) else 0
        xx = x
        yy = y-1
        neighbors += 1 if ((0 <= xx < self.size) and (0 <= yy < self.size) and self.grid[xx][yy]) else 0

        xx = x+1
        yy = y
        neighbors += 1 if ((0 <= xx < self.size) and (0 <= yy < self.size) and self.grid[xx][yy]) else 0

        xx = x
        yy = y+1
        neighbors += 1 if ((0 <= xx < self.size) and (0 <= yy < self.size) and self.grid[xx][yy]) else 0
        return neighbors

    def add_land(self, x, y):
        # todo check invalid input
        if self.grid[x][y]:
            return self.numberOfIslands
        neighbors = self.countNeighbors(x, y)
        self.grid[x][y] = True;
        if neighbors == 0:
            self.numberOfIslands += 1
            return self.numberOfIslands
        if neighbors == 1:
            return self.numberOfIslands
        print(x, y, neighbors)

        diff = 1 - self.determineJoinedIslands(x, y)
        self.numberOfIslands += diff
        return self.numberOfIslands;

grid = Grid(3)
print(grid.add_land(1, 0))
print(grid.add_land(1, 2))
print(grid.add_land(1, 1))