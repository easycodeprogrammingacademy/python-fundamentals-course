# Question 01
# Write a program that prints 'HelloWorld' 10 times using a while loop.
iteration = 0
while iteration < 10:
    print('HelloWorld')
    iteration += 1

# Question 02
# Write a program that allows users to enter a positive integer n. Your program should the print numbers from 1 to n using a while loop.
number = int(input('Enter a number: '))
current_number = 1
while current_number <= number:
    print(current_number)
    current_number += 1

# Question 03
# Write a program that prints all the even numbers between -50 and 30 (inclusive) using a while loop.
current_number = -50
while current_number <= 30:
    if current_number % 2 == 0:
        print(current_number)
    current_number += 1

# Question 04
# Write a program that allows users to enter 4 positive integer and calculate the product of all numbers using a while loop.
iteration = 0
product = 1
while iteration < 4:
    number = int(input('Enter a number: '))
    product *= number
    iteration += 1
print(product)

# Question 05
# Write a program that prints the following sequence using a while loop: 1, 14, 27, 40 … 1314.
current_number = 1
while current_number <= 1314:
    print(current_number)
    current_number += 13

# Question 06
# Write a program that prints all the numbers between 1500 and 2300 (inclusive) that are divisible by both 5 and 7.
current_number = 1500
while current_number <= 2300:
    if current_number % 5 == 0 and current_number % 7 == 0:
        print(current_number)
    current_number += 1

# Question 07
# Write a program that allows users to guess a number between 1-20. If a wrong answer is entered, prompt appears again until the guess is correct. On successful guess, print 'Well guessed' and exits.
correct_answer = 19
while True:
    guess = int(input('Guess a number between 1-20: '))
    if guess == correct_answer:
        print('Well guessed!')
        break

# Question 08:
# Write a program that allows users to enter a string repeatedly until a 'quit' keyword is entered. Your program should print the number of vowels and consonents in the string.
while True:
    string = input('Enter a string: ')
    if string == 'quit':
        break
    vowels = 0
    consonents = 0
    for character in string:
        if character in 'aeiouAEIOU':
            vowels += 1
        elif character != ' ':
            consonents += 1
    print('Vowels: {0}, Consonents: {1}'.format(vowels, consonents))

# Question 09
# Write a program that allows users to enter an integer repeatedly until a 'quit' keyword is entered. Your program should sum up all the numbers entered by the user and print the result before exit.
total = 0
while True:
    string = input('Enter a string: ')
    if string == 'quit':
        print('Total: ' + str(total))
        break
    total += int(string)

# Question 10
# Write a program that allows users to enter an integer repeatedly until a 'quit' keyword is entered. Your program should print the largest number ever entered before exit.
import math
largest_number = -math.inf
while True:
    string = input('Enter a string: ')
    if string == 'quit':
        print('The largest number: ' + str(largest_number))
        break
    current_number = int(string)
    if current_number > largest_number:
        largest_number = current_number

# Question 11
# Write a program that allows users to enter a positive integer repeatedly until a 'quit' keyword is entered. Your program should check if the number is a prime number.
while True:
    string = input('Enter a string: ')
    if string == 'quit':
        break
    current_number = int(string)
    is_prime = True
    for i in range(2, current_number):
        if current_number % i == 0:
            is_prime = False
            break
    if is_prime:
        print('{0} is a prime number!'.format(current_number))
    else:
        print('{0} is not a prime number!'.format(current_number))