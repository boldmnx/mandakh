# Тооны факториал
n = int(input())
i, s = 1, 1
while s < n:
    i += 1
    s *= i
if s == n:
    print(i)
else:
    print("No")
