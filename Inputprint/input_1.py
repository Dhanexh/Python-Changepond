# print('Enter Name')
# Name = input()
# print('The Name is',Name)
# print()

# Name = input("Enter Name")
# print('The Name is',Name)


num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
print("Original numbers :",num1,num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Swapped numbers :",num1,num2)

num1 = num1 * num2
num2 = int(num1 / num2)
num1 = int(num1 / num2)
print("Re-swapped numbers :",num1,num2)

num1, num2 = num2, num1
print("Rere-swapped numbers :",num1,num2)