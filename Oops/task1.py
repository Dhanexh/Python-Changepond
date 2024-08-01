class Product:
    _id_counter = 1  
    
    def __init__(self, name, price, description):
        self._id = Product._id_counter
        Product._id_counter += 1
        self.name = name
        self.price = price
        self.description = description
    
    def get_product_details(self):
        return {
            'ID': self._id,
            'Name': self.name,
            'Price': self.price,
            'Description': self.description
        }

class Cart:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Product '{product.name}' added to the cart.")
        else:
            print("Only instances of Product can be added to the cart.")
    
    def display_cart(self):
        if not self.products:
            print("Cart is empty.")
        else:
            for product in self.products:
                details = product.get_product_details()
                print(f"ID: {details['ID']}, Name: {details['Name']}, Price: ${details['Price']:.2f}, Description: {details['Description']}")

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, price, description):
        product = Product(name, price, description)
        self.products.append(product)
        print(f"Product '{name}' added to the list.")
    
    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                details = product.get_product_details()
                print(f"ID: {details['ID']}, Name: {details['Name']}, Price: ${details['Price']:.2f}, Description: {details['Description']}")

def create_product_from_user_input():
    name = input("Enter product name: ")
    price = int(input("Enter product price: $"))
    description = input("Enter product description: ")
    return name, price, description

def main():
    cart = Cart()
    product_manager = ProductManager()
    
    while True:
        print("Product Management System")
        print("1. Add Product")
        print("2. View Products")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name, price, description = create_product_from_user_input()
            product_manager.add_product(name, price, description)
            input()
        elif choice == '2':
            product_manager.view_products()
            input()
        elif choice == '3':
            if not product_manager.products:
                print("No products available to add to cart.")
                input()
            else:
                product_manager.view_products()
                product_id = int(input("Enter the ID of the product to add to the cart: "))
                product = next((p for p in product_manager.products if p._id == product_id), None)
                if product:
                    cart.add_product(product)
                    input()
                else:
                    print("Invalid product ID.")
                    input()
        elif choice == '4':
            cart.display_cart()
            input()
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
