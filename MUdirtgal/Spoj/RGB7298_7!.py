# Анхны тоо 
from math import sqrt
n=int(input())
ans="YES"

for i in range(2,int(n) + 1):
    if n % i == 0:
        ans = "NO"
    break

if n == 1:
    print("NO")
else:
    print(ans)

# x=int(input())
# s=0
# for i in range(2,x):
#     if(x%i==0):
#         s=1
#         break
#     else:
#         s=0
# if(x==1 or x==0):
#     print("YES")
# elif(s==0):
#     print("YES")
# else:
#     print("NO") 