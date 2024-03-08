

class Node:
    def __init__(self, root, parent=None):
        self.root = root
        self.children = []
        self.parent = parent
        pass


class Tree:
    def __init__(self):
        self.head = None

    def add_child(self, child, parent=None):
        newChild = Node(child, parent)
        if self.head is None:
            self.head = newChild
            return self.head
        newChild.parent.children += [newChild]
        return newChild

    def display(self, root, e=0):
        if root:
            if e == 0:
                print(f'{root.root}')
            else:
                print(f' {"  "*e }|-- {root.root}')

            for i in root.children:
                self.display(i, e+1)


# recursion function
tree = Tree()
chimedmaa = tree.add_child('Чимэдмаа')
jigmed = tree.add_child('Жигмэд', parent=chimedmaa)
todol = tree.add_child('Тодол', parent=chimedmaa)
delger = tree.add_child('Дэлгэр', parent=chimedmaa)

bold = tree.add_child('Болд-Эрдэнэ', parent=jigmed)
galaa = tree.add_child('Галбадрах', parent=jigmed)

bolorjin = tree.add_child('Болоржин', parent=todol)
ariunjin = tree.add_child('Ариунжин', parent=todol)

uyaral = tree.add_child('Уярал', parent=bold)

tree.display(chimedmaa)
