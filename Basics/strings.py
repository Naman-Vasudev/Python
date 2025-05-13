# Python Basics - Strings

# --------------------------------------------
# String Basics
# --------------------------------------------

# A string stores a sequence of characters.
# For multiple lines in a string, we can use escape sequence characters.

str1 = "My name is Naman Vasudev.\nI am learning Python."  # \n means new line
print(str1)

# --------------------------------------------
# String Operations
# --------------------------------------------

# Concatenation (Joining strings together)
first_name = "Naman"
last_name = "Vasudev"
print(first_name + " " + last_name)  # With space
print(first_name + last_name)        # Without space

# Using variables to store messages
message = "Hello World"
print(message)  # Correct way (not as a string literal)

# Using escape characters for special cases
print("Naman's world")  # We can use single quote inside double quotes
print('Naman\'s world')  # Using escape character

# We can also use double quotes inside a string
string = "My name is Naman Vasudev"

# --------------------------------------------
# String Length and Indexing
# --------------------------------------------

# Finding length of a string
print(len(string))  # Total number of characters

# Indexing - Position of a character in a string (starts from 0)
print(string[0])  # First character
print(string[1])  # Second character
# print(string[23])  # Uncommenting this will give an error (Index out of range)

# --------------------------------------------
# String Slicing
# --------------------------------------------

# str[starting index: ending index] (Ending index is non-inclusive)
print(string[0:5])  # First 5 characters
print(string[5:])   # From index 5 to end
print(string[6:])   # From index 6 to end

# Negative Indexing
# Starts from -len(string) to -1 (last character)
print(string[-5:])  # Last 5 characters

# --------------------------------------------
# String Formatting
# --------------------------------------------

greeting = "Hello"
name = "Naman"

# Simple concatenation
message = greeting + " " + name
print(message)

# Using .format() method
message = "{}, {}. Welcome!".format(greeting, name)
print(message)

# Using f-strings (Recommended for readability)
message = f"{greeting}, {name.upper()}. Welcome!"
print(message)