n = int(input())
m = list(map(int, input().split()))
ih = m[0]

for i in range(n):
    if ih < m[i]:
        ih = m[i]
print(ih)
