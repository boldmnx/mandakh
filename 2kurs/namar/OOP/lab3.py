

# task10
# a = 'mandakh university'
# c = 0
# for i in a:
#     if (i == 'i'):
#         c += 1
# print(c)


# # task9
# name = 'bat|bold|suren'
# names = ''
# for i in name:
#     if i != '|':
#         names += i
#     else:
#         print(names)
#         names = ''
# print(names)

# # task8
# carPrice = ['$2500', '$35500', '$17500', '$4000']
# carTug = []
# for i in range(len(carPrice)):
#     carTug.append(int(carPrice[i][1:])*3300)
# print(carTug)

# task7
# rD = input('Регистрээ оруулна уу!: ')
# fName = input('Овог нэрээ оруулна уу!: ')


# def task7(rD, fName):
#     ognoo = f'19{rD[2: -6]}-{rD[4: -4]}-{rD[6:-2]}'

#     index = 0
#     for i in range(len(fName)):
#         if fName[i] == ' ':
#             index = i
#     ovogNer = f'{fName[0]}.{fName[index:]}'
#     fullOvogNer = f'{fName[:index]} овогтой {fName[index:]}'
#     return ognoo, ovogNer, fullOvogNer


# res = task7(rD, fName)
# print(res)


# task6 MS sum
def ms_sum(**args):
    summ = 1
    for value in args.values():
        summ *= value
    print(summ)

# # task5

# a = input('Ymar neg yum bich nuu:  ')
# if a[0:] == a[::-1]:
#     print(f'{a}: палиндром мөн')
# else:
#     print(f'{a}: палиндром биш')


# # # task4
def dict_function(arg):
    dictionary = {
        'bad': 'муу',
        'good': 'сайн',
        'red': 'улаан',
        'This is computer': 'Энэ бол компьютер'
    }
    for key, value in dictionary.items():
        if arg == key:
            print(f'{key} --- {value}')
        elif arg == value:
            print(f'{value} --- {key}')


# # task3
# u = 'abcdefkjyhtgnbgrspoikjabcdefkjyhtgnbgrspoikjabcdefkjyhtgnbgrspoikjabcdefkjyhtgnbgrspoikjgkdljfhgkdfhgkld'
# def tooloh(u):
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     for i in u:
#         if i == 'a':
#             a += 1
#         if i == 'b':
#             b += 1
#         if i == 'c':
#             c += 1
#         if i == 'd':
#             d += 1
#         if i == 'e':
#             e += 1
#     return a, b, c, d, e


# res = tooloh(u)
# print(f'a: {res[0]}\nb: {res[1]}\nc: {res[2]}\nd: {res[3]}\ne: {res[4]}')

# task2


# a = 'hello world'
# s = 0
# for i in a:
#     s += 1
# print(f'Урт: {s}')


# # task1
# try:
#     a = int(input('1dehi toog oruulna uu! '))
#     b = int(input('2dahi toog oruulna uu! '))
#     c = int(input('3dahi toog oruulna uu! '))

#     def litMid(a, b, c):
#         lit = a
#         if b < a and b < c:
#             lit = b
#         if c < b and c < a:
#             lit = c
#         lot = a
#         if b > a and b > c:
#             lot = b
#         if c > b and c > a:
#             lot = c
#         mid = (a+b+c)/3
#         return lit, mid, lot

#     res = litMid(a, b, c)
#     print(f'Бага тоо: {res[0]} \nДундаж тоо: {res[1]} \nИх тоо: {res[2]}')
# except ValueError:
#     print('Зөвхөн тоо оруулна уу!')

# dict_function(input('search: '))
ms_sum(b=3, c=3)
