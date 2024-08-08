# Create a class representing a shopping cart. 
# Which include methods for adding items , removing items , 
# total items and total price

class Shopping_card:
    items = {
        "apple":100,
        "orange":300,
        "grapes":130,
        "cherry":130,
        "banana":140,
        "guava":105,
        "watermelon":150,   
             }
    
    user_items = {}

    def display(self):
        print(self.items)

    def user_display(self):
        print(self.user_items)

    def adding_items(self,items):
        self.user_items[items] = self.items[items]

    def remove_items(self,items):
        del self.user_items[items]

    def total_items(self):
        print(f"Total Items { len(self.user_items.values())}")

    def total_price(self):
        finals = sum(self.user_items.values())
        print("Total price",finals)

Obj1 =Shopping_card()
Obj1.display()
Obj1.adding_items("apple")
Obj1.user_display()
Obj1.adding_items("orange")
Obj1.user_display()
Obj1.adding_items("banana")
Obj1.user_display()
Obj1.total_items()
Obj1.total_price()
Obj1.remove_items("apple")
Obj1.total_items()
Obj1.total_price()

