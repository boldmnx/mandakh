a, n = map(int, input().split())
zereg = 1
for i in range(1, n+1):
    zereg *= a
print(zereg)
