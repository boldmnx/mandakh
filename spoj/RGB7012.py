import math
x = int(input())
minut = x/60
tsag = minut/60
print(f'{math.floor(tsag)} {math.floor(minut%60)} {x % 60}')
