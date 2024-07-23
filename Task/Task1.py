# Create a menu_card list
#     veg_starter = ['paneer 65','chilly paneer','veg crispy']
#     1) display menu_card
#     2) Add starter in the menu_card
#     3)Update Starter in te menu_card
#     4)remove Starter in the menu_card

#     Example:
#     Add : Which starter you want to add in menu?
#     paneer roll
#     ['Paneer 65','Chilly paneer','Veg crispy','Paneer roll']
#     Added Successfully

menu_card = ['paneer 65', 'chilly paneer', 'veg crispy']


def display_menu():
    print("Menu Card:",menu_card)


def add_starter(starter):
    menu_card.append(starter)
    print(f"{starter} added to the menu card.")


def update_starter(old_starter, new_starter):
    index = menu_card.index(old_starter)
    menu_card[index] = new_starter
    print(f"{old_starter} updated to {new_starter}.")



def remove_starter(starter):
    menu_card.remove(starter)
    print(f"{starter} removed from menu card.")


def main():
    print("Select option")
    print("1.Display Menu Card")
    print("2.Add to Menu Card")
    print("3.Update in Menu Card")
    print("4.Remove from Menu Card")

    option = input("Enter your choice (1-4): ")

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
    else:
        print("Invalid option.")



if __name__=="__main__":
    main()




###################################


# menu_card = {
#     'paneer 65': 1,
#     'chilly paneer': 5,
#     'veg crispy': 8
# }

# def display_menu():
#     print("Menu Card:",menu_card)

# def add_starter(starter):
#     index = len(menu_card) + 1
#     menu_card[starter] = index
#     print(f"{starter} added to the menu card.")

# def update_starter(old_starter, new_starter):
#     menu_card[new_starter] = menu_card.pop(old_starter)
#     print(f"{old_starter} updated to {new_starter}.")

# def remove_starter(starter):
#     menu_card.pop(starter)
#     print(f"{starter} removed from menu card.")

# def main():
#     print("Select option")
#     print("1. Display Menu Card")
#     print("2. Add to Menu Card")
#     print("3. Update in Menu Card")
#     print("4. Remove from Menu Card")

#     option = input("Enter your choice (1-4): ")

#     if option == '1':
#         display_menu()
#     elif option == '2':
#         starter = input("Enter the starter to add: ")
#         add_starter(starter)
#     elif option == '3':
#         old_starter = input("Enter old starter: ")
#         new_starter = input("Enter new starter: ")
#         update_starter(old_starter, new_starter)
#     elif option == '4':
#         starter = input("Enter starter to remove: ")
#         remove_starter(starter)
#     else:
#         print("Invalid option.")

# if __name__=="__main__":
#     main()