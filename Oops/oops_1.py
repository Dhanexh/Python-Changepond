# creating class 
class Student:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def Display(self):
        print(f'{self.firstname} {self.lastname}')

    

Obj1 = Student('Dhanesh','Chan')
# print(Obj1.firstname,Obj1.lastname) 
Obj1.Display() 