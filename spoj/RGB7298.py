n = int(input())
res = 'YES'


for i in range(2, n):
    if n % i == 0:
        res = "NO"
        break


print(res)
