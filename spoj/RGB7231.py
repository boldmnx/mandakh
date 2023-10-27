import math
x, n = map(float, input().split())
s = 0
for i in range(1, int(n)+1):
    s += pow(math.sin(x), i)

print(f'{s:.3f}')
