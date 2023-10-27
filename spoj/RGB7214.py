n = int(input())
s = n
for i in range(2, n+1):
    s += i*(n-(i-1))
print(s)
