friends = ['bat', 'dulam', 'badam', 'bold', 'anu', 'dorj', 'dondog']
zochid = ['bat', 'dulam', 'badam']
vehicle = ['lexus 570', 'lexus 470', 'land 300',
           'land 200', 'prius 30', 'prius 20', 'aqua']

travels = ['Швицар', 'Тэнгэрийн хаалга', 'Африк', 'Токио', 'Колумб']
# pop with index, remove with utgaar


def t1(args):
    for friend in args:
        print(friend)


def t2(args):
    print(f'Сайн байн уу {args[0]} найзаа')


def t3(args):
    print(f"Би {args[0].title()}-тай болмоор байна")


def t4(args):
    for i in args:
        print(f'Эрхэм хүндэт {i} таныг оройн зоогонд урьж байна.')


def t5(args):
    for i in args:
        print(f'Эрхэм хүндэт {i} таныг оройн зоогонд урьж байна.')
    print(f'''{args.pop(
        1)} нь хүндэтгэх шалтгааны улмаас ирж чадхааргүй болж түүний оронд Бааска ирхээр боллоо.''')
    args.insert(1, "Бааска")
    for i in args:
        print(f'Эрхэм хүндэт {i} таныг оройн зоогонд урьж байна.')


def t6(args):
    print(f'{args} нартаа хэлэхэд илүү том ширээ олсон тул нэмэлт 3 зочин урих боломжтой боллоо. Зочдын тоо {len(args)}')
    args.insert(0, 'Даавка')
    args.insert(2, 'Баян')
    args.append('Орчлон')
    for i in args:
        print(f'Эрхэм хүндэт {i} таныг оройн зоогонд урьж байна.')
    print(f'Зочдын тоо {len(args)}')


def t7(args):
    print(f'Заа сорри манай саяны ширээ цуцлагдсан тул зөвхөн 2 хүний ширээ захиалхаар боллоо.')
    if len(args) > 1:
        print(
            f'\033[1m{args.pop()}\033[0m таныг оройн хоолонд урих боломжгүй боллоо хамарсалтай байна.')
    for i in args:
        print(f'{i} та оройн хоолонд уригдсан хэвээр байна')

    c = len(args)
    while c > 0:
        del args[c-1]
        c -= 1
    print(args)


# Бүр эрэмблэх бол sort, түр эрэмблэх бол sorted, reverse
def t8(args):
    print(f'original: {args}')
    print(f'sorted: {sorted(args)}')
    print(f'original: {args}')
    print(f'sorted reverse: {sorted(args, reverse=True)}')
    print(f'original: {args}')
    args.reverse()
    print(f'reverse: {args}')
    args.reverse()
    print(f'again reverse: {args}')
    args.sort()
    print(f'sort: {args}')
    args.sort(reverse=True)
    print(f'sort reverse: {args}')
    print(f'original: {args}')


def t9(args):
    print(f'Оройн хоолны зочидын тоо: {len(args)}')


def t10(args):
    pass


def t11(args):
    # len shalgah esvel -1
    print(args[100])
