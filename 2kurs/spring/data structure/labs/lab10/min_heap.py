class MinHeap:
    def __init__(self):
        self.lst = []

    def insert(self, e):
        self.lst.append(e)
        self.heap_down(len(self.lst)-1)

    def print_min(self):
        print(self.lst)

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


toonud = [45, 99, 63, 27, 29, 57, 42, 35, 12, 98, 12]

minHeap = MinHeap()

for i in toonud:
    minHeap.insert(i)

minHeap.print_min()
minHeap.insert(12)
print('12 nemew')
minHeap.print_min()

'''
|45
    R|42
        R|57
        L|63
    L|12
        R|29
            L|98
        L|27
            R|35
            L|99


'''
