# Create class:
class Item:
    # Class attributes:
    pay_rate = 0.8 # The pay rate after 20% discount
    # Constructor:
    def __init__(self, name: str, price: float, quantity=0):

        # Run validation to receive arguments:
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign self object:
        self.name = name
        self.price = price
        self.quantity = quantity

    # Methods:
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

# Create an instance of a class   
item1 = Item('Phone', 10000, 5) # try negative numbner of price or quantity
# Create second instance(one can create as much as want):
item2 = Item('Laptop', 30000, 3)

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

print(Item.__dict__) # All the attributes for class level
print("\n")
print(item1.__dict__) # All thye attributes for instance level

item1.apply_discount()
print(item1.price)


