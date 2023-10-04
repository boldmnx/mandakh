x, y = map(int, input().split())
z = int(input())
if z % y != 0:
    print(z//y, y)
else:
    print(z//y+1, z % y)
