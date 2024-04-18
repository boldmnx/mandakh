class Map:
    def __init__(self):
        self.dic = {}

    def __setitem__(self, k, v):
        self.dic[k] = v

    # region delete

    def __delitem__(self, e):
        del self.dic[e]

    def __pop__(self, e, d=None):
        for i in self.dic:
            if i == e:
                return self.dic.pop(e)
        return d
    # endregion

    def __len__(self):
        count = 0
        for i in self.dic:
            count += 1
        return count

    # region print

    def __getitem__(self, k):
        return self.dic[k] if k in self.dic else 'Key error'

    def __get__(self, e, d=None):
        for i, a in self.dic.items():
            if e == i:
                return print(a)
        return print(d)

    def __items__(self):
        print(self.dic.items)

    def __keys__(self):
        for i in self.dic:
            print(i, end=' ')

    def __values__(self):
        for i in self.dic.values():
            print(i, end=' ')

    # endregion

    def find_lt(self, k):
        lessThanK = []
        c = 0
        for ke in self.dic.keys():
            if k > int((ke)):
                lessThanK.append(ke)

        return print(f'''{k}- н утгаас бага бас хамгийн их утгатай түлхүүр нь: {max(lessThanK) if lessThanK else 'бага утга алга'}''')

    def find_min(self, m):
        return print(f"min key:{min(m.keys())}, min value:{min(m.values())}")

    def __setdefault__(self, e, d):
        for k, v in self.dic.items():
            if k == e:
                return v
        self.dic[e] = d
        return self.dic[e]

    def __contains__(self, e):
        for i in self.dic:
            if i == e:
                return True
        return False

    def find_le(self, k):
        newArray = []
        for ke in self.dic.keys():
            if k >= int(ke):
                newArray.append(ke)

        return print(f'{k}-аас бага буюу тэнцүү хамгийн их түлхүүр: {max(newArray)}, түүний утга: {self.dic[max(newArray)]}  ')

    def find_gt(self, k):
        newArray = []
        for ke in self.dic.keys():
            if k < int(ke):
                newArray.append(ke)

        return print(f'{k}-аас их хамгийн бага түлхүүр: {min(newArray)}, түүний утга: {self.dic[min(newArray)]}  ')

    def find_ge(self, k):
        newArray = []
        for ke in self.dic.keys():
            if k <= int(ke):
                newArray.append(ke)

        return print(f'{k}-аас их болон тэнцүү хамгийн бага түлхүүр: {min(newArray)}, түүний утга: {self.dic[min(newArray)]}  ')

    def sorted_m(self):
        newDic = {}
        for i in sorted(map(int, self.dic.keys())):
            newDic[i] = self.dic[str(i)]
        return print(newDic)


maps = Map()
# maps.__setitem__('k', 2)
# maps.__setitem__('b', 4)
# maps.__setitem__('u', 2)
# maps.__setitem__('v', 8)
# maps.__setitem__('k', 9)
maps.__setitem__('10', 'hurga')
maps.__setitem__('30', 'yamaa')
maps.__setitem__('1', 'honi')
maps.__setitem__('50', 'temee')
maps.__setitem__('20', 'mori')
maps.__setitem__('5', 'hs')
maps.__setitem__('6', 'hs')
maps.__setitem__('19', 'hs')
# maps.find_le(10)
# maps.find_gt(2)
# maps.find_ge(2)
maps.sorted_m()
