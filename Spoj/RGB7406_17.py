#Илэрхийлэл 1
x = int(input())
t=0
for i in range(1,x+1):
    s=1
    for j in range(i,i*2+1):
        s=s*j
    t=t+s
print(t) 