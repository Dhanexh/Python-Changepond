# Write an application which will duplicate files

import os

def Duplicate_file(source_file, duplicate_file):
    if not os.path.isfile(source_file):
        print("file not exist")
    
    src_file = open(source_file, 'r')
    dup_file = open(duplicate_file, 'w')
    content = src_file.read()
    dup_file.write(content)
    print("File duplicated successfully")
    

def main():
    source_file = input("Enter the path of the source file: ")
    duplicate_file = input("Enter the path of the duplicate file: ")
    
    Duplicate_file(source_file, duplicate_file)


if __name__ == "__main__":
    main()
