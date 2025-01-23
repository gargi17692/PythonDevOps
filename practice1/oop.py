class Item(object):
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self, name: str, price: float, quantity=0):
         # Run validations to the received arguments
         assert price >= 0, f"price {price} is not greater or equal to zero!"
         assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

         # Assign to self object
         self.name=name
         self.price=price
         self.quantity=quantity
         return None
    def display(self):
        return self.price*self.quantity
    def apply_dicount(self):
        self.price=self.price*self.pay_rate
    
# for recap add script from oopy.txt
