class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print("Name:",self.name,"\n Price:",self.price,"\nQuantity:",self.quantity)
        
        
    def update_quantity(self,new_quantity):
        self.quantity = new_quantity
        print("Quantity updated to:",self.quantity)
        
    
        