# def Addition(value1,value2):
#     return value1+value2

# Output_1 = Addition(12,13)
# print("Addition:",Output_1)

# Output_1 = Addition("Dhanesh","Chan")
# print("Addition:",Output_1)




class Transport:
    def __init__(self,brand,mode):
        self.brand = brand
        self.mode = mode

    def Display(self):
        print(f'{self.brand} and {self.mode}')

class Car(Transport):
    pass

class Boat(Transport):
    pass

Obj1 = Car('Mercedes','Road')
Obj2 = Boat('Jetski','Sea')
Obj1.Display()
Obj2.Display()

