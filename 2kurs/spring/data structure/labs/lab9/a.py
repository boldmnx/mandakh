class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Database:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, root, key, value):
        if root is None:
            return TreeNode(key, value)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key, value)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key, value)
        else:
            root.value = value  # Update value if key already exists
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root.value if root else None
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._get_min_value(root.right)
            root.value = self.search(root.key)  # Update value with successor's value
            root.right = self._delete_recursive(root.right, root.key)
        return root

    def _get_min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

# Example usage:
db = Database()
db.insert(5, "Value 5")
db.insert(3, "Value 3")
db.insert(7, "Value 7")
db.insert(2, "Value 2")
db.insert(4, "Value 4")

print("Search for key 3:", db.search(3))
print("Search for key 6:", db.search(6))  # Not present

db.delete(3)
print("After deleting key 3, search for key 3:", db.search(3))  # None

db._get_min_value(6)