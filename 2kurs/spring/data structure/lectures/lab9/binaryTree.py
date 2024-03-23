class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


class binaryTree:
    def __init__(self):
        self.head = None

    def insert(self, e):
        if self.head is None:
            self.head = Node(e)
            return
        current = self.head
        while current:
            if current.root == e:
                return True
            elif current.root < e:
                current.right = Node(e)
            elif current.root > e:
                current.left = Node(e)
            current = current.root


n = binaryTree(8)

n1 = binaryTree(9)

n1.search()
