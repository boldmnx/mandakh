class BankAcoount:

    def __init__(self, pin):
        self.amount = 0
        self.pin = pin

    def deposit(self, pin, amount):
        if pin == self.pin:
            self.amount += amount
            print(f'Таны дансанд {amount}т нэмэгдэж үлдэгдэл {self.amount}т')
        else:
            print(f'Пин код буруу байна.')

    def withdraw(self, pin, amount):
        if pin == self.pin:
            self.amount -= amount
            print(f'Таны данснаас {amount}т хасагдаж үлдэгдэл {self.amount}т')
        else:
            print(f'Пин код буруу байна.')

    def get_balance(self, pin):
        if pin == self.pin:
            return print(f'Таны дансны үлдэгдэл {self.amount}')
        else:
            print(f'Пин код буруу байна.')