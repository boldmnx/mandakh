n = int(input())
multi = 1
for i in range(1, n+1):
    multi *= i
    print(f'{i}!={multi}')
