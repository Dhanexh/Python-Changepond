# Write an application which will delete duplicate files
import os
import filecmp

def Delete_file(file1,file2):
    if not os.path.isfile(file1):
        print("1st file not exist")
    elif not os.path.isfile(file2):
        print("2nd file not exist")
    else:
        compare = filecmp.cmp(file1,file2)
        if compare == True:
            os.remove(file2)
            print('Success -> Duplicatefile is deleted')
        else:
            print('Failure -> files are different')

def main():
    file1 = input("Enter 1st file: ")
    file2 = input("Enter 2nd file: ")
    
    Delete_file(file1, file2)


if __name__ == "__main__":
    main()