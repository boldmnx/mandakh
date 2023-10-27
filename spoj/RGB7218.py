a, n = map(int, input().split())
s = 1
for i in range(1, n+1):
    s += pow(a, i)
print(s)
