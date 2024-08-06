# 4) Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That Class Contains one class variable as ROI which is initialize to 10.5
# Inside init method initialize all name and amount variable by accepting the values from user.
# There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
# Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
# And Display () method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects
# has context menu

class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0

    def Create(self):
        self.Name = input("Enter Name: ")
        self.Amount = int(input("Enter Amount: "))

    def Deposit(self):
        value = int(input("Enter Deposit Amount: "))
        self.Amount += value
        print("Balance:",self.Amount)

    def Withdraw(self):
        value = int(input("Enter Withdrawal Amount: "))
        self.Amount -= value
        print("Balance:",self.Amount)

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest:",Interest)

    def Display(self):
        print("Name:",self.Name)
        print("Amount:",self.Amount)


Obj1 = BankAccount()
Obj1.Create()
Obj1.Deposit()
Obj1.Withdraw()
Obj1.CalculateInterest()
Obj1.Display()

