import math

# Question 01
# Write a program to accept a name and output the following greeting message: 'Hello, [name]!'
name = input('Enter your name: ')
print('Hello ' + name + '!')

# Question 02
# Write a program that prompts the user to input two numbers and calculate multiplication.
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
print(num1 * num2)

# Question 03
# Design a program that asks the user for the radius of a circle and calculates its circumference and area.
radius = float(input('Enter radius: '))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print('Circumference: ' + str(circumference))
print('Area: ' + str(area))

# Question 04
# Write a program to promp the user for their age and determine if they are classified as an adult.
age = int(input('Enter your age: '))
is_adult = age >= 18
print('Classified as adult: ' + is_adult)

# Question 05
# Design a program that asks the user for a string and counts the number of vowels present in it.
string = input('Enter a random string: ')
lower_string = string.lower()
vowels = lower_string.count('a') + lower_string.count('e') + lower_string.count('i') + lower_string.count('o') + lower_string.count('u')
print('Number of vowels: ' + str(vowels))
