class Node:
    def __init__(self, data):
        self.data = data
        self.address = None


class LinkedList:
    def __init__(self):
        self.head = None

    # add
    def add_begin(self, data):
        newNode = Node(data)
        newNode.address = self.head
        self.head = newNode

    def add_middle(self, e, index):
        newNode = Node(e)

        if self.head is None:
            self.head = newNode

        current = self.head
        prev = self.head
        count = 0

        while current.address is not None:
            while index == 0:
                print('Index зөв оруулна уу!')
                index = int(input('indexe oruul'))
            count += 1
            if count == index:
                newNode.address = current.address
                prev.address = newNode
                return
            prev = current.address
            current = current.address
        current.address = newNode

    def add_end(self, e):
        newNode = Node(e)
        if self.head is None:
            self.head = newNode
            return

        current = self.head
        while current.address:
            current = current.address
        current.address = newNode

    # delete
    def delete_begin(self):
        if not self.head:
            print('Node алга')
            return
        self.head = self.head.address

    def delete_end(self):
        if not self.head:
            print('Node алга')
            return
        current = self.head
        while current.address.address is not None:
            current = current.address
        current.address = None

    def delete_middle(self, e):
        current = self.head
        pre = None
        while current is not None:
            if current.data == e:
                pre.address = current.address
                print(f'{e} устгагдлаа.')
            pre = current
            current = current.address

    # read search count
    def read(self):
        current = self.head
        while current:
            print(f'-> {current.data}')
            current = current.address

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.address
        return count

    def search(self, e):
        if self.head is None:
            print('Node алга')
            return

        current = self.head

        while current:
            if current.data == e:
                print(f'Утга олдлоо: {e}')
                return True
            current = current.address
        print(f'Утга олдсонгүй!!!')
        return False


# node = LinkedList()
# node.add_end(1)
# node.add_end(2)
# node.add_end(3)
# node.add_end(4)
# # node.add_end(3)
# # node.read()
# # print(node.count())
# # node.search(2)
# # node.delete_begin()
# # node.read()
# # node.delete_middle(2)
# # node.add_middle(5, 2)
# node.read()
