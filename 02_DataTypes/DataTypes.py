# Data Types in Python
# integers - Whole numbers such as 1, 2, 3, -4, 0, etc.
# float - Decimal numbers such as 1.5, -0.2, 100.0, etc.
# complex - Numbers with a real and imaginary part, e.g., 3 + 4j, 5 - 2j, etc.
# boolean - True or False values
# string - Sequence of characters enclosed in quotes, e.g., "Hello", 'Python', "2000", " I'm going on run"etc.
# list - Ordered collection of items, e.g., [10, 'apple', "banana", 200.3], etc. or ordered sequences of objects.
# tuple - Ordered, immutable collection/sequence of items, e.g., [10, 'apple', "banana", 200.3], etc.
# dictionary - Collection of unordered key:value pairs, e.g., {'name': 'John', "name" : "vijay", 'age': 30}, etc.
# set - Unordered collection of unique items, e.g., {1, 2, 3}, {'apple', "banana"}, etc.

# Arithmetic Operators in Python:
print (21+29)       # Addition operator gives sum   
print (21*29)       # Multiplication operator gives product
print (21/29)       # Division operator gives quotient
print (21-29)       # Subtraction operator gives difference
print (21//29)      # Floor division operator gives integer quotient
print (7 % 4)       # Modulus operator gives remainder
print (2 ** 3)      # Exponentiation operator gives power
print (2+10*20-3)   # Operator precedence
print (2+ (10*20) +3)  # Using parentheses to change precedence
print (2+10*20+3)   # Without parentheses
print ( (2+10) * (20-3) )  # Using parentheses to change precedence
print (7 % 4 + 3 * 2 - 1)  # Combined operations

# variables in Python:
#Rules for variable names:
#1. Variable names must start with a letter (a-z, A-Z) and there can be no space in the name, useunderscore (_) instead.
#2. The rest of the variable name can contain letters, digits (0-9), or underscores (_).
#3. Variable names are case-sensitive (e.g., myVar and myvar are different), better to consider best practice that names are lowercase.
#4. Variable names cannot be the same as Python reserved keywords (e.g., if, else, while, for, list, str, etc.).
#5. can't use any special characters/symbols like !, @, #, $, %, (), etc. in variable names.
#6. python uses dynamic typing, this means you can reassign variables to different data types.
my_dogs = 2     # integer variable 
my_dogs = ["Buddy", "Frankie"]  # list variable
print(my_dogs)

a=5
print(a)

print (a+a)

a=a+a
print(a)

type (a)   # to check the data type of variable 'a'
print (type(a))

a = "Hello"
print (type(a))

a = 3.14
print (type(a))

a = 2 + 3j
print (type(a))

a = True
print (type(a))

my_income = 1300000
tax_rate = 0.20
my_taxes = my_income * tax_rate
print(my_taxes)

# srings:
# strings are sequence of characters using the syntax of either single quotes or double quotes.
# eg: 'hello', "python", '2000', "It's a sunny day", etc.
# strings rae ordered sequences of characters, means we can using indexing and slicing to grab sub-sections of the string.
# indexing notation uses square brackets [] to access individual characters in the string.
# indexing starts at 0 for the first character, 1 for the second character, and so on.
# negative indexing starts at -1 for the last character, -2 for the second last character, and so on.
    #Eg:-  Charater:    h   e   l   l   o
    #      Index:       0   1   2   3   4
    # Reverse Index:    0  -4  -3  -2  -1       
# slicing notation uses the colon : inside the square brackets to grab a range of characters from the string.
# syntax for slicing is [start:stop:step], where start is the starting index (inclusive), stop is the ending index (exclusive), and step is the increment between indices (default is 1).
# String examples:  
print("Hello World")          # double quotes
print('Hello World')          # single quotes
print("It's a sunny day")     # single quote inside double quotes
print('He said, "Hello!"')    # double quotes inside single quotes   
print("Hello" + " " + "World")  # string concatenation
print("Hello " * 3)           # string repetition
my_string = "Hello World"
print(my_string)              # printing the string variable 
print(my_string[0])           # first character
print(my_string[4])           # fifth character
print(my_string[-1])          # last character
print(my_string[-5])          # fifth last character
print(my_string[0:5])        # slicing from index 0 to 4
print(my_string[6:11])       # slicing from index 6 to 10
print(my_string[:5])         # slicing from start to index 4
print(my_string[6:])         # slicing from index 6 to end
print(my_string[::2])        # slicing with step of 2
print(my_string[::-1])       # reversing the string 
print( 'hello \n world' )   # new line escape sequence
print( 'hello \t world' )   # tab escape sequence
print( 'hello \\ world' )   # backslash escape sequence
print( 'He said, \"Hello!\"' )  # double quotes escape sequence
print( 'It\'s a sunny day' )    # single quote escape sequence  
print(len(my_string))          # length of the string
print(my_string.upper())       # convert to uppercase
print(my_string.lower())       # convert to lowercase
print(my_string.split())       # split string into list of words
print(my_string.replace("World", "Python"))  # replace substring 
print(len("python programming"))  # length of another string
print(len('I am learning Python!'))  # length of another string

# Srings are immutable, means we cannot change individual characters in the string directly.
# 