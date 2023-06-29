from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):

        # Call Super function
        super().__init__(
            name, price, quantity
        )

        # Run validation to receive arguments:
        assert broken_phones >= 0, f"Broken Phone {broken_phones} is not greater than zero!"

        # Assign self object:
        self.broken_phones = broken_phones
   

Phone1 = Phone("IPhone13", 100000, 5, 1)
Phone2 = Phone("IPhone14", 150000, 5, 1)

# print(Phone1.calculate_total_price())
print(Item.all)
print(Phone.all)