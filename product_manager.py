from product import Product
class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def display_all_products(self):
        if not self.products:
            print("No products found !")
        else:
            for product in self.products:
                product.display()
        
    def total_value_of_products(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value

    def product_removal(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Product {product_name} removed successfully !")
        print(f"Product {product_name} not found !")