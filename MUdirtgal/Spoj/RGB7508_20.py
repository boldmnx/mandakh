#Массивын их хэд
from sys import maxsize
n = int(input())
a =list(map(int,input().split()))
cnt=0
m = -maxsize
 
for i in range(n):
    if a[i] > m:
        m = a[i]
        cnt=1
    elif a[i]==m:
        cnt+=1
print(f'{m} {cnt}')