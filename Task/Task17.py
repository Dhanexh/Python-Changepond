# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitary number of keyword arguments. 

cars=[]
def create_car(*args,**car_info):
    car = {
        'manufacturer': args[0],
        'model': args[1]
    }
    car.update(car_info)
    cars.append(car)
 
def main():
    num_of_cars=int(input("Enter number of cars"))
    for i in range(0,num_of_cars):
        manufacturer=input("Enter Manufacturer")
        model=input("Enter Model")
        choice=int(input("Enter 0 if you want to add more info"))
        d={}
        while(not choice):
            key=input("Enter key")
            value=input("Enter value")
            d[key]=value
            choice=int(input("Enter 0 if you want to add more info"))
           
        create_car(*[manufacturer, model], **d)
    print(cars)
    
 
if __name__ == "__main__":
    main()