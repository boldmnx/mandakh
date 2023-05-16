#Массивын бага
from  sys import maxsize
m= maxsize
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]<m:
        m=a[i]
print(m)