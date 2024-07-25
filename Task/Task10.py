#sort a dictionary by value in python (lambda function)
def main():
    list = [
        {'name': 'shreya', 'age': 15},
        {'name': 'pratiksha', 'age': 13},
        {'name': 'prerna', 'age': 15}
    ]

    sorted_list = sorted(list, key=lambda val: (val['name'], val['age']))

    for i in sorted_list:
        print(i)

if __name__ == "__main__":
    main()