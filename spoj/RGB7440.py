n = input()
a = ['A', 'B', 'C', 'D', 'E',
     'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
index = 0

for i in range(len(a)):
    if n.upper() == a[i]:
        index = i

for i in range(index, len(a)):
    for j in range(index, i+1):
        print(a[j], end='')
    print('')
