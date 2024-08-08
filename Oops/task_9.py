# File handling: Accept file name and one string from the user and return the frequency  
# of that string from the file Example: Demo.txt changepond Search 'Changepond' in Demo.txt

import os
 
def task():
    if os.path.exists(r"D:\Python\Oops\demo.txt"):
        permission = open(r"D:\Python\Oops\demo.txt","r")
        content = permission.read()
        lists = content.split(" ")
        word = input("Enter search words: ")
        if word in lists:
            return f"{word} is in the file"
        else:
            return f"{word} is not in the file"
    else:
        print("file doesn't exist")
print(task())