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

    def printBTree(self):
        if self.left:
            self.left.printBTree()
        print(self.data)
        if self.right:
            self.right.printBTree()


btree = Node(50)
btree.insert(25)


btree.insert(75)
btree.insert(12)
btree.insert(30)
btree.insert(60)
btree.insert(85)
btree.insert(52)
btree.insert(70)


# btree.find(86)
btree.printBTree()
