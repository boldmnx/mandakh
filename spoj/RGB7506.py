b = int(input())
m = list(map(int, input().split()))
s = int(input())
c = 0

for i in range(b):
    if s == m[i]:
        c += 1
print(s, c)
