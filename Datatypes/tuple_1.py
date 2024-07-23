#Create a tuple
#Hemogenous
student_id = (123,124,125,126)
ice_cream = ('Vanilla','Coco-chips','Blueberry')

#Hetrogenous
mixed_type = (123,'Hello',False,56.78)

#len()
print("Length of student_id tuple:", len(mixed_type)) 

#using index --> blueberry(Positive index)
print("Element at index 2 in ice_cream tuple:", ice_cream[2]) 

#using index --> False(Nagative index)
print("Element at index -3 in mixed_type tuple:", mixed_type[-2])

#using slicing --> 'Hello',False
print("Slicing 'Hello' and False from mixed_type tuple:", mixed_type[1:3])


ice_cream = ('Vanilla')
print(ice_cream,type(ice_cream))
ice_cream = ('Vanilla',)
print(ice_cream,type(ice_cream))


# immutable (cannot modify, delete or add)
# mixed_type[0] = True
# print(mixed_type)

ice_cream = ('Vanilla','Choco-chips','Blueberry','Vanilla')
countmethod = ice_cream.count('Vanilla')
print('Count method:',countmethod)
print()
indexmethod = ice_cream.index('Vanilla')
print('Index method:',indexmethod)
