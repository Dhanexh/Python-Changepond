# 3)Write a program which contains one class named as Circle
# Circle class contains three instance variables as Radius,Area ,Circumference.
# That class contains one class variable as PI which is initialize to 3.14
# Inside init method initialize all instance variables to 0.0
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
# ,Display( )
# Accept method will accept value of Radius from user.
# CalculateArea () method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference () method will calculate circumference of circle and store it into instance variable
# Circumference.
# And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
# After designing the above class call all instance methods by creating multiple objects

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0

    def Accept(self):
        self.radius = int(input("Enter radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print('Radius:',self.radius,'\nArea:',self.Area,'\nCircumference:',self.Circumference)

Obj1 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

    
