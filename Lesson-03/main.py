# If/Else
print('If/Else')
condition = 'hola'

if condition == True:
    print('True Condition')
elif condition == False:
    print('False Condition')
else:
    print('Unrecognized Condition')

# Converting numbers to text
print('----------------------------')
print('Converting numbers to text')

number = int(input('Provide a number between 1 and 3: '))

if number == 1 :
    print('One')
elif number == 2 :
    print('Two')
elif number == 3 :
    print('Three')
else:
    print('Invalid Number')       

# Ternary operator 
print('----------------------------')
print('Ternary operator ')

condition = True
print('True Condition') if condition else print('False Condition')

# Stages of Life
print('----------------------------')
print('Stages of Life')

age = int(input('Provide your age: '))

if age>=0 and age<=10: 
    print('Amazing childhood')
elif age>=11 and age<= 20:
    print('A lot of changes and a lot of study')
elif age>=21 and age<=30:
    print('Love and work starts')
else:
    print('Unrecognized stage of life')