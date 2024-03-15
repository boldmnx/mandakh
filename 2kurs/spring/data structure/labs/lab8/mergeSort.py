import random
import timeit


def mergeSort(myList):
    time = 0
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1
    time = timeit.timeit()
    return round(time, 3)


myList = [55, 63, 18, 32, 19, 34, 14, 94, 10, 41, 35, 4, 81, 35, 35, 67, 32, 16, 18, 73, 45, 100, 84, 3, 36, 73, 74, 62,
          41, 51, 56, 75, 5, 94, 35, 13, 49, 29, 68, 40, 27, 7, 73, 41, 84, 67, 77, 8, 86, 32, 82, 3, 43, 97, 95, 47, 85, 41, 9]

# print('Энгийн жагсаалт:')
# print(myList)
print(f'time merge: {mergeSort(myList)}')
# print('Эрэмбэлсэн жагсаалт:')
# print(myList)


def swap_one(args):
    time = 0
    for _ in range(len(args)):
        for i in range(len(args)-1):
            if args[i] > args[i+1]:
                args[i], args[i+1] = args[i+1], args[i]
                time += timeit.timeit()
    return round(time, 3)


lst = [55, 63, 18, 32, 19, 34, 14, 94, 10, 41, 35, 4, 81, 35, 35, 67, 32, 16, 18, 73, 45, 100, 84, 3, 36, 73, 74, 62,
       41, 51, 56, 75, 5, 94, 35, 13, 49, 29, 68, 40, 27, 7, 73, 41, 84, 67, 77, 8, 86, 32, 82, 3, 43, 97, 95, 47, 85, 41, 9]


print(f'sorted bubble: {swap_one(lst)}')
# print(f'swaped: {lst}')
