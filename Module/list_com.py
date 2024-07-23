# Using for loop create a list of square numbers
def main():
    n = int(input("Enter number: "))
    square_list = []
    for i in range(1, n+1):
        square_list.append(i*i)

    print("square numbers:", square_list)


if __name__=="__main__":
    main()