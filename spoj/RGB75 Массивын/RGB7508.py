n = int(input())
m = list(map(int, input().split()))
ih = m[0]
c = 1
for i in range(1, n):
    if ih < m[i]:
        ih = m[i]
        c = 0
    if ih == m[i]:
        c += 1

print(ih, c)
