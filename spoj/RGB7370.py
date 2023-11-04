k = int(input())
n = int(input())
sondgoi = 0
tegsh = 0

while n > 0:
    last_number = n % 10
    if last_number % 2 != 0:
        sondgoi += last_number
    else:
        tegsh += last_number
    n = n//10
res = sondgoi-tegsh
if res % k == 0:
    print('YES')
else:
    print('NO')
