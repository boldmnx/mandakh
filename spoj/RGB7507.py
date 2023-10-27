b = int(input())
m = list(map(int, input().split()))
ih = m[0]
index = 0
for i in range(1, b):
    if ih < m[i]:
        ih = m[i]

for i in range(b):
    if ih == m[i]:
        index = i+1
        break

print(ih, index)
