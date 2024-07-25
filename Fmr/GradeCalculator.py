# Create a Grade Calculator using Dictionary

def calculateGrade(marks,result):
    final = sum(marks.values())
    if final >= 400:
        return result[400]
    elif final <=399 and final >=300:
        return result[300]
    elif final <=299 and final >=200:
        return result[200]
    elif final < 200:
        return result[100]
    
def main():
    result = {
        400:"Your Grade: O :)",
        300:'Your Grade: A',
        200:"Your Grade: B",
        100:'Your Grade: F'}
   
    marks = {}
    marks["English"] = int(input("Enter English Mark: "))
    marks["Tamil"] = int(input("Enter Tamil Mark: "))
    marks["Maths"] = int(input("Enter Maths Mark: "))
    marks["Science"] = int(input("Enter Science Mark: "))
    marks["Social"] = int(input("Enter Social Mark: "))
        
    print()
    print("Marks:",marks)
    print(calculateGrade(marks,result))


if __name__ == "__main__":
    main()


# Enter English Mark: 10
# Enter Tamil Mark: 34
# Enter Maths Mark: 67
# Enter Science Mark: 90
# Enter Social Mark: 90

# Marks: {'English': 10, 'Tamil': 34, 'Maths': 67, 'Science': 90, 'Social': 90}
# Your Grade: B