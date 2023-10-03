x, y, z = map(int, input().split())
# hamgiin ih tooni kvadrattai nugu 2toniikvdratin nilber tentsu bval zob esvel 3ula ijil
if x == y and x == z:
    print('YES')
elif pow(x, 2)+pow(y, 2) == pow(z, 2):
    print('YES')
elif pow(y, 2)+pow(z, 2) == pow(x, 2):
    print('YES')
elif pow(z, 2)+pow(x, 2) == pow(y, 2):
    print('YES')
else:
    print('NO')
