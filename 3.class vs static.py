import csv

# Create class:
class Item:
    # Class attributes:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    # Constructor:
    def __init__(self, name: str, price: float, quantity=0):

        # Run validation to receive arguments:
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"

        # Assign self object:
        self.name = name
        self.price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    # Methods:
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            #print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Magic method __repr__
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

   


print(Item.is_integer(7.5)) # 7, 7.0, 7.5

"""
1. We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
2. We generally use static methods to create utility functions

"""