n = int(input())
m = 10
while n > 0:
    a = n % 10
    if a < m:
        m = a
    n = n//10
print(m)
