n = int(input())
s = 0
multi = 1

for i in range(1, n+1):
    multi *= i
    s += multi
print(s)
