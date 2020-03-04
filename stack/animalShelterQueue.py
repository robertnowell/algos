from datetime import datetime

class Dog(object):
    def __init__(self, name, prev=None, next=None):
        self.name = name
        self.prev = prev
        self.next = next
        self.time = None
        self.type = 'dog'

class Cat(object):
    def __init__(self, name, prev=None, next=None):
        self.name = name
        self.prev = prev
        self.next = next
        self.time = None
        self.type = 'cat'

class Queue:
    def __init__(self, node=None):
        if node:
            self.front = node
            self.back = node
        else:
            self.front = None
            self.back= None

    def __repr__(self):
        if self.isEmpty():
            return 'empty queue'
        else:
            s = ''
            tmp = self.front
            while tmp is not None:
                s += '({}, {}), '.format(tmp.name, tmp.time)
                tmp = tmp.next
            return s

    def peek(self):
        if self.isEmpty():
            raise ValueError('cannot peek empty queue')
        else:
            return self.front

    def isEmpty(self):
        return self.front is None

    def enqueue(self, node):
        if self.isEmpty():
            new = node
            self.front = self.back = new
        else:
            oldBack = self.back
            new = node
            new.prev = oldBack
            oldBack.next = node
            self.back = node

    def dequeue(self):
        if self.isEmpty():
            raise ValueError('cannot dequeue from empty queue')
        else:
            front = self.front
            self.front = self.front.next
            if self.front is not None:
                self.front.prev = None
            return front.name

class Shelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        animal.time = datetime.now()
        if animal.type == 'dog':
            self.dogs.enqueue(animal)
        else:
            self.cats.enqueue(animal)

    def dequeue(self):
        if self.dogs.isEmpty():
            if self.cats.isEmpty():
                raise ValueError('Shelter is empty :)')
            else:
                return self.cats.dequeue()
        else:
            if self.cats.isEmpty():
                return self.dogs.dequeue()
            else:
                return self.dogs.dequeue() if self.dogs.peek().time < self.cats.peek().time else self.cats.dequeue()

    def __repr__(self):
        return 'dogs: {}\ncats: {}\n'.format(self.dogs.__repr__(), self.cats.__repr__())

cats = [Cat('mittens'), Cat('archibald')]
dogs = [Dog('spot'), Dog('charlie')]

sh = Shelter()
sh.enqueue(cats[1])
sh.enqueue(dogs[1])
sh.enqueue(dogs[0])
sh.enqueue(cats[0])

print (sh)
print sh.dequeue()
print sh.dequeue()
print sh.dequeue()
print sh.dequeue()