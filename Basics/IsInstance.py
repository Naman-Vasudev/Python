# ==========================================================
# Python isinstance() Function Notes
# ==========================================================
# The isinstance() function is a built-in Python function
# that checks if an element belongs to a specific class or type.
# It returns a boolean value: True if the object is an instance of 
# the specified class, and False otherwise.

# Syntax:
# isinstance(object, classinfo)

# - object: The object whose type you want to check.
# - classinfo: The class, type, or a tuple of classes and types to check against.

# Example of usage:

# -----------------------------------------------
# Step 1: Define variables of different types
# -----------------------------------------------

# Example 1: List of strings
a = ['Jay', 'Eva', 'Nathaniel', 'Elisha']

# Example 2: Tuple of strings
b = ('a', 'b', 'c', 'd')

# Example 3: Dictionary of integers
c = {1: 'apple', 2: 'banana', 3: 'cherry'}

# -----------------------------------------------
# Step 2: Use isinstance() to Check Object Types
# -----------------------------------------------

# Check if 'a' is a list
print(isinstance(a, list))  # Expected output: True

# Check if 'b' is a tuple
print(isinstance(b, tuple))  # Expected output: True

# Check if 'c' is a dictionary
print(isinstance(c, dict))  # Expected output: True

# -----------------------------------------------
# Additional Example: Checking with wrong types
# -----------------------------------------------

# Check if 'a' is an instance of a tuple (should return False)
print(isinstance(a, tuple))  # Expected output: False

# Check if 'c' is an instance of a list (should return False)
print(isinstance(c, list))  # Expected output: False

# -----------------------------------------------
# Explanation of Output:
# -----------------------------------------------

# - isinstance(a, list) returns True because 'a' is a list.
# - isinstance(b, tuple) returns True because 'b' is a tuple.
# - isinstance(c, dict) returns True because 'c' is a dictionary.

# When checked with incorrect types:
# - isinstance(a, tuple) returns False because 'a' is not a tuple.
# - isinstance(c, list) returns False because 'c' is not a list.

# -----------------------------------------------
# Summary:
# -----------------------------------------------
# The isinstance() function is useful to verify the type of an object.
# It can be used for:
# - Checking if an object is an instance of a specific class.
# - Ensuring type safety by validating types before performing operations.
