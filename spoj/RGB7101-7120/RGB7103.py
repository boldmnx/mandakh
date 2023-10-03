x, y, z = map(int, input().split())
m = x
if m < y:
    m = y
if m < z:
    m = z
print(m)
