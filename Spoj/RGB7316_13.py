# Гурван тооны ХБЕХ
def gcd(a, b):
    if a == 0:
        return b
    else:
        gcd(b % a, a)


def lcm(a, b):
    return a / int(gcd(a, b)*b)


a = int(input())
b = int(input())
c = int(input())
print(lcm(a, lcm(b, c)))
