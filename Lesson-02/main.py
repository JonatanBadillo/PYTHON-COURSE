# Arithmetic operators
a = 3
b = 2
addition = a + b
#print('The result is: ',addition)
print(f'The result of the addition is: {addition}')

substraction = a - b
print(f'The result of the substraction is: {substraction}')

multiplication = a * b
print(f'The result of the multiplication is: {multiplication}')

division = a / b
print(f'The result of the division is: {division}')

division = a // b
print(f'The result of the division(int) is: {division}')

residue = a % b
print(f'The residue is: {residue}')

exponent = a ** b
print(f'The result of the exponent is: {exponent}')


# Exercise
'''
In the following exercise, we are asked to calculate the area and perimeter of a Rectangle. To do this, we will need to create the following variables:

height (int)
width (int)

The user should provide the values for height and width,
and then the result should be printed in the following format
(no accents and respect spaces, capital letters, lowercase letters, and line breaks):

Provide the height:
Provide the width:
Area: <area>
Perimeter: <perimeter>

The formulas for calculating the area and perimeter of a Rectangle are:
Area: height * width
Perimeter: (height + width) * 2
'''
print('----------------------------')
print('Rectangle Exercise')
height = int(input('Provide the height: '))
width = int(input('Provide the width: '))
area = height * width
perimeter = (height + width) * 2

print(f'Area: {area}')
print(f'Perimeter: {perimeter}')

# Assignment Operators
print('----------------------------')
print('Assignment Operators')
myVariable = 10
print(myVariable)

myVariable += 1
print(myVariable)

myVariable -= 2
print(myVariable)

myVariable *= 3
print(myVariable)

# Comparison Operators
print('----------------------------')
print('Comparison Operators')
a = 4
b = 2

result = a == b
print(f'Result == : {result}')

result = a != b
print(f'Result != : {result}')

result = a > b
print(f'Result > : {result}')

result = a >= b
print(f'Result >= : {result}')

# Exercise Even number or Odd number
print('----------------------------')
print('Exercise Even number or Odd number')
a = int(input('Provide a number: '))

#print(a % 2)
if a % 2 == 0:
    print(f'The value of {a} is even number')
else:
    print(f'the value of {a} is odd number')