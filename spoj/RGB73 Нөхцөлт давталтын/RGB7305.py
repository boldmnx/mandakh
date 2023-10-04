x, y = map(int, input().split())
c = 0
while x > 0:
    a = x % 10
    if a == y:
        c += 1
    x = x//10
print(c)
