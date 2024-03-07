class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Tree:
    def __init__(self, root):
        self.root = root

    def display_tree(self, node, level=0):
        if node is not None:
            print("  " * level + str(node.data))
            for child in node.children:
                self.display_tree(child, level + 1)


root_node = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

