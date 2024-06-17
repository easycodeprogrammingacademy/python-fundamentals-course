# Question 01
# Write a program that allows users to enter two integer values. If the numbers are equal, print 'The numbers are equal'; otherwise, do nothing.
num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter another number: '))
if num_1 == num_2:
    print('The numbers are equal')

# Question 02
# Write a program that allows users to enter an integer value. If the number is even, print 'Even'; otherwise, print 'Odd'.
num = int(input('Enter a number'))
if num % 2 == 0:
    print('Even')
else:
    print('Odd')

# Question 03
# Write a program that allows users to enter an integer value and checks if the number is zero, positive or negative.
num = int(input('Enter a number: '))
if num > 0:
    print('Positive')
elif num < 0:
    print('Negative')
else:
    print("Zero")

# Question 04
# Write a program that allows users to enter an integer value and checks if the value is divisible by 5.
num = int(input('Enter a number: '))
if num % 5 == 0:
    print('The number is divisibly by 5!')

# Question 05
# Write a program that checks if a year is a leap year. A year is a leap year if one of the following conditions is satisfied.
# a. The year is a multiple of 400
# b. The year is a multiple of 4 and not multiple of 100
year = int(input('Enter a year: '))
condition_1 = year % 400 == 0
condition_2 = year % 4 == 0 and not year % 100 != 0
is_leap_year = condition_1 or condition_2
print(str(year) + ' is a leap year: ' + str(is_leap_year))

# Question 06
# Write a program that finds the largest of three numbers.
num1, num2, num3 = 10, 20, 30
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# Question 07
# Write a program that allows users to enter their exam score. If the score is
# a. Less than 40% -> print 'You failed your exam'
# b. Between 40% and 69% -> print 'You pass your exam'
# c. Between 70% and 79% -> print 'Not bad, try harder'
# d. Between 80% and 89% -> print 'You scored an A'
# e. Between 90% and 100% -> print 'Excellent score'
# f. Otherwise -> print 'I don't understand'
score = int(input('Enter your score: '))
if score >= 90 and score <= 100:
    print('Excellent score!')
elif score >= 80 and score < 90:
    print('You scored an A')
elif score >= 70 and score < 80:
    print('Not bad, try harder')
elif score >= 40 and score < 70:
    print('You pass your exam')
elif score >= 0 and score < 40:
    print('You failed your exam')
else:
    print('I dont understand!')

# Question 08
# Write a program that checks if a string contains the substring 'hello'.
string = input('Enter a string: ')
if 'hello' in string:
    print('The string contains substring "hello"')
else:
    print('The string does not contain substring "hello"!')

# Question 09
# Write a program that allows users to enter a character and checks if the character is a vowel or consonant.
character = input('Enter a character: ')
if character in 'aeiouAEIOU':
    print('The character is a vowel')
else:
    print('The character is a consonent')

# Question 10
# Write a program that checks if a person is eligible for a library membership. A person is eligible if they are 18 years old or older and have an ID.
age = 20
has_id = True
if age >= 18 and has_id:
    print('Eligible for library membership')
else:
    print('Not eligible')

# Question 11
# Write a program that allows users to input a date. Your program should then print the date of the next day. Note that your program should take leap years into consideration.
current_day = int(input('Enter current day: '))
current_month = int(input('Enter current month: '))
current_year = int(input('Enter current year: '))
is_leap_year = current_year % 400 == 0 or (current_year % 4 == 0 and not current_year % 100 != 0)

next_day, next_month, next_year = -1, -1, -1

month_has_30_days = current_month == 4 or current_month == 6 or current_month == 9 or current_month == 11
if month_has_30_days:
    if current_day <= 29:
        next_day = current_day + 1
        next_month = current_month
        next_year = current_year
    else:
        next_day = 1
        next_month = current_month + 1
        next_year = current_year
elif current_month == 2:
    next_year = current_year
    if current_day <= 27 or (current_day == 28 and is_leap_year):
        next_day = current_day + 1
        next_month = current_month
    elif current_day == 28 or current_day == 29 :
        next_day = 1
        next_month = 3
else:
    if current_day <= 30:
        next_day = current_day + 1
        next_month = current_month
        next_year = current_year
    elif current_month == 12:
        next_day = 1
        next_month = 1
        next_year = current_year + 1
    else:
        next_day = 1
        next_month = current_month + 1
        next_year = current_year

print('The date of next day is {0}/{1}/{2}'.format(next_day, next_month, next_year))