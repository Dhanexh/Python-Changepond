# Area of Circle = PI

def Area (Radius,PI=3.14):
    print('Radius:',Radius)
    print('PI value:',PI)
    Result = PI*Radius*Radius
    return Result

def main():
    # # Positional Argument
    # Output_1 = Area(10,12)
    # print('Area of circle:',Output_1)

    # # First argument is positional and second is default
    # Output_1 = Area(10)
    # print('Area of circle:',Output_1)

    # # Keyword argument
    # Output_2 = Area(PI=3,Radius=12)
    # print('Area of circle:',Output_2)

    # Keyword argument and second is default
    Output_2 = Area(Radius=12)
    print('Area of circle:',Output_2)







if __name__=="__main__":
    main()

