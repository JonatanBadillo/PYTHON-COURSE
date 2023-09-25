# LIST
print('LIST')
names = ['Memo','Leo','Kevin','Diego']

# printing the list of names
print(names)

# accessing to the elements of the list
print('----------------------------')
print('Accesssing to the elements of the list')
print(names[0])
print(names[2])

# accesing to the elements in reverse manner
print('----------------------------')
print('Accessing to the elements in reverse manner')
print(names[-1])
print(names[-2])

# Printing a range
print('----------------------------')
print('Printing a range')
print(names[0:2]) # without including second index

# Go from the beginning to the end of the list without including index 3
print('----------------------------')
print('Go from the beginning to the end of the list without including index 3')
print(names[:3])

# Go from selected index to the end of the list
print('----------------------------')
print('Go from selected index to the end of the list')
print(names[1:])

# Changing a value of the list
print('----------------------------')
print('Changing a value of the list')
names[3] = 'Henry'
print(names)

# Iterate a list
print('----------------------------')
print('Iterate a list')
listNames = ''
for i in names:
    listNames += i + ' '

print(listNames)

# Length of a list
print('----------------------------')
print('Length of a list')
print(len(names))

# Adding an element
print('----------------------------')
print('Adding an element')
names.append('Julian')
print(names) 

# Inserting an element in a specific index
print('----------------------------')
print('Inserting an element in a specific index')
names.insert(1, 'Octavio')
print(names)

# Removing an element
print('----------------------------')
print('Removing an element')
names.remove('Octavio')
print(names)

# Removing the last added element
print('----------------------------')
print('Removing an element')
names.pop()
print(names)

# Deleting an index
print('----------------------------')
print('Deleting an index')
del names[1]
print(names)

# Clean all the list
print('----------------------------')
print('Clean all the list')
names.clear()
print(names)

# Deleting all the list
del names

# Exercise 1. Iterate over a range from 0 to 10 and print numbers divisible by 3
print('----------------------------')
print('EXERCISE 1')
for i in range(0,11):
    if i % 3 == 0:
        print(i)


# Exercise 2. Create a range of numbers from 2 to 6 and print them
print('----------------------------')
print('EXERCISE 2')
for i in range (2,7):
    print(i)

# Exercise 3. Create a range from 3 to 10, but with an increment of 2 in 2, instead of 1 in 1
print('----------------------------')
print('EXERCISE 3')
for i in range (3,11,2):
    print(i)

# Tuples in Python 
print('----------------------------')
print('Tuples in python')# You can not add, modify or delete elements in a tuple
# Define a tuple
fruits = ('Banana','Apple','Orange')
# To know the length
print('To know the lenght of the tuple:')
print(len(fruits))
# Accesing to an element
print(fruits[0])
# Inverse navegation
print('Inverse navegation:')
print(fruits[-1])
# Range of values
print('Range of values:')
print(fruits[0:2]) # without including the last index
# Accesing all the elements
print('Accessing all the elements')
for fruit in fruits:
    print(fruit,end=' ')
print()

# To modify a tuple we have to convert into a list 
print('Modifying a element of a tuple')
listFruits = list(fruits)
listFruits[0] = 'Watermelon'
fruits = tuple(listFruits)
print(fruits)

# Deleting a tuple
del(fruits)