class Restaurant:
    __unenuud = []
    __hoolnuud = []

    def __init__(self, pin):
        self.pin = pin

    def hool_zahialah(self, une, hool):
        self.__unenuud.append(une)
        self.__hoolnuud.append(hool)

    def tootsoo(self):
        i = 0
        su = 0
        if len(self.__hoolnuud) != 0:
            print('Таны тооцоо: ')
            while i < len(self.__hoolnuud):
                print(f'{i + 1}: {self.__hoolnuud[i]}-{self.__unenuud[i]}')
                su += self.__unenuud[i]
                i += 1
            print(f'нийт: {su}')
        else:
            print('Таньд тооцоо байхгүй байна')


res = Restaurant(123)
while True:
    try:
        ePin = int(input("ПИН кодоо оруулна уу: "))
        if ePin == res.pin:
            print("Амжилттай нэвтэрлээ.")
            while True:
                print("Сонголтыг сонгоно уу:")
                print("1. Хоол захиалах")
                print("2. Тооцоо хийх")
                print("3. Гарах")
                choice = input("Сонголтоо оруулна уу (1/2/3/4): ")

                if choice == '1':
                    bUne = 0
                    tsUne = 0
                    hUne = 0
                    while True:
                        print("Сонголтыг сонгоно уу:")
                        print('1. Бууз---500₮')
                        print('2. Цуйван---5000₮')
                        print('3. Хуушуур---1000₮')
                        print("4. Гарах")
                        zahialga = input("Сонголтоо оруулна уу (1/2/3/4): ")
                        if zahialga == '1':
                            shirheg = int(input('Хэдэн ширхэгийг авах юэ?: '))
                            bUne += 500*shirheg
                            hool = 'Бууз'
                            res.hool_zahialah(bUne, hool)
                            # print("Сонголтыг сонгоно уу:")
                            # print('1. Дахин захиалах')
                            # print('2. Гарах')
                            # again = input('Сонголтоо оруулна уу (1/2): ')
                            # if again!='1':1
                            #     True
                        elif zahialga == '2':
                            shirheg = int(input('Хэдэн ширхэгийг авах юэ?: '))
                            tsUne += 5000*shirheg
                            hool = 'Цуйван'
                            res.hool_zahialah(tsUne, hool)
                        elif zahialga == '3':
                            shirheg = int(input('Хэдэн ширхэгийг авах юэ?: '))

                            hUne = 1000*shirheg
                            hool = 'Хуушуур'
                            res.hool_zahialah(hUne, hool)
                        elif zahialga == '4':
                            break
                elif choice == '2':
                    res.tootsoo()
                    break
                elif choice == '3':
                    print("Та аппаас гарлаа.")
                    break
            break
        else:
            print(f'pin code buruu bna')
    except ValueError:
        print('too orrulna uu')
