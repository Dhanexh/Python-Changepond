# 9-1. Restaurant: Make a class called Restaurant. The init() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.



class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Resaurant name:",self.restaurant_name,"// Cuisine type:",self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is open")

restaurant1 = Restaurant("KFC","Chinese")
restaurant2 = Restaurant("Dominos","Japanese")
restaurant3 = Restaurant("McDonalds","Korean")

print(restaurant1.restaurant_name,restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.open_restaurant()


