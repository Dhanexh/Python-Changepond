# def sum_all(*args):
#     count = 0
#     for i in args:
#         count += i
#     return count

# output = sum_all(1,2,3,4,5)
# print('addition:',output)








# def printname(*args):
#     for names in args:
#         for name in names:
#             print(name)

# def main():
#     changepond = ['gokul','ajith','suresh','dhanesh']
#     printname(changepond)







# def staffDetails(**kwarg):
#      for key,value in kwarg.items():
#           print(f'{value}')
     
# def  main():
#     changepond = {'Name':'Ajtih','Age':21,'MobileNum':123456789}
#     staffDetails(**changepond)





def StaffDetails(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} is {value}')

def main():
    StaffDetails(Name='gokul', Age=21, MobileNum=1234444)


if __name__ == "__main__":
    main()
