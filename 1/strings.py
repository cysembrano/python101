# strings
singleline = 'Cyrus Sembrano'
multiline = '''
The 
quick\'s
brown
fox
jumps 
over
'''
print(singleline)
print(singleline[0])
print(singleline[-1])
# up to the index three with three excluded
print(singleline[0:3])
print(singleline[1:])
print(singleline[:5])
print(singleline[:])
# up to the last but last excluded
print(singleline[1:-1])

# formatted strings
first = 'cyrus'
last = 'sembrano'
msg = f'{first} [{last}] is great'
print(msg)

# methods and functions
course = 'My Python101 Course'
print(str(len(course)))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.find('My'))
print(course.replace('Course', 'Subject'))
print(course.replace('o', 'i'))
print('Python' in course)
print('*' * 100)
print(course)
