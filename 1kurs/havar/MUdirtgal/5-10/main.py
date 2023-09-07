import math

# Anhnii too esehiig shalgah

# m=math.sqrt(int(input()))
# n=int(m)
# ans="YES"

# for i in range(2,n + 1, 1):
#     if int(n) % i == 0:
#         ans = "NO"
#     break

# if n == 1:
#     print("NO")
# else:
#     print(ans)

# garaas orson toonuudiin Tugs toog olov

n=int(input())

def checktugs(n):
    sum1 = 0
    for i in range(1, n//2+1, 1):
        if n % i == 0:
            sum1 += i
            # print(i)

    if sum1 == n:
        return True
    else:
        return False


for i in range(1, n, 1):
    if checktugs(i) == True:
        print(i)
