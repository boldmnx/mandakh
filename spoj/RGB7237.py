n = int(input())
oroltuud = list(map(float, input().split()))
s = 0
av = s/n

for i in range(n):
    s += oroltuud[i]

print(f'{av:.2f}')
