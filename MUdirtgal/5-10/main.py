import math


n = int(input())
# b = int(n)

# print(b)
# for i in range(0, b + 1, 1):
#     if b % i == 0:
#         ans = "NO"
#     break

# if b == 1:
#     print("NO")
# else:
#     print(ans)


def checktugs(n):
    count = 0
    sum1 = 0
    for i in range(1, n/2+1, 1):
        if n % i == 0:
            sum1 += i
            # print(i)

    if sum1 == n:
        return True
    else:
        return False


for i in range(1, 1000, 1):
    if checktugs(i) == True:
        print(i)
