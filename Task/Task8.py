# course = [ '' , 'python' ,'java',';$','angu;lar','php']
# filter_course = ['python','java','PHP']


course = ['', 'python', 'java', ';$', 'angu;lar', 'php']

filter_course = list(filter(lambda val: val.isalpha() and val != '', course))
print(filter_course)


