from math import pow, log, sqrt
import operator
from pprint import pprint


def one(n):
  return pow(3,n)

def two(n):
  return n*log(n,2)

def three(n):
  return log(n, 4)

def four(n):
  return n

def five(n):
  return pow(5, log(n, 2))

def six(n):
  return pow(n,2)

def seven(n):
  return sqrt(n)

def eight(n):
  return pow(2, 2*n)


n = 500
fs = {
  '1': one(n),
  '2': two(n),
  '3': three(n),
  '4': four(n),
  '5': five(n),
  '6': six(n),
  '7': seven(n),
  '8': eight(n)
}



# fs = sorted(fs.items(), key=operator.itemgetter(0))
pprint(sorted(fs, key=lambda x: fs[x]))
# pprint(sorted(fs.items(), key=operator.itemgetter(0)))
# for key in fs:
#   print "{}: {}".format(key, fs[key])