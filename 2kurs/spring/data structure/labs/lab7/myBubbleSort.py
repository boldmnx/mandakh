from faker import Faker


ners = ['az', 'ab',  'baw', 'bat','Jat', 'Bold', 'dondog', 'anugo', 'Aanaa']


def swap(args):
    c = 0
    count = 0
    isTrue = True
    while isTrue:
        isTrue = False
        for i in range(len(args)-count-1):
            if ord(args[i][i-c].lower()) > ord(args[i+1][i-c].lower()):
                args[i], args[i+1] = args[i+1], args[i]
                isTrue = True
            elif ord(args[i][i-c].lower()) is ord(args[i+1][i-c].lower()):

                if ord(args[i][i-c+1].lower()) > ord(args[i+1][i-c+1].lower()):
                    args[i], args[i+1] = args[i+1], args[i]
                    isTrue = True
                elif ord(args[i][i-c+1].lower()) is ord(args[i+1][i-c+1].lower()):
                    if ord(args[i][i-c+2].lower()) > ord(args[i+1][i-c+2].lower()):
                        args[i], args[i+1] = args[i+1], args[i]
                        isTrue = True

            c += 1
        c = 0
        count += 1
    return args




# f = Faker()

# ners=[]
# for _ in range(5):
#     ners.append(f.name())

print(f'origional: {ners}')
print(f'swaped: {swap(ners)}')


