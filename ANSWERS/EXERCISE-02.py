# Question 01
# Create a variable called 'greeting' and assign it the string 'Hello, World!' and finally print the string.
greeting = 'Hello, World!'
print(greeting)

# Question 02
# Concatenate the strings 'Python' and 'Programming' and store the result in a variable called 'full_string'.
full_string = 'Python' + ' ' + 'Programming'
print(full_string)

# Question 03
# Repeat the string 'Hello' 3 times and store the result in a variable called 'repeated_greeting'
repeated_greeting = 'Hello' * 3
print(repeated_greeting)

# Question 04
# Create a string that contains a tab character between the words 'Hello' and 'World'.
greeting_with_tab = 'Hello\tWorld'
print(greeting_with_tab)

# Question 05
# Create a string that contains a newline characters between two sentences – 'Hello' and 'How are you?'
greeting_with_newline = 'Hello' + '\n' + 'How are you?'
print(greeting_with_newline)

# Question 06
# Convert the integer 123 and float '45.67' to a string and store it in a variable called 'num_str' and 'float_str' respectively.
num_str = str(123)
float_str = str(45.67)

# Question 07
# Create a variable named 'temperature' and assign it a value of integer 25. Then concatenate the variable with the string 'The temperature outside is (temperaure) degrees Celcius.'
temperature = 25
temperature_str = str(temperature)
combined_str = 'The temperature outside is ' + temperature_str + ' degrees Celcius'
print(combined_str) 

# Question 08
# Convert the string 'I LOVE PYTHON' to all lowercase and store it in a variable called 'lower_str'.
lower_str = 'I LOVE PYTHON'.lower()
print(lower_str)

# Question 09
# Convert the string 'welcome to easycode' to all uppercase and store it in a variable called 'upper_str'.
upper_str = 'welcome to easycode'.upper()
print(upper_str)

# Question 10
# Count the number of occurances of the letter 'o' in the string 'hello world' and store the result in a variable called 'o_count'.
o_count = 'hello world'.count('o')
print('Number of occurance of letter o: ' + str(o_count))

# Question 11
# Replace all the occurances of the word 'hello' with 'hi' in the string 'hello world' and store the result in a variable called 'replaced_str'.
replaced_str = 'hello world'.replace('hello', 'hi')
print(replaced_str)

# Question 12
# Replace the first two occurrences of the letter 'l' with 'x' in the string 'hello world' and store the result in a variable called 'replaced_str_count'.
replaced_str_count = 'hello world'.replace('l', 'x', 2)
print(replaced_str_count)

# Question 13
# Create a variable name called sentence and assign it the string 'Hello Welcome To Easycode'. Find the number of vowels and consonents in the string.
sentence = 'Hello Welcome To Easycode'
lower_sentence = sentence.lower()
vowels = lower_sentence.count('a') + lower_sentence.count('e') + lower_sentence.count('i') + lower_sentence.count('o') + lower_sentence.count('u')
consonents = len(sentence) - sentence.count(' ') - vowels
print('Vowels: ' + str(vowels))
print('Consonents: ' + str(consonents))
