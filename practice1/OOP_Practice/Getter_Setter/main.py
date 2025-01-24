# Getters and Setters
from item import Item

item1=Item("MyItem", 750)
#item1.name="OtherItem" # AttributeError: property 'name' of 'Item' object has no setter
#print(item1.__name) # AttributeError: 'Item' object has no attribute '__name'.

# Setting an Attribute
item1.name="OtherItem"
# Getting an Attribute
print(item1.name)