
n = int(input())
s = str(n)
digits = [int(digit) for digit in s]  # str to list
digits.sort(reverse=True)
res = int(''.join(map(str, digits)))  # list to int

print(res)
