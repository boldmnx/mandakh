x, y, z, w = map(int, input().split())
s = 0
if 80 < x:
    s += x
if 80 < y:
    s += y
if 80 < z:
    s += z
if 80 < w:
    s += w
print(s)
