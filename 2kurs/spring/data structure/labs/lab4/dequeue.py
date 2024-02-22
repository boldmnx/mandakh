class Deq:
    def __init__(self):
        self.deq = []

    # add_front
    def add_front(self, e):
        self.deq += [0]
        for i in range(len(self.deq)-1, 0, -1):
            self.deq[i] = self.deq[i-1]
        self.deq[0] = e

    def add_end(self, e):
        self.deq += [e]

    # delete_front
    def delete_front(self):
        self.deq = self.deq[1:]
    # delete_End

    def delete_end(self):
        l = self.deq[-1]
        self.deq = self.deq[:-1]
        return l

    # read front
    def first(self):
        f = self.deq[0]
        return f

    # read end
    def last(self):
        l = self.deq[-1]
        print(l)

    # len
    def len(self):
        c = 0
        for i in self.deq:
            c += 1
        print(c)

    # isEmpty
    def is_empty(self):
        print(self.len() == 0)

    # read
    def read(self):
        print(self.deq)

    def __str__(self):
        return str(self.deq)


deq = Deq()
deq.add_end(5)
deq.read()

deq.add_front(3)
deq.read()

deq.add_front(7)
deq.read()

print(deq.first())
print(deq.delete_end())

deq.read()
deq.len()

print(deq.delete_end())
print(deq.delete_end())

deq.add_front(6)
deq.read()
deq.last()

deq.add_front(8)
deq.read()

deq.is_empty()
deq.last()


print(type(deq))
# [1, 2, 3]
# lifo 3 stack
# fifo 1 queue
