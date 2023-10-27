n = int(input())
m = []
c = 0
for i in range(n):
    m.append(int(input()))
    if m[i] < 60:
        c += 1
print(c)
