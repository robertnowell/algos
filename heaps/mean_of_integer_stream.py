def mean_of_int_stream(n, max_heap, min_heap):
  """ add n to correct heap, balance heaps, and return the mean
  """
  if n < max_heap.max():
    max_heap.insert(n)
  else:
    min_heap.insert(n)

  balance_heaps(max_heap, min_heap)

  if max_heap.count() > min_heap.count():
    return max_heap.max()
  elif min_heap.count() > max_heap.count():
    return min_heap.min()
  else:
    return (max_heap.max() + min_heap.min())/2

def balance_heaps(h1, h2):
  """rearrange elements of two heaps to ensure that the quantity of elements in each heap does not differ by more than one."""
  return

class MinHeap:
  def __init__(self):
    self.heapList = [0]
    self.max_index = 0

  def bubble_down(self, i):
    # if (2 * i + 1) > self.max_index:
    #   if self.heapList[i] > self.heapList[2 * i]:
    #     tmp = self.heapList[i]
    #     self.heapList[i] = self.heapList[2 * i]
    #     self.heapList[2 * i] = tmp
    if self.heapList[i] > self.heapList[2 * i] or self.heapList[i] > self.heapList[2 * i + 1]:
      k = (2 * i) if self.heapList[2 * i] <= self.heapList[2 * i + 1] else (2 * i + 1)
      tmp = self.heapList[k]
      self.heapList[k] = self.heapList[i]
      self.heapList[i] = tmp
      if (2 * k) <= self.max_index:
        self.bubble_down(k)

  def bubble_up(self, i):
    if self.heapList[i] < self.heapList[i / 2]:
      tmp = self.heapList[i]
      self.heapList[i] = self.heapList[i / 2]
      self.heapList[i / 2] = tmp
      self.bubble_up(i / 2)

  def insert(self, n):
    self.heapList.append(n)
    self.max_index = self.max_index + 1
    self.bubble_up(self.max_index)

  # this came from the internet, and I decided to write my own. Kept around for reference, for now
  # def percUp(self, i):
  #   while i // 2 > 0:
  #     if self.heapList[i] < self.heapList[i // 2]:
  #        tmp = self.heapList[i // 2]
  #        self.heapList[i // 2] = self.heapList[i]
  #        self.heapList[i] = tmp
  #     i = i // 2

test = MinHeap()
test.heapList = [10, 1, 3, 4, 5, 6, 7, 8, 0, 0, 0]
test.max_index = len(test.heapList) - 1
# test.insert(2)
test.bubble_down(0)
print test.heapList