# Creating a list 
# Creating same datatype
course = ['Python','Java','PHP']
rollno = [123,124,124]

# Creating mixed datatype
mixed_type = ['Dhan',123,True,67.68]
print('Hetrogenous',mixed_type)
print('length',len(mixed_type))

# Postion index
print('Access value of 1',mixed_type[0])
print('Access value of 2',mixed_type[1])
print('Access value of 3',mixed_type[2])
print('Access value of 4',mixed_type[3])

# Negative index
print('Access value of 1',mixed_type[-4])
print('Access value of 2',mixed_type[-3])
print('Access value of 3',mixed_type[-2])
print('Access value of 4',mixed_type[-1])

# Slicing [start:stop(excluded)]
print('Slicing',mixed_type[1:3])
print('Slicing',mixed_type[0:3])
print('Slicing',mixed_type[-4:-1])

#Mutable (can change,add and delete)
fruits = ['Mango','Banana','Grapes','Watermelon']
fruits[1] = 'Kiwi'
print(fruits)
del fruits
fruits[1:3]=['banana','orange']
print(fruits)
 
 