class Stack:
    def __init__(self):
        self.__list1 = []

    def push(self, e):
        self.__list1 += [e]

    def pop(self):
        if self.is_empty():
            return 'hooson bna'
        self.__list1 = self.__list1[:-1]

    def top(self):
        if self.lenn() != 0:
            return self.__list1[-1]
        return 'hooson bna'

    def bottom(self):
        if self.lenn() != 0:
            return self.__list1[0]
        return 'hooson bna'

    def lenn(self):
        count = 0
        for i in self.__list1:
            count += 1
        return count

    def is_empty(self):
        if self.lenn() == 0:
            return True
        return False

    def getItems(self):
        return self.__list1
