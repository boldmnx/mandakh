class Queque:
    # Queque is FIFO
    def __init__(self):
        self.__oochir = []

    def first(self):
        return print(self.__oochir[0])

    def add(self, tasalbar):
        self.__oochir += [tasalbar]

    def delete(self):
        if self.__oochir:
            tasalbar = self.__oochir[0]
            self.__oochir = self.__oochir[1:]
            return tasalbar
        return 'error'

    def len(self):
        count = 0
        for i in self.__oochir:
            count += 1
        return count

    def is_empty(self):
        return self.len() == 0

    def display(self):
        return print(self.__oochir)


# hospital = Queque()

# hospital.add(5)
# hospital.display()

# hospital.add(3)
# hospital.display()
# print(hospital.len())
# print(hospital.delete())
# print(hospital.is_empty())
# print(hospital.delete())
# print(hospital.is_empty())
# print(hospital.delete())
# hospital.add(7)
# hospital.display()
# hospital.add(9)
# hospital.display()
# hospital.first()
# hospital.add(4)
# hospital.display()
# print(hospital.len())
# # print(hospital.add())


# hospital.add(1)
# hospital.add(4)
# hospital.add(10)


# hospital.display()
# print(hospital.len())

# hospital.delete()
# hospital.display()

# print(hospital.len())
# print(hospital.is_empty())
