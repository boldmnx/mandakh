# Факториалуудын нийлбэр
n=int(input())
sum=0
m=1
for i in range(1,n+1):
    m*=i
    sum+=m
print(sum)