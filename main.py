from item import Item
from phone import Phone
from keyboard import Keyboard

# Load items from CSV and inspect all instances
Item.instantiate_from_csv()
print(Item.all)

# Static method
print(Item.is_integer(7.0))

# Child class usage
phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())

# Encapsulation: getters / setters / increment / discount
item1 = Item("MyItem", 750)
item1.name = "OtherItem"
print(item1.name)
item1.apply_increment(0.2)
print(item1.price)   
item1.apply_discount()
print(item1.price)   

# Polymorphism: class-level pay_rate override
keyboard1 = Keyboard("Keyboard", 1000, 3)
keyboard1.apply_discount()
print(keyboard1.price)  
