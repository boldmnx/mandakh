


class Tree:
    def __init__(self):
        self.head = None

        self.parent = None
        self.child = None

    def add_child(self, child,  parent):
        if self.head.parent == parent:
            self.head.parent = parent
            self.head.child = child

        # while current is not None:
        #     if current.root == parent:
        #         current.child = newNode
        #     current = current.child
        return self.head.child

    def add_root(self, root):
        baseRoot = Node(root)
        if self.head is None:
            self.head = baseRoot
            return baseRoot.root

    def display(self):
        pass


class Node:
    def __init__(self, root):
        self.root = root
        self.address = None


t = Tree()
davka = t.add_root('davka')
d_ohin = t.add_child('davkagin ohin', parent=davka)
ohin = t.add_child('davkagin ohiniinii ohin', parent=d_ohin)

# temeet = Tree()
# # Chimedmaa
# temeet.add_child('Ганбаатар')
# temeet.add_child('Дарьхижав')
# temeet.add_child('Жигмэд')
# temeet.add_child('Тодгэрэл')
# temeet.add_child('Дэлгэрцэцэг')
# print(f'{temeet.root} хүүхдүүд:')
# for child in temeet.children:
#     print(child, end='\n->')
