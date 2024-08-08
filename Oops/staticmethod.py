class Student:

    @staticmethod
    def RollNumber(x):
        print('Inside static method:',x)

# static method call
Student.RollNumber(101)

# using object
S1 = Student()
S1.RollNumber(102)







class Student:
    def RollNumber(x):
        print('Inside static method:',x)

Student.RollNumber = staticmethod(Student.RollNumber)
Student.RollNumber(103)