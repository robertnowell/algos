def valid_so_far(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      current = grid[i][j]
      if current == 1:
        # check diagonals
        ii = i-1
        jj = j-1
        if ii >= 0 and jj >= 0:
          if grid[ii][jj] == current:
            print message(grid, i, j, current, ii, jj, grid[ii][jj], "/ left and above")
            return False 
        ii = i + 1
        jj = j + 1
        if ii < len(grid) and jj < len(grid[0]):
          if grid[ii][jj] == current:
            print message(grid, i, j, current, ii, jj, grid[ii][jj], "/ right and below")
            return False 

        # check horizontals
        jj = j - 1
        if jj >= 0:
          if grid[i][jj] == 2:
            print message(grid, i, j, current, i, jj, grid[i][jj], "/ horizontal left")
            return False 
        jj = j + 1
        if jj < len(grid[0]):
          if grid[i][jj] == 2:
            print message(grid, i, j, current, i, jj, grid[i][jj], "/ horizontal right")
            return False 

        # check verticals
        ii = i - 1
        if ii >= 0:
          if grid[ii][j] == 2:
            print message(grid, i, j, current, ii, j, grid[ii][j], "/ vertical above")
            return False 
        ii = i + 1
        if ii < len(grid):
          if grid[ii][j] == 2:
            print message(grid, i, j, current, ii, j, grid[ii][j], "/ vertical below)")
            return False

      if current == 2:
        # check diagonals
        ii = i+1
        jj = j-1
        if ii < len(grid) and jj >= 0:
          if grid[ii][jj] == current:
            print message(grid, i, j, current, ii, jj, grid[ii][jj], "\\ left and below")
            return False 
        ii = i-1
        jj = j+1
        if ii >= 0 and jj < len(grid[0]):
          if grid[ii][jj] == current:
            print message(grid, i, j, current, ii, jj, grid[ii][jj], "\\ right and above")
            return False

        # check horizontals
        jj = j - 1
        if jj >= 0:
          if grid[i][jj] == 1:
            print message(grid, i, j, current, i, jj, grid[i][jj], "\\ horizontal right")
            return False
        jj = j + 1
        if jj < len(grid[0]):
          if grid[i][jj] == 1:
            print message(grid, i, j, current, i, jj, grid[i][jj], "\\ horizontal left")
            return False

        # check verticals
        ii = i - 1
        if ii >= 0:
          if grid[ii][j] == 1:
            print message(grid, i, j, current, i, jj, grid[i][jj], "\\ vertical above")
            return False
        ii = i + 1
        if ii < len(grid):
          if grid[ii][j] == 1:
            print message(grid, i, j, current, ii, j, grid[ii][j], "\\ vertical below")
            return False

  return True

def message(grid, i,j, current, ii,jj, conflict, s):
  return "grid:\n{} \ncurrent:  [{}, {}]: {}\nconflict: [{}, {}]: {}\n{}".format(
          pretty_grid(grid), i, j, current, ii, jj, conflict, s)

def pretty_grid(grid):
  res = ""
  for i in range(len(grid)):
    res += str(grid[i]) + "\n"
  return res

def extend(grid, i, j, n, count):
  if(n == count):
    print(pretty_grid(grid))
    return
  if not (i < len(grid)):
    return

  for k in range(3):
    grid[i][j] = k
    if valid_so_far(grid):
      ii = i
      jj = j + 1
      if not jj < len(grid[0]):
        ii += 1
        jj = 0
      if k != 0:
        extend(grid, ii, jj, n, count + 1)
      else:
        extend(grid, ii, jj, n, count)

# extend([[0,0],[0,0]], 0, 0, 3, 0)
# print valid_so_far([[2,2],[2,2]])



















def _extend(grid, i, j, n, count):
  if(n == count):
    print(pretty_grid(grid))
    return
  if not (i < len(grid)):
    return

  for k in range(3):
    grid[i][j] = k
    ii = i
    jj = j + 1
    if not jj < len(grid[0]):
      ii += 1
      jj = 0
    if k != 0:
      _extend(grid, ii, jj, n, count + 1)
    else:
      _extend(grid, ii, jj, n, count)

_extend([[0,0],[0,0]], 0, 0 , 3, 0)