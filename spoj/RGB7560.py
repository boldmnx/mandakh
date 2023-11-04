n = int(input())
m = list(map(float, input().split()))
res = m[0]
resBaga = m[0]
indexIh = 0
indexBaga = 0

for i in range(n):
    if res < m[i]:
        res = m[i]
        indexIh = i
    elif resBaga > m[i]:
        resBaga = m[i]
        indexBaga = i

m[indexBaga] = res
m[indexIh] = resBaga
# format_m = [f"{i:.2f}" for i in m]
# format_int = [float(i) for i in m]


print(m)
