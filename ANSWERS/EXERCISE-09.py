import math 

# Question 01
# Write a program that prints all the rows of a nested list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for index in range(len(nested_list)):
    print(nested_list[index])

# Question 02
# Write a program that prints all the columns of a nested list. You can assume that the nested list has the same row and column count.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
columns_per_row = len(nested_list[0])
for col in range(columns_per_row):
    for row in range(len(nested_list)):
        print(nested_list[row][col], end=' ')
    print()

# Question 03
# Write a program to find the row in a nested list whose sum of elements in the row is the greatest.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3]]
largest_row_index = None
largest_row_sum = -math.inf
for index in range(len(nested_list)):
    if sum(nested_list[index]) > largest_row_sum:
        largest_row_sum = sum(nested_list[index])
        largest_row_index = index
print('Largest row: ' + str(nested_list[largest_row_index]))

# Question 04
# Write a program that convert a nested list into a flat list.
nested_list = [[1, 2, 3, 4, 5, 6], [7, 8, 9], [10]]
flat_list = []
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        flat_list.append(nested_list[i][j])
print(flat_list)

# Question 05
# Given two 3x3 matrices (nested list), write a program to add them together and print the resulting matrix.
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
resulting_matrix = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(3):
    for j in range(3):
        resulting_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
print(resulting_matrix)

# Question 06
# Write a program to calculate and print the sum of diagonal elements of a 4x4 matrix.
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
diagonal_sum = 0
for i in range(4):
    diagonal_sum += matrix[i][i]
for i in range(4):
    diagonal_sum += matrix[i][3 - i]
print(diagonal_sum)

# Question 07 
# Given a string, write a program to count the number of words in it. Words are separated by spaces.
sentence = 'this is an example sentence'
words_list = sentence.split()
number_of_words = len(words_list)
print(number_of_words)

# Question 08
# Given a string containing numbers separated by commas and possibly spaces, extract all numbers and print them as a list of integers. For example
# a. Input: '1, 2,  3, 4 ,   5,6, 7   '
# b. Output: [1, 2, 3, 4, 5, 6, 7]
example_string = '1, 2,  3, 4 ,   5,6, 7   '
number_list = example_string.split(",")
print(number_list)
for index in range(len(number_list)):
    number_list[index] = int(number_list[index].strip())
print(number_list)

# Question 09
# Given a string with extra spaces at the beginning, end and between words, remove the extra spaces and print the cleaned string.
# a. Input: '    This   is    a    string   with extra   spaces'
# b. Output: 'This is a string with extra spaces'
example_string = '    This   is    a    string   with extra   spaces'
words_list = example_string.split()
cleaned_string = ''
for index in range(len(words_list)):
    cleaned_string += words_list[index]
    if index != len(words_list) - 1:
        cleaned_string += " "
print(cleaned_string)
