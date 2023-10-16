a = int(input())
x = 1
i = 1
while (x < a):
    i += 1
    x *= i
if x == a:
    print(i)
else:
    print('No')
