# def Addition():
#     print('Inside Addition')
# Addition()

# def Addition(value_01):
#     print('Inside Addition')
#     print('Argument:',value_01)
# Addition(12)


# def Addition(value_01,value_02):
#     print('Inside Addition')
#     print('Argument1:',value_01)
#     print('Argument2:',value_02)
#     print(f'{value_01} and {value_02} addition is:',value_01+value_02)
# Addition(12,13)

def Addition(value_01,value_02):
    print('Inside Addition')
    print('Argument1:',value_01)
    print('Argument2:',value_02)
    Add = value_01 + value_02
    Sub = value_01 - value_02
    return Add,Sub

Result1, Result2 = Addition(12, 13)
print('Addition:',Result1)
print('Subtraction:',Result2)









