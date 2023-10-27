x, y, z, w = map(int, input().split())
count = 0
if x % 3 == 0:
    count += 1
if y % 3 == 0:
    count += 1
if z % 3 == 0:
    count += 1
if w % 3 == 0:
    count += 1
print(count)
