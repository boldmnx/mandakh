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
        print(self.dic)

    def __keys__(self):
        for i in self.dic:
            print(i, end=' ')

    def __values__(self):
        for i in self.dic.values():
            print(i, end=' ')

    # endregion

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


map = Map()
map.__setitem__('k', 2)
map.__setitem__('b', 4)
map.__setitem__('u', 2)
map.__setitem__('v', 8)
map.__setitem__('k', 9)



print(map.__getitem__('b'))
print(map.__getitem__('x'))
map.__get__('f')
map.__get__('f',5)
map.__get__('k',5)
print(map.__len__())
map.__delitem__('v')
print(map.__pop__('k'))
map.__keys__()
map.__values__()
map.__items__()
print(map.__setdefault__("b", 1))
print(map.__setdefault__("a", 1))

# print(map.__contains__('b'))
