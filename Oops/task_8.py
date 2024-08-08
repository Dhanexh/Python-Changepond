# Create a class representing a shopping cart. 
# Which include methods for adding items , removing items , 
# total items and total price

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def total_items(self):
        return sum(details['quantity'] for details in self.items.values())

    def total_price(self):
        return sum(details['price'] * details['quantity'] for details in self.items.values())



if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item('Apple', 20, 3)
    cart.add_item('Banana', 10, 2)
    print(cart.items)
    print(f"Total items: {cart.total_items()}")
    print(f"Total price: ${cart.total_price()}")

    cart.remove_item('Apple', 1)
    print("\nAfter removing 1 Apple:")
    print(cart.items)
    print(f"Total items: {cart.total_items()}")
    print(f"Total price: ${cart.total_price()}")


