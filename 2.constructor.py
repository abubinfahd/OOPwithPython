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
        self.price = self.price * self.pay_rate

   
item1 = Item('Phone', 10000, 5) 
item2 = Item('Laptop', 30000, 3)

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

item1.apply_discount()
print(item1.price)
item2.pay_rate=0.7
item2.apply_discount
print(item2.price)


