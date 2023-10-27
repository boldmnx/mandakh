n = int(input())
m = 1
for i in range(1, n+1):
    if n % 2 == 0:
        if i % 2 == 0:
            m *= i
    else:
        if i % 2 != 0:
            m *= i
print(m)
