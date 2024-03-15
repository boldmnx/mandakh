ners = ['az', 'ab',  'baw', 'bat', 'Jat', 'Bold', 'dondog', 'anugo', 'Aanaa']
# ners = ['az', 'ab',  'baw', 'bat', 'Jat']


def swaped_merge(args):
    if len(args) > 1:
        # divide
        mid = len(args)//2
        left = args[:mid]
        right = args[mid:]

        # conquer
        swaped_merge(left)
        swaped_merge(right)

        # combine
        k, j, i, u = 0, 0, 0, 0

        while i < len(left) and j < len(right):
            while ord(left[i][u].lower()) is ord(right[j][u].lower()):
                u += 1
            if ord(left[i][u].lower()) > ord(right[j][u].lower()):
                args[k] = right[j]
                j += 1
            else:
                args[k] = left[i]
                i += 1
            k += 1
            u = 0

        while i < len(left):
            args[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            args[k] = right[j]
            j += 1
            k += 1

        return args


print(f'initial : {ners}')

print(f'merge sorted: {swaped_merge(ners)}')
