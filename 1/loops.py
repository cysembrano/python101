# while loops
print('')
loop_count = 1
while loop_count <= 5:
    print('*' * loop_count)
    loop_count = loop_count + 1
print('while loop done')

# for loops
print('')
for item in 'Python':
    print(item)

# for loops on list
print('')
for item in ['Cyrus', 'Jane', 'John']:
    print(item)

# for loops with range function
print('')
for item in range(10):
    print(item)
print('')
for item in range(10, 15):
    print(item)
print('')
for item in range(20, 28, 2):
    print(item)
print('')
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f'total is {total}')

# nested loops
print('')
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

