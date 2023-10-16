a = int(input())
x = 0
while a % 2 == 0:
    a //= 2
if a == 1:
    print('YES')
else:
    print("NO")
