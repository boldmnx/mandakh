from math import sin

b, n = map(float, input().split())
s = 0
for i in range(1, int(n)+1):
    s += sin(pow(b, i))
print(f'{s:.3f}')
