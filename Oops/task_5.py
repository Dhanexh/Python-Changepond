class MenuCard:
    def __init__(self):
        self.menu_card = {
            'paneer 65': 1,
            'chilly chicken': 5,
            'veg crispy': 8
        }
    
    def display_menu(self):
        print("Menu Card:")
        for starter, index in self.menu_card.items():
            print(f"{starter}: {index}")
    
    def add_starter(self, starter):
        index = len(self.menu_card) + 1
        self.menu_card[starter] = index
        print(f"{starter} added to the menu card.")
    
    def update_starter(self, old_starter, new_starter):
        if old_starter in self.menu_card:
            self.menu_card[new_starter] = self.menu_card.pop(old_starter)
            print(f"{old_starter} updated to {new_starter}.")
        else:
            print(f"{old_starter} not found in the menu card.")
    
    def remove_starter(self, starter):
        if starter in self.menu_card:
            self.menu_card.pop(starter)
            print(f"{starter} removed from menu card.")
        else:
            print(f"{starter} not found in the menu card.")

def main():
    menu = MenuCard()
    
    while True:
        print()
        print("Select option")
        print("1. Display Menu Card")
        print("2. Add to Menu Card")
        print("3. Update in Menu Card")
        print("4. Remove from Menu Card")
        print("5. Exit")

        option = input("Enter your choice (1-5): ")

        if option == '1':
            menu.display_menu()
        elif option == '2':
            starter = input("Enter the starter to add: ")
            menu.add_starter(starter)
        elif option == '3':
            old_starter = input("Enter old starter: ")
            new_starter = input("Enter new starter: ")
            menu.update_starter(old_starter, new_starter)
        elif option == '4':
            starter = input("Enter starter to remove: ")
            menu.remove_starter(starter)
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
