def Subtraction(No1,No2):
    Ans = No1-No2
    return Ans

def Decorated_function(function_name):
    def Inner(A,B):
        if(A<B):
            A,B = B,A
        output = function_name(A,B)
        return output
    return Inner

def main():
    value_01=int(input('Enter first number:'))
    value_02=int(input('Enter second number:'))
    New_Function = Decorated_function(Subtraction)
    Result = New_Function(value_01,value_02)
    print('Subtraction',Result)

if __name__ == "__main__":
    main()