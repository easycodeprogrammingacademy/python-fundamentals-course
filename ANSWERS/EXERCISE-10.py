# Question 01
# Write a function `find_max(num1, num2, num3)` that takes 3 integers and prints the largest value.
def find_max(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

# Question 02
# Write a function `factorial(n)` that takes an non-negative integer `n` and prints its factorial.
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    print(result)

# Question 03
# Write a function `sum_of_list(lst)` that takes a list of integers and returns the sum of all the integers in the list.
def sum_of_list(lst):
    total = 0
    for number in lst:
        total += number
    return total

# Question 04
# Write a function `count_occurances(lst, x)` that takes a list and an element `x` and returns the number of times `x` appears.
def count_occurances(lst, x)
    occurance = 0
    for element in lst:
        if element == x:
            occurance += 1
    return occurance

# Question 05
# Write a function `reverse_string(s)` that takes a string `s` and returns the reversed string.
def reverse_string(s):
    reversed_string = ""
    for index in range(-1, -len(s) - 1, -1):
        reversed_string += s[index]
    return reversed_string

# Question 06
# Write a function `list_intersection(lst1, lst2)` that takes two lists and returns a new list that contains only the elements that are common to both lists.
def list_intersection(lst1, lst2):
    intersection = []
    for element in lst1:
        if element in lst2 and element not in intersection:
            intersection.append(element)
    return intersection

# Question 07
# Write a function `is_prime(n)` that takes an integer `n` and returns True if `n` is a prime number and False otherwise.
def is_prime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Question 08
# Write a function `list_of_primes(n)` that takes an integer `n` and returns a list of prime numbers up to `n`.
def list_of_primes(n):
    prime_numbers = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

# Question 09
# Write a function `greet` that takes an optional string argument `name` and prints 'Hello, `name`!'
def greet(name='Guest'):
    print('Hello ' + name)

# Question 10
# Write a function `alphabet_counter(s)` that takes a string `s` and prints the number of occurance for each alphabet. 
def alphabet_counter(s):
    counters = [0] * 26
    lower_s = s.lower()
    for character in lower_s:
        if ord(character) >= 97 and ord(character) <= 122:
            index = ord(character) - 97
            counters[index] += 1
    print(counters)
    for index in range(26):
        if counters[index] != 0:
            print('{0} appears {1} times'.format(chr(index+97), counters[index]))
