import datetime
today = datetime.date.today()
year = today.year
print(year)

try:
    # num1 = int(input('enter num1: '))
    # num2 = int(input('enter num2: '))
    # result = num1/num2
    # print(result)
    items = ["Bread","Butter","Jam","Cheese"]
    # items[len(items)] = "Spread"
    num1 = int(input('enter num1: '))
    assert num1%2==0
except ZeroDivisionError:
    print("num2 cannot be zero")
except ValueError:
    print("only numbers allowed")
except AssertionError:
    print("enterd value not mating test condition")
else:
    print(num1,"is even")
finally:
    print("Program is over")


yob = int(input('enter year of birth: '))
age = year - yob
if(age < 18):
    raise Exception(f'Age should be graeter than 18 and age is {age}')
print(age)