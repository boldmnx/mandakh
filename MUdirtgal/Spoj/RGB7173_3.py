# 	Цэгийн байрлал
x, y= map(int,input().split())
if x>0 and y>0:   
    print("I"  )
elif x<0 and y>0:
    print("II")
elif x<0 and y<0:
    print("III")
else: print("IV")