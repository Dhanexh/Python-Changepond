student_name = input('Enter name: ')
student_id = int(input('Enter ID: '))
# print(f'Student Name: {student_name.title()} \nStudent ID: {student_id}')
print(f'Student Name: {student_name.upper()} /Student ID: {student_id}')

# format method
print('Student Name: {} /Student ID: {}'.format(student_name,student_id))
print('Student Name: {} /Student ID: {}'.format(student_id,student_name))

