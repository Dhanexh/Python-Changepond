# Write an application which can remove file or delete file

import os

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print('Success -> File deleted')
    else:
        print('File not exist')

def main():
    file_name = input('Enter file to delete: ')
    delete_file(file_name)

if __name__ == "__main__":
    main()
