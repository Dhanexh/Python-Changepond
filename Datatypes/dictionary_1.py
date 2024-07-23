watch_details = {
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Titan':12000
}
print('Length :',len(watch_details))
print('Type :',type(watch_details))
print('using key :',watch_details['Titan'])
print(watch_details)
print()



watch_details = {
    'Titan':8000,
    'Fastrack':5000,
    'Omega':9000,
    'Cartier':8000
}
print('Length :',len(watch_details))
print('Type :',type(watch_details))
print('using key :',watch_details['Titan'])
print('using key :',watch_details['Cartier'])
print(watch_details)
watch_details['Omega'] = 4000
print('After modifying :',watch_details)
watch_details['IWC'] = 5000
print('After new watch :',watch_details)


# Create dictionary food_items and price
food = {
    'Idli': 10,
    'Dosa': 30,
    'Vada': 7,
    'Parota': 15,
    'poori': 10,
}
print('Length :',len(food))
print('Type :',type(food))
print('using key :',food['Dosa'])
print('using key :',food['Parota'])
print(food)
food['Pongal'] = 4000
print('After modifying :',food)
food['Briyani'] = 5000
print('After new food :',food)
print()


# Nested dictionary
users = {
    'kastubag': {
        'firstname': 'Kasturi',
        'lastname': 'Chaware',
        'location': 'Pune'
    },
    'shrebag': {
        'firstname': 'Sheraya',
        'lastname': 'Bagde',
        'location': 'Nagpur'
    },
    'Prajakbag': {
        'firstname': 'Prajakta',
        'lastname': 'Patil',
        'location': 'Chennai'
    },
}

# for key, details in users.items():
#     if key == 'kastubag':
#         print("Username:", key)
#         print("First Name:", details['firstname'])
#         print("Last Name:", details['lastname'])
#         print("Location:", details['location'])

for key in users:
    print(users['kastubag'])


