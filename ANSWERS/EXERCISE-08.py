# Question 01
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

# Question 02
# Write a program to check if an index is out of range.
exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
if index >= len(exampleList):
    print('The index is out of range!')

# Question 03
# Write a program that allows users to enter a string repeatedly until a 'quit' keyword is entered. Your program should append all the strings into a list and print it before exit. 
output_list_str = []
while True:
    string = input('Enter a string: ')
    if string == 'quit':
        print('Output List: ' + str(output_list_str))
        break
    output_list_str.append(string)

# Question 04
# Write a program that allows users to enter an integer repeatedly until a 'quit' keyword is entered. Your program should append all the integers into a list and print it before exit. Note that the elements in the list must be in integer type.
output_list_int = []
while True:
    string = input('Enter an integer: ')
    if string == 'quit':
        print('Output List: ' + str(output_list_int))
        break
    output_list_int.append(int(string))

# Question 05
# Write a program to sum all the items in a list.
exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_easy = sum(exampleList)
total_hard = 0
for nunber in exampleList:
    total_hard += number
print(total_easy, total_hard)

# Question 06
# Write a program to get the largest and smallest number from a list.
exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_number = min(exampleList)
max_number = max(exampleList)
print(min_number, max_number)

# Question 07
# Write a program to remove duplicates from a list.
exampleList = [1, 2, 4, 3, 1, 6, 1, 1, 4, 5, 6, 'a', 'b', 'a']
filtered_list = []
for element in exampleList:
    if element not in exampleList:
        exampleList.append(element)
print(filtered_list)

# Question 08
# Write a program that allows users to enter an integer. Your program should print the number of occurance of the integer in the list without using the count() method.
exampleList = [1, 2, 4, 3, 1, 6, 1, 1, 4, 5, 6]
number = int(input('Enter a number: '))
easyOccurance = exampleList.count(number)
occurance = 0
for element in exampleList:
    if element == number:
        occurance += 1
print('Number of occurance: ' + str(occurance))

# Question 09
# Write a program that finds the indexes of all even number in a list.
exampleList = [1, 2, 4, 3, 1, 6, 1, 1, 4, 5, 6]
even_number_indexes = []
for index in range(len(exampleList)):
    if exampleList[index] % 2 == 0:
        even_number_indexes.append(index)
print('Indexes of even numbers: ' + str(even_number_indexes))

# Question 10
# Write a program to reverse a list without using the reverse() method.
exampleList = [1, 2, 4, 3, 1, 6, 1, 1, 4, 5, 6]
# Using .insert()
reversed_list = []
for element in exampleList:
    reversed_list.insert(0, element)
print(reversed_list)

# Using negative index and .append()
reversed_list = []
for index in range(-1, -len(exampleList) - 1, -1):
    reversed_list.append(exampleList[index])
print(reversed_list)

# Question 11
# Write a program to count the number of strings in a list that meets the following condition:
# a. The length of string is greater or equal to 2
# b. The first and last characters are the same
exampleList = ['hello', 'world', 'test', 'example', 'aa']
occurance = 0
for index in range(len(exampleList)):
    if len(exampleList[index]) >= 2:
        if exampleList[index][0] == exampleList[index][-1]:
            occurance += 1
print('Number of occurance: ' + str(occurance))
