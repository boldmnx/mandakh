n = int(input())
m = []
s = 0
t = 0
for i in range(n):
    m.append(int(input()))
    if m[i] % 2 != 0:
        s += 1
    else:
        t += 1
if s > t:
    print('YES')
else:
    print('NO')
