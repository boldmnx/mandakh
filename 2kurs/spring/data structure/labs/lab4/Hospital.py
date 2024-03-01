from dequeue import Deq


class HospitalQueue:

    def __init__(self):
        self.dque = Deq()

    def add(self, a):
        if a["rank"] == 1:
            # print("r1")
            return self.dque.fadd(a)
        else:
            # print("r2")
            return self.dque.ladd(a)

    def dell(self):
        return self.dque.fdel()

    def first(self):
        return self.dque.first()

    def last(self):
        return self.dque.last()

    def total(self):
        return self.dque.len()

    def gettask(self):
        # print(self.dque.look())
        print(self.dque.look())


ovchton = HospitalQueue()

ovchton.add({'name': 'bat', 'rank': 1})
ovchton.add({'name': 'bat2', 'rank': 1})
ovchton.add({'name': 'bat3', 'rank': 2})








ovchton.add({'name': 'bat4', 'rank': 1})
ovchton.gettask()
