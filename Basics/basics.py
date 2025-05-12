# Python Basics - Lecture 1 Notes

# --------------------------------------------
# Variable Declaration and Data Types
# --------------------------------------------

name = 'Naman'   # String
price = 19.77    # Float
age = 23         # Integer
is_old = False   # Boolean
value = None     # NoneType

# Checking the type of variables
print(type(name))   # Output: <class 'str'>  
print(type(is_old)) # Output: <class 'bool'>
print(type(value))  # Output: <class 'NoneType'>

# --------------------------------------------
# Type Conversion and Type Casting
# --------------------------------------------

# Type Conversion (Automatic conversion)
num1 = 2    # Integer
num2 = 4.25 # Float
result = num1 + num2  # Automatically converts '2' to float
print(result)  # Output: 6.25

# Type Casting (Forced conversion)
str_num = "2"
int_num = int(str_num)  # Typecasting string to integer
print(num2 + int_num)   # Output: 6.25

# --------------------------------------------
# Input in Python
# --------------------------------------------

# input() -> Always takes input as a string by default
# int(input()) -> Converts input string to an integer

# Program to take two numbers as input and print their sum
num1 = int(input("Enter the first number: "))  # Taking first number as input
num2 = int(input("Enter the second number: ")) # Taking second number as input
print("The sum of the two numbers is:", num1 + num2)  # Printing the sum

# --------------------------------------------
# Mathematical Operations
# --------------------------------------------

# Basic arithmetic operations
print(3 / 2)   # Division (Result: 1.5)
print(3 // 2)  # Floor division (Quotient: 1)
print(3 ** 2)  # Exponentiation (3 raised to the power 2 = 9)
print(3 % 2)   # Modulus (Remainder: 1)

# Other useful math functions
print(abs(-7/2))        # Absolute value (Result: 3.5)
print(round(4.9999999)) # Round off to the nearest integer (Result: 5)

# Rounding to specific decimal places
print(round(45.654, 1))  # Round to 1 decimal place (Result: 45.7)

#Getting the output at fixed decimal places
x = int(input("Enter the number of decimal places: "))
number = float(input("Enter the number: "))
print(f"{number:.{x}f}")


# --------------------------------------------
# Comparison Operators
# --------------------------------------------

num_1 = 3
num_2 = 2

print(num_1 == num_2)  # Equality check (False)
print(num_1 != num_2)  # Inequality check (True)