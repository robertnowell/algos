import random

# def change(coins, n):
#   assert n > 23
#   if n == 24:
#     return coins + [5,5,7,7]
#   if n == 25:
#     return coins + [5,5,5,5,5]
#   if n == 26:
#     return coins + [7, 7, 7, 5]
#   if n == 27:
#     return coins + [5, 5, 5, 5, 7]
#   if n == 28:
#     return coins + [7, 7, 7, 7]
#   return change(coins + [5], n-5)


def change(amount):
  assert amount > 23
  if amount == 24:
    return [5,5,7,7]
  if amount == 25:
    return [5,5,5,5,5]
  if amount == 26:
    return [7, 7, 7, 5]
  if amount == 27:
    return [5, 5, 5, 5, 7]
  if amount == 28:
    return [7, 7, 7, 7]

  coins = change(amount-5)
  return coins + [5]

def test_change():
  for i in range(100):
    target = random.randint(24, 5000)
    l = change(target)
    assert target == sum(l)

test_change()