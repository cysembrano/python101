import math

# variable declarations
n = 'Name'
a = 20
guess_count = True

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

# integer division
print(10 // 3)
# exponents
print(10 ** 3)
# augmented assignment operator
x = 10
x += 3
print(x)

# operator precedence
# P-E-M-D-A-S
y = (10 + 3) * 2 ** 2
print(y)

# math functions
w = 2.9
print(round(w))
print(abs(-2.9))
print(math.ceil(2.9))
print(math.floor(2.9))

# conditions
is_hot = False
is_cold = False

if is_hot:
    print('It\'s a hot day.')
    print('Drink plenty of water')
else:
    print('not hot')


if is_hot:
    print('It\'s a hot day.')
    print('Drink plenty of water')
elif is_cold:
    print('It\'s a cold day.')
    print('Wear warm clothes')
else:
    print('It\'s a lovely day.')

name = 'Cyrus'

if len(name) > 2:
    print('Name is ok')
else:
    print('Name is too short')

# while loops
loop_count = 1
while loop_count <= 5:
    print('*' * loop_count)
    loop_count = loop_count + 1
print('while loop done')

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you win')
        break
    else:
        print(f'try {guess_limit - guess_count} more time.')
else:  # if code ends without breaking
    print('Sorry, you failed')


# car game
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print('Car started....')
    elif command == 'stop':
        print('Car stopped...')
    elif command == 'help':
        print('''
        start - to start car
        stop - to stop car
        quit - to quit car game
        ''')
    elif command == 'help':
        print('Thank you for playing')
    else:
        print('I do not understand command')



# user inputs
# print('')
# input_var = input('Input a number ')
# print(type(input_var))
# age = 2000 - int(input_var)
# print(age)


