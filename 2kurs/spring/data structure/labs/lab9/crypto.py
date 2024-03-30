class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self.insert_recursive(self.root, key, value)

    def insert_recursive(self, node, key, value):
        if key < node.key:
            if node.left:
                self.insert_recursive(node.left, key, value)
            else:
                node.left = TreeNode(key, value)
        elif key > node.key:
            if node.right:
                self.insert_recursive(node.right, key, value)
            else:
                node.right = TreeNode(key, value)
        else:
            node.value = value

    def search(self, key=None, value=None):
        if key is not None:
            return self.search_recursive(self.root, key=key)
        return self.search_recursive(self.root, value=value)

    def search_recursive(self, node, key=None, value=None):
        if key is not None:
            if not node or node.key == key:
                return node.value if node else None
            elif key < node.key:
                return self.search_recursive(node.left, key=key)
            else:
                return self.search_recursive(node.right, key=key)

        if not node or node.value == value:
            return node.key if node else None
        elif value < node.value:
            return self.search_recursive(node.left, value=value)
        else:
            return self.search_recursive(node.right, value=value)


def encrypt_message(message, bst):
    encrypted_message = ""
    for char in message:
        encrypted_char = bst.search(key=char)
        if encrypted_char:
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt_message(encrypted_message, bst):
    decrypted_message = ""
    for char in message:
        decrypted_char = bst.search(value=char)
        if decrypted_char:
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


bst = BST()
bst.insert("a", "!")
bst.insert("b", "@")
bst.insert("c", "#")
bst.insert("d", "$")
bst.insert("h", "№")
bst.insert("e", "%")
bst.insert("f", "^")
bst.insert("g", "&")
bst.insert("l", "&")
bst.insert("w", "!")
bst.insert("r", "#")
bst.insert("o", "@")

message = "hello world"
encrypted_message = encrypt_message(message, bst)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, bst)
print("Decrypted Message:", decrypted_message)
