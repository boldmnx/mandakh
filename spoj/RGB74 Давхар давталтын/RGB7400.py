
n = int(input())
s = 0
for i in range(1, n+1):
    s *= 10
    s += i
    for j in range(1, n+1):
        print(j, end='')
    print('')
