n, m, k = map(int, input().split())
nm = ''
for i in range(n, m+1):
    nm += str(i)
nm = ''.join(sorted(nm, reverse=True))

if len(nm) > k:
    print(int(nm[k-1]))
else:
    print(-1)
