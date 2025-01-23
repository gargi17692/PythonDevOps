# Class_Methods Vs Static_Methods
#*A Class_Meyhod cloud be accessed from the Class level only
import csv

class Item(object):
     pay_rate = 0.8 # The pay rate after 20% discount
     all=[]
     def __init__(self, name: str, price: float, quantity=0):
         # Run validations to the received arguments
         assert price >= 0, f"price {price} is not greater or equal to zero!"
         assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"
         # Assign to self object
         self.name=name
         self.price=price
         self.quantity=quantity
         # Actions to execute
         Item.all.append(self)  # self is the insatance it's-self every time it is created
         return None
     def display(self):
         return self.price*self.quantity
     def apply_dicount(self):
         self.price=self.price*self.pay_rate
    
     #*When we call our classmethod ; the class object it's-self passed as the first argument always in the background 
     @classmethod
     def instantiate_from_csv(cls):
          with open('items.csv', 'r') as f:
               reader = csv.DictReader(f)
               items=list(reader)
          for item in items:
               #print(item)
               Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity')),
               )
     def __repr__(self):
          return f"Item({"self.name"}, {self.price}, {self.quantity})" 
    
Item.instantiate_from_csv()    
print(Item.all)
