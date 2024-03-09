
import random
import timeit

numbers = [8, 6, 7, 4, 3]
swapOne = [8, 6, 7, 4, 3]
swapTwo = [8, 6, 7, 4, 3]
swapTree = [8, 6, 7, 4, 3]
# for i in range(5):
#     numbers += [random.randint(1, 10)]

# 1


def swap_one(args):
    time = 0
    for _ in range(len(args)):
        for i in range(len(args)-1):
            if args[i] > args[i+1]:
                args[i], args[i+1] = args[i+1], args[i]
                time += timeit.timeit()
    return round(time, 3)


print(f'default: {numbers}')
print(f'  #1 -------------')
print(f'timed: {swap_one(swapOne)}')
print(f'swaped: {swapOne}')

# 2


def swap_two(args):
    isTrue = True
    time = 0

    while isTrue:
        isTrue = False
        for i in range(len(args)-1):
            if args[i] > args[i+1]:
                args[i], args[i+1] = args[i+1], args[i]
                time += timeit.timeit()
                isTrue = True

    return round(time, 3)


print(f'  #2 -------------')
print(f'timed: {swap_two(swapTwo)}')
print(f'swaped: {swapTwo}')


# 3


def swap_tree(args):
    isTrue = True
    time = 0
    count = 0
    while isTrue:
        isTrue = False
        for i in range(len(args)-count-1):
            if args[i] > args[i+1]:
                args[i], args[i+1] = args[i+1], args[i]
                time += timeit.timeit()
                isTrue = True
        count += 1
    return round(time, 3)


print(f'  #3 -------------')
print(f'timed: {swap_tree(swapTree)}')
print(f'swaped: {swapTree}')
