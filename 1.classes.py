# Create class:
class Item:
    # Methods:
    def calculate_total_price(self, x, y):
        return x*y

# Create an instance of a class   
item1 = Item()

# Assign attributes:
item1.name = "Phone"
item1.price = 10000
item1.quantity = 5

# Calling methods from instances of a class:
print(item1.calculate_total_price(item1.price, item1.quantity))

# Create second instance(one can create as much as want):
item2 = Item()

# Assign attributes:
item2.name = "Laptop"
item2.price = 30000
item2.quantity = 3

# Calling methods from instances of a class:
print(item2.calculate_total_price(item2.price, item2.quantity))