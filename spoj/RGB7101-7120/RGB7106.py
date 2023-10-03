x, y, z, w = map(int, input().split())
urj = 1
if x < 5:
    urj *= x
if y < 5:
    urj *= y
if z < 5:
    urj *= z
if w < 5:
    urj *= w
print(urj)
