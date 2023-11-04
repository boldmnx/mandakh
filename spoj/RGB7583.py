n = int(input())
m = []
m.append(n)
while True:
    descending = int(''.join(sorted(str(n), reverse=True)))
    ascending = int(''.join(sorted(str(n))))
    n = descending-ascending
    if n in m:
        break
    m.append(n)

print(len(m))
