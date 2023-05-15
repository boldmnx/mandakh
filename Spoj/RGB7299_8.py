



#Төгс тоо
n=int(input())

def checktugs(n):
    sum1 = 0
    for i in range(1, n//2+1, 1):
        if n % i == 0:
            sum1 += i
            # print(i)

    if sum1 == n:
        return "Yes"
    else:
        return "No"


for i in range(1, n, 1):
    if checktugs(i) == "Yes":
        print(i)







