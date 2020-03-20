# it = [1,2,3].__iter__()
# next(it) -> 1 or throw error

# next(), hasNext(), peek()
# different kinds of input
# empty iterator

# FlattenIterator([Iterator1, Iterator2])
#    next() -> return the next object in the next iterator
#    hasNext()
#    peek()

class FlattenIterator():
    def __init__(self, its):
        self.its = its
        self.index = 0
        # check empty list
        self.current = its[0] 
        self.setNext()

    def setNext(self):
        if self.current.hasNext():
            self._next = self.current.next()
        else:
            self.updateCurrent()
            self._next = self.current.next()

    def next(self):
        if self.hasNext():
            ret = self._next
            self.setNext()
            return ret

    def updateCurrent(self):
        self.index += 1
        if self.index < len(self.its):
            self.current = self.its[self.index]
    
    def hasNext(self):
        return self._next is not None
    
    def peek(self):
        return self._next

class Iterator():
    def __init__(self, it):
        self.it = it
        self.setNext()

    def setNext(self):
        try:
            self._next = next(self.it)
        except:
            self._next = None

    def next(self):
        if self._next is not None:
            ret = self._next
            self.setNext()
            return ret

    # return a boolean of whether the iterator is nonempty
    def hasNext(self):
        return self._next is not None

    # return the result of calling next without changing state of iterator object
    def peek(self):
        return self._next

if __name__ == '__main__':
    it = [1,2,3].__iter__()
    it2 = ["4","5","6"].__iter__()
    # it = [None, None, None].__iter__()

    i1 = Iterator(it)
    i2 = Iterator(it2)
    # iterator = FlattenIterator([i1])

    iterator = FlattenIterator([i1, i2])

    while (iterator.hasNext()):
        # print(iterator.peek())
        print(iterator.next())
    # for i in range(3):
    #     print(iterator.next())
    

        