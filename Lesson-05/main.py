# LIST
print('LIST')
names = ['Memo','Leo','Kevin','Diego']

# printing the list of names
print(names)

# accessing to the elements of the list
print('----------------------------')
print('Accessing to the elements of the list')
print(names[0])
print(names[2])

# accesing to the elements in reverse manner
print('----------------------------')
print('Accesing to the elements in reverse manner')
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