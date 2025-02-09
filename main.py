from product import Product
from product_manager import ProductManager

product_manager = ProductManager()

product_manager.add_product(Product("Laptop", 1200.99, 5))
product_manager.add_product(Product("Mobile", 500.99, 10))
product_manager.add_product(Product("Tablet", 700.99, 3))
product_manager.add_product(Product("Camera", 1000.99, 2))
product_manager.add_product(Product("Headphones", 200.99, 8))

product_manager.display_all_products()
print("Total value of products:", product_manager.total_value_of_products())
#product_manager.product_removal("Camera")