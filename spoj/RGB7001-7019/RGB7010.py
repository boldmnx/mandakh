import math
x = int(input())
y = x % 10
z = math.floor(x / 10) % 10
w = math.floor(x / 100)
print(y+w+z)
