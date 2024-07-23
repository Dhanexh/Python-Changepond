watch_details = {
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000
}

#Keys()-> returns a list containing the dictionarys keys
key_method = watch_details.keys()
print('Key Method:',key_method)

value_method = watch_details.values()
print('Value Method:',value_method)

#get method -> returns the value of a specified key
get_method = watch_details.get('Titan')
print('Get Method:',get_method)


#items() method
item_method = watch_details.items()
print('Item Method:',item_method)

#update({}) method->insert an item inot the dictionary
watch_details.update({'Noise':12000})
print('Updated Method:',watch_details)

#pop() method ->Remove element with the specified key
watch_details.pop('Titan')
print('Poped Method:',watch_details)