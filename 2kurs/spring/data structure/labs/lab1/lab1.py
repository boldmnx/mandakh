

def maxx(*a):
    m = a[0][0]
    for i in a[0]:
        if m < i:
            m = i
    return m


def avg(*a):
    sum = 0
    for i in a[0]:
        sum += i
    return sum//len(a[0])


def minn(*a):
    m = a[0][0]
    for i in a[0]:
        if m > i:
            m = i
    return m


def weekend_method(weekend):
    if weekend == 1:
        print('Monday')
    elif weekend == 2:
        print('Tuesday')
    elif weekend == 3:
        print('Wednesday')
    elif weekend == 4:
        print('thursday')
    elif weekend == 5:
        print('Friday')
    elif weekend == 6:
        print('Saturday')
    elif weekend == 7:
        print('Sunday')
    else:
        print('1-7 hoorond too oruulna uu')


# Daalgavar 1

# w = int(input())
# weekend_method(w)

# Daalgavar 2

# n = list(map(int, input().split()))

# print(f'max: {maxx(n)}')
# print(f'avg: {avg(n)}')
# print(f'min: {minn(n)}')

# Daalgavar 3


class Phone:
    def __init__(self, ner):
        self.ner = ner

    def __str__(self):
        print(f'Tuunii ner: {self.ner}')


class Homephone(Phone):
    def __init__(self, ner, cable):
        Phone.__init__(self, ner)
        self.cable = cable

    def __str__(self):
        print(f'Каблын төрөл: {self.cable}')


class Cellphone(Phone):
    def __init__(self, ner, touch=False):
        Phone.__init__(self, ner)
        self.touch = touch

    def __str__(self):
        print(f'Утасны нэр: {self.touch}')


iphone = Cellphone('iphone 11', True)
landline = Homephone('landline', 'RJ-11')
iphone.__str__()
landline.__str__()
