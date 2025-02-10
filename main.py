from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    product_manager = ProductManager()

    product_manager.add_product(Product("Tv", 1200.99, 5))
    product_manager.add_product(Product("Mobile", 500.99, 19))
    product_manager.add_product(Product("Tablet", 700.99, 3))
    product_manager.add_product(Product("Camera", 1000.99, 22))
    product_manager.add_product(Product("Headphones", 200.99, 8))

    #product_manager.display_all_products()
    #print("Total value of products:", product_manager.total_value_of_products())
    #product_manager.product_removal("Camera")

    
    cart=Cart()
    products=product_manager.products
    for _ in range(3):
        product=random.choice(products)
        max_quantity=min(product.quantity,3)
        
        if max_quantity>0:
            quantity=random.randint(1,max_quantity)
            cart.add_to_cart(product,quantity)

    cart.display_cart()
    #cart.total_price()
    cart_total=cart.total_price()
    print(f"\nTotal Cart Value: {cart_total:.2f}")

if __name__ == "__main__":
    main()