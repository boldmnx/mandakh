n = int(input())
c = 0
while n > 0:
    a = n % 10
    if a % 2 != 0:
        c += 1
    n = n//10
print(c)
