mixed_type ={'Moni',25,True,124}
more_add={'Ravi',23}
# add() method -> add element to the set
mixed_type.add('Hello')
print(mixed_type)

# update() method
mixed_type.update(more_add)
print(mixed_type)

# discard() method -> remove Specifi element
mixed_type.discard(True)
print(mixed_type)

# remove() method
mixed_type.remove('Hello')
print(mixed_type)