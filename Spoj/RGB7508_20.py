#Массивын их хэд
import sys

a = []
n = int(input())
cnt=0
for i in range(n):
    # a.append(int(input()))
    a=list(map(int,input().split()))
 
m = -sys.maxsize
for i in range(n):
    if a[i] > m:
        m = a[i]
        cnt=1
    elif a[i]==m:
        cnt+=1
print(f'{m} {cnt}')
