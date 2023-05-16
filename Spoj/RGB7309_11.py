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