












def binary_search_recursive(sequence, low, high, value, ops):
  ops += 1
  if low > high:
    print 'number of calls in binary search: ' + str(ops)
    return -1
  mid = (low + high) / 2
  if sequence[mid] == value:
    print 'number of calls in binary search: ' + str(ops)
    return mid
  elif sequence[mid] > value:
    return binary_search_recursive(sequence, low, mid - 1, value, ops)
  elif sequence[mid] < value:
    return binary_search_recursive(sequence, mid + 1, high, value, ops)





































def binary_search_iterative(sequence, value, ops):
    low, high = 0, len(sequence) - 1
    while low <= high:
      ops += 1
      mid = (low + high) // 2
      if sequence[mid] < value:
        low = mid + 1
      elif value < sequence[mid]:
        high = mid - 1
      else:
        print 'number of calls in binary search: ' + str(ops)
        return mid
    print 'number of calls in binary search: ' + str(ops)
    return None












def simple_search(sequence, value):
  ops = 0
  for i in range(len(sequence)):
    ops += 1
    if sequence[i] == value:
      break
  print 'number of calls in simple value: ' + str(ops)
  if sequence[i] == value:
    return i
  else:
    return -1

















sequence = range(1, 10000001, 1)
value = 10000000
ops = 0
binary_search_iterative(sequence, value, ops)

ops = 0
simple_search(sequence, value)
