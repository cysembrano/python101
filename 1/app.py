
# variable declarations
n = 'Name'
a = 20
i = True

# user inputs
input_var = input('Tell ')
print(type(input_var))
age = 2000 - int(input_var)
print(age)

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

# len function
course = 'My Python101 Course'
print(str(len(course)))



