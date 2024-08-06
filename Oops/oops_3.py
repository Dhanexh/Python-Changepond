# class Student:
#     graduation = 'BE'
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.graduation = 'ME'
   

# Obj1 = Student('Dhanesh','Chan')
# print(Obj1.graduation)
# print(Obj1.__class__.graduation)

class Student:
    graduation = 'BE'

    @classmethod
    def Graduate_in(cls):
        print('Graduation in:',cls.graduation)
Student.Graduate_in()