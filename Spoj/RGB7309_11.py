


# 11	Палиндром эсэх	
too = str(input())
con = True
tugsgul = len(too) - 1
for ehlel in range(0, len(too)):
    if(too[ehlel] != too[tugsgul]):
        con = False
    tugsgul -= 1
if(con):
    print("YES")
else:
    print("NO")



# from sys import maxsize; maxsize
# a =int(input()); 
# cnt=maxsize
# for i in range(0,a):
#     input(a[i])
# for j in range(0,a):
#     if(a[i]<cnt):
#         cnt=a[i]
# print(cnt)




