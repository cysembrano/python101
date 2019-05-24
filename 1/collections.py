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
