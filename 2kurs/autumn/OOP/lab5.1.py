class Oyutan:
    __dunguud = []
    __hicheeluud = []

    def __init__(self, ner, kod):
        self.__ner = ner
        self.__kod = kod

    def sudalsan_hicheel(self, hicheel, dun):
        self.__dunguud.append(dun)
        self.__hicheeluud.append(hicheel)

    def dunguud_hevleh(self):
        i = 0
        while (i < len(self.__dunguud)):
            print(f"{self.__hicheeluud[i]}-{self.__dunguud[i]}")
            i += 1

    def golch(self):
        return sum(self.__dunguud)/len(self.__dunguud)


if __name__ == '__main__':
    o = Oyutan('Zorigoo', 'SW19D001')
    print(o.__kod)

    # o.sudalsan_hicheel('Монгол хэл', 80)
    # o.sudalsan_hicheel('Компьютерийн хэрэглээ', 100)
    # o.dunguud_hevleh()
    # print(o.golch())  # 90
