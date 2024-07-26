# Write a function that accepts a list of items a person wants on 
# a sandwich.The function should have one parameter that collects as 
# many items as the function call provides, should print sandwich that's being ordered

def make_sandwich(*items):
    if not items:
        print("You not added any items to sandwich.")
        return items

    print("Sandwich Order:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ordered with above items.")

def main():
    Make = ('cabbage', 'tomato', 'sauce', 'cheese', 'mayo')
    make_sandwich(*Make)

if __name__ == "__main__":
    main()