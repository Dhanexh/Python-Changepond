# open() function -> filename, mode (r,w,a,....)

# file_read = open('string_1.py','r')
# print(file_read.read())

import os
def CreateFile(filename):
    if(os.path.exists(filename)):
        print('File alreay exists')
    else:
        file_create = open(filename,'w')

def main():
    print('Enter filename you want to create: ')
    file_name = input()

    CreateFile(file_name)

if __name__=="__main__":
    main()
