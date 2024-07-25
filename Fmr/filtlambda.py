
def main():
    size = int(input('Enter size: '))
    lst = []
    print('Enter values:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List:',lst)

    filter_list=list(filter(lambda number: number >= 70 and number <= 90 ,lst))
    print('Filter List:',filter_list)

       


if __name__ == "__main__":
    main()