# public: These are accesible from the outside of class
# protected: _single underscore within the class and its subclass
# private: __double underscore

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

    def SalaryInfoSelf(self):
        print(f'{self.name} holding salary of {self.salary}')

E1 = Employee("Dhanesh",50000)
print(E1.name)
print(E1._salary)
# E1.SalaryInfoSelf()