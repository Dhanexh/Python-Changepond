#Write an application which copy content from one file to another(other file will be created from user)

import os
 
def copy_file(file1, file2):
    if not os.path.exists(file1):
        print("File not exist")
    else:
        f1 = open(file1, 'r')
        f1_read = f1.read()
       
        f2 = open(file2, 'w')
        f2.write(f1_read)
        print("Success -> Content copied")
        
 
def main():
    file1 = input('Enter file1: ')
    file2 = input('Enter file2 to be created: ')
    copy_file(file1, file2)
 
if __name__ == "__main__":
    main()


