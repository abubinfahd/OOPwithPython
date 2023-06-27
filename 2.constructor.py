# Create class:
class Item:
    # Constructor:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Methods:
    def calculate_total_price(self):
        return self.price * self.quantity

# Create an instance of a class   
item1 = Item('Phone', 10000, 5)
# Create second instance(one can create as much as want):
item2 = Item('Laptop', 30000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())



