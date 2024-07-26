# Write an application which will append your existing file

import os

def Appendfile(filename, data):
    if os.path.exists(filename):
        open_file = open(filename, 'a')
        open_file.write(data)
        print("Success -> Content appended")
    else:
        print("File not exist.")

def main():
    filename = input("Enter filename: ")
    data = input("Enter data to append: ")
    
    Appendfile(filename, data)

if __name__ == "__main__":
    main()


 