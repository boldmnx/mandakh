# Массив тэгээс их нийлбэр 
a=[]
s=0
n=int(input())
for i in  range(n):
    a.append(int(input()))
for i in range(n):
    if a[i]>0:
        s+=a[i]
print(s)