from queque import Queque


class Hospital:
    def __init__(self):
        self.__oochir = Queque()

    def first(self):
        return self.__oochir.first()

    def add_patient(self, tasalbar):
        self.__oochir.add(tasalbar)

    def remove_patient(self):
        return self.__oochir.delete()

    def len(self):
        self.__oochir.len()

    def is_empty(self):
        return self.__oochir.is_empty()

    def display(self):
        return self.__oochir.display()


hos = Hospital()
hos.add_patient('uvchtun1')
hos.add_patient('uvchtun2')
hos.display()
hos.add_patient('uvchtun3')
hos.display()

hos.remove_patient()
hos.display()
