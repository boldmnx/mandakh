x = int(input())
r = 0
while (x > 0):
    r = r*10
    s = x % 10
    r = r+s
    x = x//10
print(r)
