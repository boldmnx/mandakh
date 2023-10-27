x, y, z, w = map(int, input().split())
s = 0
if x % 11 != 0:
    s += x
if z % 11 != 0:
    s += z
if y % 11 != 0:
    s += y
if w % 11 != 0:
    s += w
print(s)
