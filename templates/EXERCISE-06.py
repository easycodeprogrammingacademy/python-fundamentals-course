# Question 1
# What is the output of the program? Write your answer on a piece of 
# paper or in a textfile. Run the program to find out the correct answer.
exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(exampleList))
print(exampleList[5])
print(exampleList[1:3])
print(exampleList[4:])
print(exampleList[:2])
print(exampleList[-1])
print(exampleList[-3:-1])
print(exampleList[-5:])
print(exampleList[:-4])
print(exampleList[:])


# Question 2
# Write a program that checks if an index is out of range. If the index is 
# out of range, print “Index not found”. Otherwise do nothing. You are 
# required to use the len() method for this question.


# Question 3
# Write a program that allows users to enter an index. Your program 
# should then print the value at the specific index. If the index is out of 
# range, print “Index not found”.


# Question 4
# Write a program that allows users to enter an index and an integer
# value. Your program should then replace the element at the specific 
# index by the new value and print the new list. If the index entered is 
# out of range, print “Index not found”


# Question 5
# Write a program that allows users to enter an index and an integer 
# value. Your program should then insert the value at the specific index 
# and print the new list. If the index entered is out of range, print “Index 
# not found”. You are required to use the .insert() method for this question.


# Question 6
# Write a program that allows users to enter a string repeatedly until a 
# “quit” keyword is entered. Your program should append all the strings 
# into a list and print the list before program ends. You are required to 
# use the .append() method for this question.
# Your output should look something like this:
# >> Enter a string: Hi
# >> Enter a string: Welcome
# >> Enter a string: To
# >> Enter a string: EasyCode
# >> Enter a string: quit
# >> [“Hi”, “Welcome”, “To”, “EasyCode”]


# Question 7
# Write a program that allows users to enter an integer repeatedly until a 
# “quit” keyword is entered. Your program should append all the 
# integers into a list and print it before the program ends. You are 
# required to use the .append() method for this question. Note that the 
# elements in the list must be integer type
# Your output should look something like this:
# >> Enter an integer: 5
# >> Enter an integer: 50
# >> Enter an integer: 10
# >> Enter an integer: quit
# >> [5, 50, 10]
# >> ['5', '50', '10'] XXXXX


# Question 8
exampleList = [1, 2, 3, 4, 5, 4, 4, 4, 5]
print(exampleList.count(0))
print(exampleList.count(4))
print(sum(exampleList))
print(max(exampleList))
print(min(exampleList))

exampleList.pop(2) 
print(exampleList)

exampleList.remove(4)
print(exampleList)

exampleList.reverse()
print(exampleList)


# Question 9
# Write a program that prints all the elements in a list. You are required 
# to use for loop for this question.
# >> list -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >> Index 0 -> 1
# >> Index 1 -> 2
# …
# >> Index 9 -> 10


# Question 10
# Write a program that allows users to enter an integer value. Your 
# program should then remove all the occurances of the specific value 
# from a list. 


# Question 11
# Write a program that allows users to enter an integer value. Your 
# program should the print the number of occurance of the number in a 
# list. You are not allowed to use the .count() method for this question.


# Question 12
# Write a program that sums up all the elements in a list. You are not 
# allowed to use the sum() method for this question.


# Question 13
# Write a program to find the largest number in a list. You are not 
# allowed to use the max() method for this question.


# Question 14
# Write a program to reverse a list. You are not allowed to use 
# the .reverse() method for this question.


# Question 15
# Write a program to remove all the duplicates from a list.


# Question 16
# Write a program that iterates two lists simultaneously.
# Your output should look something like this:
# >> list1 -> [1, 2, 3, 4]
# >> list2 -> [5, 6, 7, 8, 9]
# >> Index 0 -> 1 5
# >> Index 1 -> 2 6
# >> Index 2 -> 3 7
# >> Index 3 -> 4 8
# >> Index 4 -> 9
