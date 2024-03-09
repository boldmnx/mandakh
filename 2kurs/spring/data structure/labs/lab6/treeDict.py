

root = {
    'ysuhe': {
        'temujin': {
            'tului': {
                'hubilai': {},
                'munkh': {}
            },
            'zuchi': {},
            'tsagaadai': {},
            'ugudei': {}
        },
        'temuge': {},
        'basar': {},
        'hasar': {}
    }
}


def read(e, zai=0):

    for key, value in e.items():
        if zai == 0:
            print(f'{key}')
        else:
            print(f'{"  "*zai} |-- {key}')

        if type(value) is dict:
            read(value, zai+1)


read(root)
