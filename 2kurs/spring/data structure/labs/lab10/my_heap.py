# heap бол tree юм. Дотроо 2 төрөлтэй min, max
# Task management


# zuun 2*i+1,
#  baruun 2*i+2
# parent  = (i-1)//2
# complete zuun mochir duursen baih yostoi
# full tree 2mochir 2ula duursen bh yostoi
class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return (i-1)//2

    def get_leftChild(self, i):
        return 2*i+1

    def get_rightChild(self, i):
        return 2*i+2

    def has_parent(self, i):
        return self.get_parent(i) > 0

    def has_leftChild(self, i):
        return self.get_leftChild(i) < len(self.heap)

    def has_rightChild(self, i):
        return self.get_rightChild(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def print_heap(self):
        print(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heap_up(len(self.heap)-1)

    def heap_up(self, i):
        while (self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

max_heap = MaxHeap()

array = [45, 99, 63, 27, 29, 57, 42, 35, 12, 98]

for i in array:
    max_heap.insert(i)

print("Одоогийн heap")
max_heap.print_heap()

max_heap.insert(50)
print("50 утга нэмэгдсэний дараа")
max_heap.print_heap()