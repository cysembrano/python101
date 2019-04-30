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

