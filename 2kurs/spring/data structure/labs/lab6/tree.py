class Tree:
    def __init__(self, root):
        self.root = root
        self.children = []

    def add_child(self, child):
        self.children += [child]


class Node:
    def __init__(self, data):
        self.root = data
        self.children = []

    def add_node(self, obj):
        self.children += [obj]


temeet = Tree('Чимэдмаа')

temeet.add_child('Ганбаатар')
temeet.add_child('Дарьхижав')
temeet.add_child('Жигмэд')
temeet.add_child('Тодгэрэл')
temeet.add_child('Дэлгэрцэцэг')

for child in temeet.children:
    print(child)
