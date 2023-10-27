n = int(input())
m = list(map(int, input().split()))
baga = m[0]
for i in range(n):
    if m[i] < baga:
        baga = m[i]
print(baga)
