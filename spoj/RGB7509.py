
n = int(input())
m = list(map(int, input().split()))
s = int(input())
res = 'NO'
for i in range(n):
    if m[i] == s:
        res = 'YES'
print(res)
