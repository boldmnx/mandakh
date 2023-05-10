# 1 upper and lower
# print("K".lower())

# # 2
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

a,b,c,d=map(int,input().split())
s=a
if(s>b):
    s=b
if(s>c):
    s=c
if(s>d):
    s=d
print(s)

# if (a < b):
#     if (a < c):
#         if (a < d):
#             print(a)
#         else:
#             print(d)
#     else:
#           if(c<d):
#                  print(c)