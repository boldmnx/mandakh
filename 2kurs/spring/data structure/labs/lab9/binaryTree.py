class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, e):
        if e < self.data:
            if self.left is None:
                self.left = Node(e)
            else:
                self.left.insert(e)
        elif e > self.data:
            if self.right is None:
                self.right = Node(e)
            else:
                self.right.insert(e)

    def find(self, e):
        if e < self.data:
            if self.left is None:
                return print('Илэрц олдсонгүй')
            self.left.find(e)
        elif e > self.data:
            if self.right is None:
                return print('Илэрц олдсонгүй')
            self.right.find(e)
        else:
            print('Илэрц олдлоо: ' + str(self.data))

    def printBTree(self, node, level=0, prefix='Root: '):
        if node:
            print(' '*(level*4) + prefix + str(node.data))
            self.printBTree(node.left, level+1, 'L-- ')
            self.printBTree(node.right, level+1, 'R-- ')


btree = Node(50)
btree.insert(25)


btree.insert(75)
btree.insert(12)
btree.insert(30)
btree.insert(60)
btree.insert(85)
btree.insert(52)
btree.insert(70)

btree.insert(100)
btree.insert(200)
btree.insert(111)
btree.insert(222)
btree.insert(33)
btree.insert(44)
btree.insert(11)


btree.printBTree(btree)
btree.find(85)
