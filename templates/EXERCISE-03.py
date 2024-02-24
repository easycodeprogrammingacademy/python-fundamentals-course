# Question 1
# Write a program that allows users to enter two integers value. If the 
# numbers are equal, print “The numbers are the same”. Otherwise, do nothing


# Question 2
# Write a program that allows users to enter an integer value. If the 
# number entered is 7, print "It is the lucky number”. Otherwise, print “Aww bad guess”.


# Question 3 
# Write a program that allows users to enter an integer value between 0 
# and 9. Your program should then print the English word of the integer.


# Question 4
# Write a program that allows users to enter a colour of traffic light
# (Green, Yellow, Red). If the colour is green, print “Go ahead”. 
# Otherwise, print "Stop your vehicle”.
# Green/green/GreeN -> Go ahead
# Yellow/YELLOW/Red -> Stop your vehicle


# Question 5
# Write a program that allows users to enter their exam score. If the 
# score is
# • Less than 40 → print “You failed your exam”
# • Greater than or equal to 40 → print “You pass your exam”
# • Greater than or equal to 70 → print “Not bad. Try harder”
# • Greater than or equal to 80 → print “Wow you scored an A”
# • Greater than or equal to 90 → print “Excellent score”
# • Others → print “I don’t understand”


# Question 6 (nested if)
# Write a program that allows users to enter 3 integer values. Your 
# program should then check whether the values are all the same or any 
# of the two are equal or all are different.


# Question 7
# Write a program that allows users to enter a positive integer. If the 
# number is
# • A multiple of 2 and a multiple of 3 → print “Divisible by 2 and 3”
# • A multiple of 2 or a multiple of 3 → print “Divisible by 2 or 3”
# • Otherwise → print “Not divisible by 2 and 3”


# Question 8
# McDonald’s now offers a special promotion. If a red tag item and a blue 
# tag item are purchased at the same time, there will be a discount. 
# Write a program that allows users to choose their food and drink. Your 
# program should then check if the user can receive a discount. Your 
# function should ignore the capitalization of the string.
# Beef Burger Coca-Cola
# Bacon Wrap Lemon Tea


# Question 9
# Write a program that allows users to enter a new password. Your 
# program should check if the new password fullfills the requirements. 
# Validation includes
# • A minimum length of 6 characters
# • A maximum length of 16 characters
# • Must include at least 1 special character – (#$@)


# Question 10
# Write a program to check if a year is a leap year. A leap year occurs 
# once every 4 years and has 366 days including 29 February as an 
# intercalary day. A year is a leap year if one of the following conditions 
# are satisfied:
# • The year is a multiple of 400
# • The year is multiple of 4 and not multiple of 100


# Question 11
# Write a program that allows users to input a date. Your program 
# should then print the date of the next day of the given date. Note that 
# you need to take leap year into consideration.

# 1. month-> 1/3/5/7/8/10/12 (31 days)
#       day -> (<=30) -> day+1, month and year 不变
#       day -> (31) -> day=1
#            -> month = 12 -> month=1, year+1
#            -> month != 12 -> month+1, year 不变
# 2. month -> 4/6/9/11 (30 days)
#       day -> (<= 29) -> day+1, month and year 不变
#       day -> (30) -> day=1, month+1, year 不变
# 3. month -> 2
#       day -> (<=27) -> day+1, month and year 不变
#       day -> (28) -> leapyear -> 29 // not leap year --> day=1, month=3, year 不变
#       day -> (29) -> day=1, month=3, year 不变