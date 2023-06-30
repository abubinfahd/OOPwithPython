from phone import Phone

item1 = Phone("Sonny", 10000, 3)
item1.send_email()

item1.apply_increment(0.2)
print(item1.price)