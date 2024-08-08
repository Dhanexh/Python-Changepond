class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def Displayinfo(self):
        print(f'Name : {self.name} Id: {self.id}')

class employee(Person):
    def show(self):
        print('Child Class')
# Emp=Person('Dhanesh','4463')
# Emp.Displayinfo()

Emp=employee('Suresh','4455')
Emp.Displayinfo()
Emp.show()