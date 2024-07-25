# Create a simple calculator which will take two input number from the user and give following option
#     1)Addition
#     2)Subtraction
#     3)Multiplication
#     4)Division
# (you can solve above question using normal function )
# (also try to solve using dictionary)



def Addition(value1, value2):
    Ans = value1+value2
    return Ans

def Subtraction(value1, value2):
    Ans = value1-value2
    return Ans

def Multiplication(value1, value2):
    Ans = value1*value2
    return Ans

def Division(value1, value2):
    Ans = value1/value2
    return Ans

def main():
    while True:
        num01 = int(input('Enter num1: '))
        num02 = int(input('Enter num2: '))

        print('Choose operation')
        print('1.Addition\n2.Subtration\n3.Multiplication\n4.Division\n5.Exit')
        select = int(input('Select 1/2/3/4/5: '))

        if(select == 1):
            Ans = Addition(num01,num02)
            print(f'Addition {num01} and {num02}:',Ans)
        elif(select == 2):
            Ans = Subtraction(num01,num02)
            print(f'Subtration {num01} and {num02}:',Ans)
        elif(select == 3):
            Ans = Multiplication(num01,num02)
            print(f'Mutiplication {num01} and {num02}:',Ans)
        elif(select == 4):
            Ans = Division(num01,num02)
            print(f'Division {num01} and {num02}:',Ans)
        elif(select == 5):
            print("Exiting...")
            break
        else:
            print('choose 1/2/3/4')

if __name__=="__main__":
    main()