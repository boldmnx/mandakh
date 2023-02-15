n = int(input())
b = list(map(int, input().split()))
maxx = b[0]

for i in range(1, n, 1):
    if (maxx < b[i]):
        maxx = b[i]
print(maxx)
