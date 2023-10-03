x, y, z = map(int, input().split())
s = 1
if x % 2 != 0:
    s *= x
if y % 2 != 0:
    s *= y
if z % 2 != 0:
    s *= z

print(s)
