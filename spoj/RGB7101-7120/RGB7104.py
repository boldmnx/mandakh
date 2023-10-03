x, y, z, w = map(int, input().split())
m = x
if m > y:
    m = y
if m > z:
    m = z
if m > w:
    m = w
print(m)
