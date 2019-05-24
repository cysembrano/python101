def greet_user(first_name, last_name):
    print(f'Hi There {first_name} {last_name}')
    print('Welcome Aboard')


print("Start")
greet_user(last_name="Sembrano", first_name="Cyrus")  # Keyword arguments
greet_user("Cyrus", "Sembrano")  # Positional Arguments
print("Finish")
