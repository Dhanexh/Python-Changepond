menu_card = {
    'paneer 65': 1,
    'chilly chicken': 5,
    'veg crispy': 8
}

def display_menu():
    print("Menu Card:",menu_card)

def add_starter(starter):
    index = len(menu_card) + 1
    menu_card[starter] = index
    print(f"{starter} added to the menu card.")

def update_starter(old_starter, new_starter):
    menu_card[new_starter] = menu_card.pop(old_starter)
    print(f"{old_starter} updated to {new_starter}.")

def remove_starter(starter):
    menu_card.pop(starter)
    print(f"{starter} removed from menu card.")

def main():
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
            display_menu()
        elif option == '2':
            starter = input("Enter the starter to add: ")
            add_starter(starter)
        elif option == '3':
            old_starter = input("Enter old starter: ")
            new_starter = input("Enter new starter: ")
            update_starter(old_starter, new_starter)
        elif option == '4':
            starter = input("Enter starter to remove: ")
            remove_starter(starter)
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__=="__main__":
    main()