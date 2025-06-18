# ========================================================
# Python Map Function - Notes with Examples and Output
# ========================================================

# -----------------------------------------------
# The map() function in Python
# -----------------------------------------------
# map(function, iterable)
# - Takes a function and an iterable (like list, tuple)
# - Applies the function to each element of the iterable
# - Returns a 'map object' (which is an iterator)

# Sample input list
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to double a number
def doubler(number):
    return number * 2

# Apply the function using map
output = map(doubler, num)

# Check the type of 'output'
print("Type of output:", type(output))
# Output: <class 'map'>
# This means 'output' is a map object (not a list yet).

# -----------------------------------------------
# Converting map object to a list
# -----------------------------------------------
# Since map returns an iterator, we use list() to get all values
# This is needed because iterators do not print all values directly
doubled_list = list(output)
print("Mapped (doubled) output as list:", doubled_list)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# -----------------------------------------------
# Advantages of map():
# - Cleaner syntax, avoids explicit loops
# - More efficient for large data sets
# - Commonly used in functional programming

# -----------------------------------------------
# Summary:
# - Use map when you want to apply a function to each item
# - Convert to list or use a loop to access the output
