'''
map is өгөгдлийн хийсвэр төрөл
map vs massive. Massive indextei map key valuetai
Tagline is ded ner
map hereglee is omno uzsen treenuud bugd map yum
'''

class   AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def get_address(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return None

my_address_book = AddressBook()

my_address_book.add_contact("John Doe", "123 Main St, Cityville")
my_address_book.add_contact("Jane Smith", "456 Elm St, Townsville")

print("John Doe's address:", my_address_book.get_address("John Doe"))
print("Jane Smith's address:", my_address_book.get_address("Jane Smith"))
print("Unknown Person's address:", my_address_book.get_address("Unknown Person"))
