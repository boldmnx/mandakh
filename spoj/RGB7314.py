a, b = map(int, input().split())
s = a*b
while a != b:
    if a < b:
        b -= a
    else:
        a -= b

print(s//a)
