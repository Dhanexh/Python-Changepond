class Mobile:
    def __init__(self,brand,RAM):
        self.brand = brand
        self.RAM = RAM

    def Display(self):
        print(f'{self.brand} {self.RAM}')

    

Obj1 = Mobile('Realme','8GB')
Obj1.Display() 