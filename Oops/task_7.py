# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.


class Numbers:
    def __init__(self, value):
        self.value = value

    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value**0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        if self.value < 1:
            return False
        return self.value == self.SumFactors()

    def Factors(self):
        factors = [i for i in range(1, self.value) if self.value % i == 0]
        print(f"Factors of {self.value}: {factors}")

    def SumFactors(self):
        return sum(i for i in range(1, self.value) if self.value % i == 0)

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    number1 = Numbers(num1)
    number2 = Numbers(num2)
    
    print(f"Is {number1.value} a prime number? {'Yes' if number1.ChkPrime() else 'No'}")
    print(f"Is {number2.value} a prime number? {'Yes' if number2.ChkPrime() else 'No'}")
    
    print(f"Is {number1.value} a perfect number? {'Yes' if number1.ChkPerfect() else 'No'}")
    print(f"Is {number2.value} a perfect number? {'Yes' if number2.ChkPerfect() else 'No'}")
    
    number1.Factors()
    number2.Factors()
    
    print(f"Sum of factors of {number1.value}: {number1.SumFactors()}")
    print(f"Sum of factors of {number2.value}: {number2.SumFactors()}")

if __name__ == "__main__":
    main()
