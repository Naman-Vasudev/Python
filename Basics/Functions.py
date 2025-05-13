# --------------------------------------------
# Python Functions: Reusable Code Blocks
# --------------------------------------------

# Function Syntax:
# def function_name(parameter1, parameter2, ...):
#     # Function body
#     return value
# function_name(argument1, argument2, ...)  # Function call

# --------------------------------------------
# Function with Parameters and Return Value
# --------------------------------------------

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add_numbers(2, 3))  # Output: 5

# --------------------------------------------
# Function Without Return Value (prints directly)
# --------------------------------------------

def print_hello():
    """Prints 'Hello' (no return value)."""
    print("Hello")

output = print_hello()  # Calls the function
print(output)  # Output: None (since function has no return statement)

# --------------------------------------------
# Changing Default Behavior of print()
# --------------------------------------------

print("My name is")  # By default, `end` is '\n'
print("My name is ", end="separator")  # Changing end behavior
print(" Next line starts here.")

# --------------------------------------------
# Using 'pass' in a Function
# --------------------------------------------

def placeholder_function():
    """A function that does nothing yet."""
    pass  # Used when we need to define a function but don't want it to do anything now

# Calling an empty function
print(placeholder_function())  # Output: None
