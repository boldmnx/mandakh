b = []
n = int(input())
s = 0
for i in range(0, n, 1):
    b.append(int(input()))
    s += b[i]
print(s)
