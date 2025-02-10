from product import Product

class Cart:
    def __init__(self):
        self.cart_items=[]
        
    def add_to_cart(self,product,quantity):
        if quantity>product.quantity:
            print("Quantity not available")
        else:
            product.update_quantity(-quantity)
            self.cart_items.append({"product":product,"quantity":quantity})
            print(f"Product : {product.name} added to cart successfully")
    
    def total_price(self):
        total=0
        for item in self.cart_items:
            total+=item["product"].price*item["quantity"]
            print(f"Cart price: {total}")
        return total
            
        
    
    def display_cart(self):
        for item in self.cart_items:
            print("Product:",item["product"].name,"Quantity:",item["quantity"])