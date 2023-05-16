#Тоон дахь их цифр
x = int(input())
s = 0
while (x > 0):
    a = x % 10
    x = x//10
    if (a > s):
        s = s+a-s
    if (a < s):
        x = x//10
print(s)
