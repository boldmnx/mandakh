n = int(input())
multi = 1
for i in range(1, n+1):
    multi *= 1+1/pow(i, 2)
print(f'{multi:.3f}')
