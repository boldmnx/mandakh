

def bubble_sort(value):
    ascii = [ord(char) for char in value.lower()]

    for i in range(len(ascii)):
        for j in range(len(ascii)-1):
            if ascii[j] > ascii[j+1]:
                ascii[j], ascii[j+1] = ascii[j+1], ascii[j]
    asciiList = [chr(i) for i in ascii]
    asciiStr = ''.join(asciiList)

    return asciiStr


ner = {'ner': ['cent', 'bat', 'anugo']}
# ner = 'bat'
# print(bubble_sort(ner))


def ner_sort(value):
    for i in range(len(value)):
        for j in range(len(value['ner'])-1):
            if ord(value['ner'][j][j]) > ord(value['ner'][j+1][j]):
                a = value['ner'][j]
                value['ner'][j], value['ner'][j + 1] = value['ner'][j+1], a
    return value


print('base: ', ner['ner'])
print('change: ', ner_sort(ner)['ner'])
