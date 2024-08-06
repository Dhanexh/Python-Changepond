# 6)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value1,Value2.
# Inside init method initialize all instance variables to 0.
# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of Value1 and Value2 and return result.
# Subtraction() method will perform subtraction of Value1 and Value2 and return result.
# Multiplication() method will perform multiplication of Value1 and Value2 and return result.
# Division() method will perform division of Value1 and Value2 and return result.
# After Designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value: "))
        self.Value2 = int(input("Enter second value: "))

    
    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        try:
            result = self.Value1 / self.Value2
            return result
        except ZeroDivisionError:
            return "Division by zero is not allowed."

def main():
    num1 = Numbers()
    num2 = Numbers()
    
    print("For the first object:")
    num1.Accept()
    print(f"Addition: {num1.Addition()}")
    print(f"Subtraction: {num1.Subtraction()}")
    print(f"Multiplication: {num1.Multiplication()}")
    print(f"Division: {num1.Division()}")

    print("\nFor the second object:")
    num2.Accept()
    print(f"Addition: {num2.Addition()}")
    print(f"Subtraction: {num2.Subtraction()}")
    print(f"Multiplication: {num2.Multiplication()}")
    print(f"Division: {num2.Division()}")

if __name__ == "__main__":
    main()
