from binarytree import Node


def search(root, key):
    if root is None or root.value == key:
        return root

    if root.value < key:
        return search(root.right, key)

    return search(root.left, key)


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.left = Node(9)
root.left.left = Node(99)
root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(25)
key = 25
result = search(root, key)
if result:
    print(f"илэрц: {key}")
else:
    print(f"илэрц олдсонгүй.")

print(root)
