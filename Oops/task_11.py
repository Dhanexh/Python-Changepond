# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self,first_name,last_name,contact,address):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.address = address

    def describe_user(self):
        print("\n----User's Information----")
        print("Name:",self.first_name,self.last_name,"\nContact:",self.contact,"\nAddress:",self.address)
    
    def greet_user(self):
        print("Have a great day",self.first_name,self.last_name)


User1 = User("Dhanesh","Chan","9942184648","Chennai")
User2 = User("Jackie","Chan","9945673245","Mumbai")
User3 = User("Ronie","Chan","9945637122","Kolkata")

User1.describe_user()
User1.greet_user()

User2.describe_user()
User3.greet_user()

User3.describe_user()
User3.greet_user()
