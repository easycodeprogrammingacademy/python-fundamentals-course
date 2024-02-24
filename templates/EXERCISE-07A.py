# Question1
numlist = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]
print(numlist)
print(len(numlist))
print(len(numlist[2]))
print(numlist[1]) 
print(numlist[1][0]) 
print(numlist[0][-1])
print(numlist[2][1:])

numlist.append(10) 
print(numlist) 

numlist.append([11, 12])
print(numlist)
print(len(numlist))

numlist[0].append(4)
print(numlist)

numlist[1][1] = 100
print(numlist)

numlist.pop(-1)
print(numlist)


# Question 2
# Write a program that allows users to enter a row count value (n) and a 
# column count value (m). Your program should then create a two 
# dimensional list of size n x m and initialize all the elements to zero.


# Question 3
# Write a program that prints all the rows of a nested list.


# Question 4
# Write a program that loops through a nested list and print all the 
# elements in the sublists along with its row and column index.


# Question 5
# Write a program that prints all the columns of a nested list. You can 
# assume the nested list has the same row and column count.


# Question 6
# Write a program that allows users to enter two positive integer values 
# – row index and column index. If the index is out of range, print 
# “Index not found”. If it is not, asks for an integer value. Your program 
# should then replace the element at the specific row and column index 
# by the new integer.


# Question 7
# Write a program to find the list in a nested list whose sum of elements 
# is the greatest. You are not allowed to use the sum() method for this 
# question.
# 1 2 3 -> 6
# 4 5 6 -> 15
# 7 8 9 -> 24

# Question 8
# Write a program that convert a nested list into a flat list.
# [[1, 2, 3], [4, 5]] --> [1, 2, 3, 4, 5]
