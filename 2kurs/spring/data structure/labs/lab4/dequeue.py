class Deq:
    def __init__(self):
        self.__dequ = []

    def empty(self):
        if self.__dequ == []:
            return True
        return False

    def fadd(self, a={}):
        self.__dequ = [a]+self.__dequ
        return [a]

    def ladd(self, a):
        self.__dequ = self.__dequ+[a]
        return [a]

    def ldel(self):
        if self.empty():
            return 'hooson bn'
        else:
            s = self.__dequ[-1]
            self.__dequ = self.__dequ[:-1]
            return s

    def fdel(self):
        if self.empty():
            return 'hooson bn'
        else:
            s = self.__dequ[0]
            self.__dequ = self.__dequ[1:]
            return s

    def len(self):
        if self.empty():
            return 'hooson bn'
        else:
            s = 0
        for i in self.__dequ:
            s += 1
        return s

    def look(self):
        return self.__dequ

    def first(self):
        if self.empty():
            return 'hooson bn'
        else:
            return self.__dequ[0]

    def last(self):
        if self.empty():
            return 'hooson bn'
        else:
            return self.__dequ[-1]
