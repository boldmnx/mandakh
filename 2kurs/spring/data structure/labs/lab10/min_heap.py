
class MinHeap:
    def __init__(self):
        self.lst = []

    def insert(self, e):
        self.lst.append(e)
        self.heap_down(len(self.lst)-1)

    def get_root(self, i):
        return (i-1)//2

    def has_root(self, i):
        return self.get_root(i) > 0

    def swap(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def heap_down(self, i):
        while self.has_root(i) and self.lst[i] <= self.lst[self.get_root(i)]:
            self.swap(i, self.get_root(i))
            i = self.get_root(i)

    def print_Tree(self, i=0, level=0, prefix='Root: '):
        if i < len(self.lst):
            print(' ' * (level * 4) + prefix + str(self.lst[i]))
            self.print_Tree(2 * i + 1, level + 1, 'L-- ')
            self.print_Tree(2 * i + 2, level + 1, 'R-- ')

    def print_List(self):
        print(self.lst)


toonud = [45, 99, 63, 27, 29,  57, 42, 35, 12, 98, 12]

minHeap = MinHeap()

for i in toonud:
    minHeap.insert(i)


print("Одоогийн heap")
minHeap.print_List()
minHeap.print_Tree()

minHeap.insert(11)
print("11 утга нэмэгдсэний дараа")
minHeap.print_List()
minHeap.print_Tree()
