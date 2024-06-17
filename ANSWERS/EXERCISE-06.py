# Question 01
# Write a program that allows users to enter a positive integer n. Your program should the print numbers from 1 to n.
n = int(input('Enter a number: '))
for number in range(1, n+1):
    print(number)

# Question 02
# Write a program that prints all the even numbers between -50 and 30 (inclusive).
for number in range(-50, 31):
    print(number)

# Question 03
# Write a program that allows users to enter a positive integer n. Your program should then calculate the sum of all odd numbers within the range.
n = int(input('Enter a positive integer: '))
total_of_odd_numbers = 0
for number in range(1, n+1):
    if number % 2 != 0:
        total_of_odd_numbers += number
print(total_of_odd_numbers)

# Question 04
# Write a program that allows users to enter 4 positive integer. Your program should then calculate the product of all numbers.
product = 1
for _ in range(4):
    number = int(input('Enter a number: '))
    product *= number
print(product)

# Question 05
# Write a program that prints all the numbers between 1500 and 2300 (inclusive) that are divisible by both 5 and 7.
for number in range(1500, 2301):
    if number % 5 == 0 and number % 7 == 0:
        print(number)

# Question 06
# Write a program to print a multiplication table of a given number.
n = int(input('Enter a number: '))
print('Multiplication table of number ' + str(n))
for i in range(1, 13):
    print('{0} x {1} = {2}'.format(n, i, n * i))

# Question 07
# Write a program to check if a given string is a palindrome. Palindrome is a word, phrase or sequence that reaeds the same backwards as forwards 
string = 'abba'
backward_string = ''
for character in string:
    backward_string = character + backward_string
if backward_string == string:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')

# Question 08
# Write a program that prints 'Easycode Python Programming Course' without alphabet 'o'.
sentence = 'Easycode Python Programming Course'
filtered_sentence = ''
for character in sentence:
    if character != 'o' or character != 'O':
        filtered_sentence += character
print(filtered_sentence)

# Question 09
# Write a program to check the number of vowels in a given string.
sentence = 'Write a program to check the number of vowels in a given string'
vowels = 0
for character in sentence:
    if character in 'aeiouAEIOU':
        vowels += 1
print('The number of vowels in the string: ' + str(vowels))

# Question 10
# Write a program to check if alphabet 'A' or 'a' exists in a given string.
string = 'Write a program to check if alphabet A or a exists in a given string'
found = False
for character in string:
    if character == 'A' or character == 'a':
        found = True
        break
if found:
    print('Found!')
else:
    print('Not Found!')

# Question 11
# Write a program to print multiplication table of number 2 to 12 using a nested for loop.
for outer_num in range(1, 13):
    print('\n')
    for inner_num in range(1, 13):
        print('{0} x {1} = {2}'.format(outer_num, inner_num, outer_num * inner_num))