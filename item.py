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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        # self.__name = value
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    # Methods:
    def calculate_total_price(self):
        return self.__price * self.quantity
    

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
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"
    
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
        Hello Bara!
        We have {self.name} {self.quantity} times.
        Regards, Don.
        """
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()