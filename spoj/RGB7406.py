n = int(input())
s = 0

for i in range(1, n+1):
    multi = 1
    for j in range(i, i*2+1):
        multi *= j
    s += multi
print(s)
