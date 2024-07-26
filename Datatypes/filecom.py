import os
import filecmp
def Comparefiles(filename1,filename2):
    if(not os.path.exists(filename1)):
        print('Not Exists:',filename1)
    elif(not os.path.exists(filename2)):
        print('Not Exists:',filename2)
    else:
        compare = filecmp.cmp(filename1,filename2)
        if compare == True:
            print('Success -> files are same')
        else:
            print('Failure -> files are different')


def main():
    file_01 = input('Enter first file name: ')
    file_02 = input('Enter second file name: ')
    Comparefiles(file_01,file_02)

if __name__=="__main__":
    main()
