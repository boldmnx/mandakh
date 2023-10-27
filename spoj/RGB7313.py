
a, b = map(int, input().split())

while a != b:
    if a < b:
        b -= a
    else:
        a -= b

print(a)
