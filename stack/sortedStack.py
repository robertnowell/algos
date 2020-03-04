class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class stack:
    def __init__(self, data=None):
        self.front = None
        if data:
            self.front = node(data, None)

    def peek(self):
        if self.front is None:
            raise ValueError('stack is empty')
        return self.front.data

    def isEmpty(self):
        return self.front == None

    def push(self, val):
        if self.front is not None:
            oldFront = self.front
            self.front = node(val, oldFront)
        else:
            self.front = node(val, None)

    def pop(self):
        if self.front is None:
            raise ValueError('stack is empty')
        popped = self.front.data
        self.front = self.front.next
        return popped

    def __repr__(self):
        copy = self.front
        if copy is None:
            return 'Empty stack'
        s = ''
        while (copy is not None):
            s += str(copy.data) + ', '
            copy = copy.next
        return s

def testStack():
    test = stack(3)
    assert test.__repr__() == '3, '
    test.push(4)
    assert test.__repr__() == '4, 3, '
    test.pop()
    assert test.__repr__() == '3, '
    test.pop()
    assert test.__repr__() == 'Empty stack'
    try:
        test.pop()
    except ValueError:
        pass
    print('1 test passed')

testStack()
class sortedStack:
    def __init__(self):
        self.left = stack()
        self.right = stack()

    def isEmpty(self):
        return self.left.isEmpty() and self.right.isEmpty()

    def __repr__(self):
        return 'l: ' + self.left.__repr__() + '\nright: ' + self.right.__repr__() + '\n'

    def printAscending(self):
        self._moveAllLeft()
        print(self.left.__repr__())

    def _moveAllLeft(self):
        while not self.right.isEmpty():
            self.left.push(self.right.pop())

    def _moveLeftUntilPushable(self, val):
        while not self.right.isEmpty() and self.right.peek() > val:
            self.left.push(self.right.pop())

    def _moveRightUntilPushable(self, val):
        while not self.left.isEmpty() and self.left.peek() < val:
            self.right.push(self.left.pop())

    def push(self, val):
        if self.isEmpty():
            self.left.push(val)
        elif self.left.isEmpty():
            if self.right.peek() <= val:
                # new val is greater than / equal to max
                self.left.push(val)
            else:
                # new val is less than max, so not ready to push val
                self._moveLeftUntilPushable(val)
                self.left.push(val)
        else:
            if self.right.isEmpty():
                if val <= self.left.peek():
                    self.left.push(val)
                else:
                    self._moveRightUntilPushable(val)
                    self.left.push(val)
            else:
                # neither side is empty, so need to either move left or right
                if self.left.peek() >= val:
                    if self.right.peek() <= val:
                        self.left.push(val)
                    else:
                        self._moveLeftUntilPushable(val)
                        self.left.push(val)
                else:
                    self._moveRightUntilPushable(val)
                    self.left.push(val)

t = sortedStack()
t.push(1)
print(t)
t.push(1)
print(t)
t.push(2)
print(t)
t.push(0)
print(t)

t.printAscending()