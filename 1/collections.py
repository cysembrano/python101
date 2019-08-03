# collections
print('')
names = ['bob', 'ben', 'dan', 'don']
print(names[2])
print(names[-1])
print(names[-2])
print(names[2:])
print(names)

print('')
names[0] = 'jon'
print(names)

# 2D List
print('')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])
print(matrix)

# Dictionaries
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("birthday"))
print(customer.get("birthday", "Say October 6 instead"))

# add new key
customer["gender"] = "Male"
print(customer["gender"])

# change a key
customer["name"] = "Cyrus"
print(customer["name"])
print()
snumbers = [5, 6, 8, 9]
snumbers.append(10)
print(f'put 10 at the end {snumbers}')
snumbers.insert(2, 7)
print(f'put 7 in between: {snumbers}')
snumbers.remove(5)
print(f'remove 5: {snumbers}')
snumbers.pop()
print(f'10 was removed after pop: {snumbers}')
index_6 = snumbers.index(6)
print(f'q: where is 6? a: {index_6}')
print(f'is 50 in numbers? {50 in snumbers}')
snumbers.append(9)
print(snumbers)
print(f'how many number 9\'s? {snumbers.count(9)}')
snumbers.append(4)
print(snumbers)
snumbers.sort()
print(f'sorted snumbers {snumbers}')
snumbers.reverse()
print(f'reverse sorted snumbers {snumbers}')
snumbers_2 = snumbers.copy()
snumbers_2.append(10)
print(snumbers)
print(snumbers_2)



