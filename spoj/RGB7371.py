n = int(input())
len_n = len(str(n))
m = n
s = 0
for i in range(len_n):
    last_number = n % 10
    s += pow(last_number, len_n)
    n = n//10
if s == m:
    print('YES')
else:
    print('NO')
