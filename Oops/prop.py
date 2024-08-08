class Arithmatic:
    def __init__(self,value):
        self._value = value

    def getValue(self):
        print('To the retrive the value of \'value\'')
        return self._value
    
    def setValue(self,value):
        print('Setting value to',value)
        self._value = value

    def delValue(self):
        print('Deleting the value')
        del self._value
    
    value = property(getValue,setValue,delValue)

A1 = Arithmatic(12)
print(A1.value)

A1.value = "Dhanesh"
del A1.value