#Массивын бага
from  sys import maxsize

a=[]
m= maxsize
n=int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]<m:
        m=a[i]
print(m)