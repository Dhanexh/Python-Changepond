# Write a program which will take input from the user and Returns(Using function)
# 1)Addition on the list 
#     Example: [2,3,4,5,6,7]  --> 27
#     Note: don't use sum()
# 2)Maximum from the list
#     Example: [2,3,4,5,6,7]  --> 7
#     Note: don't use max()

list = []

def main():
    n = int(input('Enter size: '))
    for i in range(n):
        num = int(input())
        list.append(num)
    
    sum = 0
    for i in list:
        sum += i
    print("Additon of list: ",sum)

    max = 0
    for i in list:
        if(i > max):
            max = i
    print("Maximum of list: ",max)
    
    
if __name__ == "__main__":
    main()










