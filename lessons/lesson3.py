# All about strings

# What is a string?
# A string is a sequence of characters. It can be defined with either a single
# or double quotes
# single quotes
alpha = 'Hello'

# double quotes
beta = "Python"

# print results
print(alpha)
print(beta)

# A multi-line string uses three single or three double quotes and allows
# a string to be created on multiple lines.
multi = '''this string can be seen
on multiple lines so you could do 
paragraphs if you wanted'''
print(multi)

# getting a specific index using the square bracket []
charlie = 'happy'
print(charlie[2])

# if you put in a value of the index that is higher than the number of
# characters -1 will generate an error
# print(charlie[5])

# slicing and range of characters
# using the same square, you can output a range of characters
# from a string. This is called slicing. You use a colon to seperate the
# start and end of slice.
delta = 'Enjoy Python'
print(delta[2:5])
# output should be joy

# negative slicing we use negative numbers. Instead of starting from zero
# it begins at the end of the string
print(delta[-5:-2])
# output should be yth

# what is check string
# This is techniqie is the ability to compare a set of characters with a string
# variable. This result will either be True or False. We use in or not it
# using the in keyword
txt = 'This is a test sentence'
result1 = 'is' in txt

# using the not in keyword
txt2 = 'This other phrase is also a test'
result2 = 'th' not in txt2

print(result1)
print(result2)


# string concatenation in Python is the ability to join 2 or more strings
# using the plus operator
# Basic Concatenation
cat1 = "Happy"
cat2 = "Friday"
combine = cat1 + cat2
print(combine)
combine2 = cat1 + " " + cat2
print(combine2)

cat3 = 'sample'
combine3 = cat3 + ' Code '
print(combine3)

# longer concatenation with more than 2 values
combine4 = cat1 + '' + cat2 + ' ' + combine3
print(combine4)

# what about strings and a number
# combine5 = cat3 + 5
# print(combine5)

# basic string format method using only a curly brace
age = 4
msg1 = 'My dog is {} years old'
print(msg1.format(age))

# string format using indexing
msg2 = 'My dog {1} is {0} years old'
print(msg2.format(age, 'Spot'))

# Optional format
name = 'John'
total = 34.9856
msg3 = 'Hello {0}, your order comes to {1:6.2f}'
print(msg3.format(name, total))

# octal escape sequence '\110\145\154\154\157'
value_0 = '\110\145\154\157'
print(value_0)

# Escape Sequence allows you to use some characters that are reserved using
# a backslash
value_more = 'that\'s a cool toy. \tcan I\n play with it?'
print(value_more)

# string methods are methods built in to python
value_string = ' Hello, World '

# strip()
print(value_string.strip())

#lower()
print(value_string.lower())

# upper()
print(value_string.upper())

#replace()
print(value_string.replace('e', 'a'))

# split()
print(value_string.split(','))

value_more = 'hello python'

# capitalize()
print(value_more.capitalize())

value_upper = 'PYTHON'

# casefold()
print(value_upper.casefold())

# centered()
print(value_more.center(40))
