class Hanoi(object):
  def __init__(self, n):
    self.n = n
    self.moves = 0
    self.one = []
    self.two = []
    self.three = []
    for i in range(n, 0, -1):
      self.one.append(i)

  def hanoi(self):
    self.solve(self.n, self.one, self.two, self.three)

  def solve(self, n, source, destination, aux):
    if n == 1:
      destination.append(source.pop())
      self.moves += 1
    else:
      self.solve(n-1, source, aux, destination)
      destination.append(source.pop())
      self.moves += 1
      self.solve(n-1, aux, destination, source)

import sys

h = Hanoi(int(sys.argv[1]))
print h.one, h.two, h.three

h.hanoi()
print h.one, h.two, h.three
print h.moves
