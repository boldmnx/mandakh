# Гурван тооны ХБЕХ
a, b, e = map(int, input().split())
s = a*b
while (a != b):
    if (a > b):
        a -= b
    else:
        b -= a
d = s//a
f = d*e
while (d != e):
    if (d > e):
        d -= e
    else:
        e -= d
print(f//d)
