import heapq


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

heapq.heapify(numbers)

print("Heapified лист:", numbers)

heapq.heappush(numbers, 7)
print("7 хийсний дараа:", numbers)

min_element = heapq.heappop(numbers)
print("Устгагдсан элемент:", min_element)
print(min_element, " устгагдасны дараа", numbers)

k_smallest = heapq.nsmallest(3, numbers)
print("Хамгийн бага 3 эл:", k_smallest)

k_largest = heapq.nlargest(3, numbers)
print("Хамгийн их 3 эл:", k_largest)


heapq.heappush(numbers, 11)
print('11 нэмсний дараа', numbers)
