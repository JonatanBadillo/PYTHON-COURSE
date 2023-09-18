# While
print('While')

# condition = True
# while condition:
#     print('Executing whyle cycle')
# else:
#     print('Ending of the whyle cycle')

counter = 0
while counter<3:
    print(counter+1)
    counter += 1
else:
    print('Ending of the whyle cycle')


# Printing numbers from 5 - 1 in a descending manner
print('----------------------------')
print('Printing numbers from 5 - 1 in a descending manner')

counter = 5
while counter>0:
    print(counter)
    counter -= 1
else:
    print('Ending of the whyle cycle')


# FOR
print('----------------------------')
print('FOR')

string = 'hola'
for letter in string:
    print(letter)
else:
    print('Ending of the for cycle')

# BREAK IN PYTHON
print('----------------------------')
print('BREAK IN PYTHON')

for letter in 'Netherland':
    if letter == 'a':
        print(f'Letter found: {letter}')
        break  
else:
    print('Ending of the for cycle')

