def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

def extended_gcd(a, b):
  assert a >= b and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def diophantine(a, b, c):
  _a = max(a,b)
  _b = min(a,b)

  
  d, x, y = extended_gcd(_a, _b)
  assert c % d == 0
  factor = c / d
  # return (x, y) such that a * x + b * y = c
  return (x*factor, y*factor) if a > b else (y*factor, x*factor)

print(extended_gcd(10, 6))
a,b = 6, 10
x, y = diophantine(6, 10, 22)
print(a*x + b*y)