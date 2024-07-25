# Write a program which will check the number is greater and equal to and less than and equal to 90

def Check_Number(Number):
    if(Number >= 70 and Number <= 90):
        return Number


def main():
    size = int(input('Enter size: '))
    lst = []
    print('Enter values:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List:',lst)

    filter_list = list(filter(Check_Number,lst))
    print('Filter List:',filter_list)

       


if __name__ == "__main__":
    main()
