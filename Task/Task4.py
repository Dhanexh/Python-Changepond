# Write a program which will count the frequency of letters of the string

def frequency(str,letter):
    count=0
    for i in str:
        if(i == letter):
            count += 1
    return count


def main():
    str = input('Enter the string: ')
    letter = input('Enter the letter: ')
    count = frequency(str,letter)
    print("Frequency of",letter,"is",count)




if __name__=="__main__":
    main()