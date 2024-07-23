menu_card = ['Paneer','Dal','Rice']
print('Available items in menu card:',menu_card)

# append
menu_card.append('Kofta')
print('After using append method:',menu_card)

# 'Dal Tadka','Briyani'
# extend() --> Add the elements of a list(or iterable)
# to the end of list
menu_card.extend(['Dal Tadka','Briyani'])
print('Using Extend method:',menu_card)

# insert() --> Adds an element in the specified position
menu_card.insert(1,'Vegbiriyani')
print('Using Insert method:',menu_card)

# remove() --> will remove specified value
menu_card.remove('Dal Tadka')
print('Using Remove method:',menu_card)

# pop() --> removes element of specified position
menu_card.pop(2)
print('Using pop method:',menu_card)

menu_card = ['Panner','Biriyani','Dosa','Panner']

# Index method
index_method = menu_card.index('Dosa')
print('It will give the position : ',index_method)

index_method = menu_card.index('Panner')
print('It will give the position : ',index_method)

# sort method
menu_card.sort()
print("Using sort method:",menu_card)