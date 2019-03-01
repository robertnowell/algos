import itertools as it

count = 0

def extend(perm, n):
  global count
  if len(perm) == n:
    count += 1
    return

  for k in range(n):
    if k not in perm:
      perm.append(k)
      if valid_so_far(perm, n):
        extend(perm, n)
      perm.pop()

def valid_so_far(perm, n):
  for i,j in it.combinations(range(len(perm)), 2):
    if abs(perm[i] - perm[j]) == abs(i-j):
      return False
  return True

def queens(n):
  extend([], n)

queens(8)
print count