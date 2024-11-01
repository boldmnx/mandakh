class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"{self.name}: ${self.price:.2f}"


class Food(MenuItem):
    def __init__(self, name, price, cuisine):
        super().__init__(name, price)
        self.cuisine = cuisine

    def display(self):
        return f"{self.name} ({self.cuisine}): ${self.price:.2f}"


class Drink(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        return f"{self.name} ({self.size}): ${self.price:.2f}"


# Example usage
pizza = Food("Pizza", 12.99, "Italian")
coffee = Drink("Coffee", 2.99, "Medium")

print(pizza.display())  # Output: Pizza (Italian): $12.99
print(coffee.display())  # Output: Coffee (Medium): $2.99


#####################################
def print_menu_item(menu_item):
    print(menu_item.display())


# Example usage
items = [pizza, coffee]

for item in items:
    print_menu_item(item)
