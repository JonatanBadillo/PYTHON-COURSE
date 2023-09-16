print("Hello World from Python")

# Sending greeting using my name
print("Hello I am Jonatan")

# Variables in Python
print('----------------------------')
print("Variables in Python")
myVariable = "Hello from Python"
print(myVariable)

myVariable = 2
print(myVariable)
x = 9
y = 10
print(x+y)

x = 3
y = 7
z = x + y
print(z)

# Memory address
print('----------------------------')
print("Memory Address:")
print(id(x)) # Getting the memory adress of the variable x
print(id(y)) # Getting the memory adress of the variable y
print(id(z)) # Getting the memory adress of the variable z

# Exercise Declaration of Variables
print('----------------------------')
print("Exercise Declaration of Variables: ")
name = "Juan Perez"
phone_number = 5562187
mail = "jperez@mail.com"

print(name)
print(phone_number)
print(mail)

# Type of Data
print('----------------------------')
print("Type of data: ")
print(x)
print(type(x))
x = "Jonatan"
print(x)
print(type(x))
x = 15.67
print(x)
print(type(x))
x = True
print(x)
print(type(x))

# String Management
print('----------------------------')
print("String Management: ")
myFavoriteSinger = "Adele" + " ,The GOAT"
print("My favorite singer is: " + myFavoriteSinger)
print("My favorite singer is: ",myFavoriteSinger)

number1 = "1"
number2 = "4"
print("Concatenation: " + number1 + number2)

number1 = 1
number2 = 4
print("Addition: ", number1 + number2)

# Boolean 
print('----------------------------')
print("Boolean: ")
myVariable = 1 > 2
print(myVariable)
myVariable = 1 < 2
print(myVariable)

# Process user input
print('----------------------------')
print("Process user input: ")
number1 = int(input("Give me a number: "))
number2 = int(input("Give me a number: "))
result = number1 + number2
print("Result: ",result)

# Exercise Rate your Day
print('----------------------------')
print("Exercise Rate your Day: ")
day = int(input("Rate your day(from 1 to 10): "))
print("My day is : ",day)

# Exercise Information of a book
print('----------------------------')
print("Exercise Information of a book: ")
title = input("Title: ")
author = input("Author: ")
print(title + " was written by " + author)