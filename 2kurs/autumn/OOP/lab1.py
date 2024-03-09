# # -----------------------------------------------------Task4
# temdegt = input()
# summ = 0
# for x in temdegt:
#     if x == 'a':
#         summ += 1
# print(summ)


# # -----------------------------------------------------Task3
# name = input('Enter name: ')
# password = input('Enter password: ')
# if name == 'admin' and password == 'mandakh':
#     print(f'Сайн байн уу? {name} тавтай морил')
# else:
#     print('Ner esvel password buruu bna')

# # ----------------------------------------------------Task2
# def hamgiinIh(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c
# def hamgiinIBaga(a, b, c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     elif c < a and c < b:
#         return c

# num1 = int(input('enter number : '))
# num2 = int(input('enter number : '))
# num3 = int(input('enter number : '))

# print(f'ih too: {hamgiinIh(num1, num2, num3)}')
# print(f'baga too: {hamgiinIBaga(num1, num2, num3)}')
# print(f'dundaj: {(num1+num2+num3)/3}')


# ---------------------------------------------Task1
try:
    too = int(input('too oruulna uu! '))

    print(type(too))
    if too == 1:
        print(f'Davaa garig')
    elif too == 2:
        print(f'Mygmar garig')
    elif too == 3:
        print(f'Lkhagva garig'
              )

    elif too == 4:
        print(f'Purev garig')
    elif too == 5:
        print(f'Baasan garig')
    elif too == 6:
        print(f'Byamba garig')
    elif too == 7:
        print(f'Nym garig')
    else:
        print(f'buruu too oruulsan bna!')
except ValueError:
    print('тооо оруулалдаа')
