def count_num(lst,number):
    count = 0
    for i in lst:
        if(i == number):
            count += 1
    return count


def main():
    print('Enter size:')
    size = int(input())
    data_input = []

    print('Enter values:')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User List:',data_input)

    SearchNum = int(input('Enter element to be checked:'))
    print(SearchNum,"is repeating",count_num(data_input,SearchNum),"times")

if __name__=="__main__":
    main()
