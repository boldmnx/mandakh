x = int(input())
r = 0
y = 0
y = y+x
while x > 0:
    r = r*10
    s = x % 10
    r = r+s
    x = x//10
if r == y:
    print('YES')
else:
    print("NO")


# a = input()

# if len(a) % 2 == 0:
#     print('NO')
# else:
#     b = len(a)//2
#     b += 1
#     if a[b:] == a[b:]:
#         print('YES')
