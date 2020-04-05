class matrixSum():
    def __init__(self, grid):
        self.grid = grid
        self.size = len(grid)
    """
        consider all possibilities
            for each row r
                for each column c
                    check all submatrices right and down from this cell
                    for each row r2 from r until end of grid
                        for each column c2 from c until end of grid
                            compute sum of grid
                            sum is zero
                                to compute sum of grid
                                    for each row r3 from r1 to r2
                                        for each column c3 from c1 to c2
                                            add grid[r3][c3] to sum
                            if sum exceeds max:
                                replace sum

    """
    def mum(self):
        bestSum = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                for ii in range(i, len(self.grid)):
                    for jj in range(j, len(self.grid[ii])):
                        s = 0
                        for iii in range(i, ii+1):
                            for jjj in range(j, jj+1):
                                s += self.grid[iii][jjj]
                        if s > bestSum:
                            print("new sum found: rows ({}:{}) cols ({}:{}) sum {}".format(i,ii, j, jj, sum))
                            bestSum = s
        return bestSum
    
if __name__ == "__main__":
    g = [ [-5, -6, 2, 1, -1], [-1, -1, -1, -1, -1], [6, 6, 6, 6, 6], [-1, -1, 2, -1, 2], [3, 2, 1, 0, -1]]
    m = matrixSum(g)
    print(m.mum())
