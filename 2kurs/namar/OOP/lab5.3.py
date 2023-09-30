class BankAcoount:

    def __init__(self, pin):
        self.__amount = 0
        self.__pin = pin

    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__amount += amount
            print(f'Таны дансанд {amount}т нэмэгдэж үлдэгдэл {self.__amount}т')
        else:
            print(f'Пин код буруу байна.')

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            self.__amount -= amount
            print(
                f'Таны данснаас {amount}т хасагдаж үлдэгдэл {self.__amount}т')
        else:
            print(f'Пин код буруу байна.')

    def get_balance(self, pin):
        if pin == self.__pin:
            return print(f'Таны дансны үлдэгдэл {self.__amount}')
        else:
            print(f'Пин код буруу байна.')


khan = BankAcoount('1122')
khan.deposit('1122', 11000)
khan.deposit('1122', 11000)
khan.withdraw('1122', 9000)
khan.get_balance('1122')
