# 1 upper and lower
# print("K".lower())
# 2
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a < b):
    if (a < c):
        if (a < d):
            print(a)
        else:
            print(d)
    else:
        print(c)
else:
    if (b < c):
        if (b < d):
            print(b)
        else:
            print(d)
    else:
        print(c)
print(b)
