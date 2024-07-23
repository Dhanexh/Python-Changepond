num = int(input('Enter Number:'))
if(num%2 == 0):
    print(f'{num} is even')
else:
    print(f'{num} is odd')
print()

days = int(input('Enter day betwwen 1 to 7:'))
if(days == 1):
    print('Monday: learning datatypes')
elif(days == 2):
    print('Tuesday: learning Functions')
elif(days == 3):
    print('Wednesday: learning string')
# elif(days == 4):
#     print('Thursday: learning datatypes')
# elif(days == 5):
#     print('Friday: learning datatypes')
# elif(days == 6):
#     print('Saturday: learning datatypes')
else:
    print('enter correct number')
