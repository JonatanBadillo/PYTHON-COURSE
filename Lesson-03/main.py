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

# Grading System
'''
    Task instructions:
    The objective of this exercise is to create a grading system, as follows:
    The user will provide a value between 0 and 10.
    If it is between 9 and 10: print an A
    If it is between 8 and less than 9: print a B
    If it is between 7 and less than 8: print a C
    If it is between 6 and less than 7: print a D
    If it is between 0 and less than 6: print an F
    Any other value should print: Incorrect value
    For example:
    Provide a value between 0 and 10:
    A
'''
print('----------------------------')
print('Grading System')

note = int(input('Provide a value between 0 and 10: '))
grade = 'A'
if 0<= note < 6:
    grade = 'F'
elif 6<= note < 7:
    grade = 'D' 
elif 7<= note < 8:
    grade = 'C'  
elif 8<= note < 9:
    grade = 'B' 
elif 9<= note <= 10:
    grade = 'A'
else:
    grade = 'Incorrect value'   


print(grade)