n = int(input())
c = 1
resul = 0

while result > 6174:
    descending = int(''.join(sorted(str(number_str), reverse=True)))
    ascending = int(''.join(sorted(str(number_str))))
    result = descending-ascending
    c += 1
print(c)
