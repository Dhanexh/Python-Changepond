# Write a program to check if a string contains any special character

def isSpecial(str,special):
    for i in str:
        if i in special:
            return "It has Special character"
    return "has no Special character"

def main():
    special = "!@#$%^&*()"
    str = input('Enter String: ')
    print(isSpecial(str,special))



if __name__ == "__main__":
    main()