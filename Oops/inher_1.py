#parent class/base class
class Person:
    def __init__(self,identity,name):
        self.identity=identity
        self.name=name

    def displayInfo(self):
        print(f'Name: {self.name} Id:{self.identity}')

class Employee(Person):  #derived class
    def __init__(self, identity, name,salary):
        super().__init__(identity, name)
        self.salary=salary
        
    def show(self):
        print("Inside Child")

e1=Employee(4463,"Dhanesh",25000)
e1.displayInfo()
e1.show()
print(e1.salary)