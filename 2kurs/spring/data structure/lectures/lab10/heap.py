# heap бол tree юм. Дотроо 2 төрөлтэй min, max
'''Хэрэглээ 
Мэдээллийг сортлоход, shortest path
Жнь: Task management

 List to Tree
left - 2 * i + 1
rigth - 2 * i + 2
parent - (i-1)//2



-complete zuun mochir duursen baih yostoi
-full tree 2mochir 2ula duursen bh yostoi
Root node нь child nodeuudese baga baih yostoi
 '''


class MaxHeap:
    def __init__(self, data):
        self.head = []

    def get_parent(i):
        return (i-1)//2

    def get_leftChild(i):
        return 2*i+1

    def get_rightChild(i):
        return 2*i+2

    def has_parent(i):
        return self.get_parent(i) >= 0

    def has_leftChild(i):
        pass

    def has_rightChild(i):
        pass

    def swap(i, j):
        pass

    def insert(key):
        pass

    def heap_up():
        pass
