# ========================================================
# Python Map Function - Taking Space-Separated Input as List
# ========================================================

# -----------------------------------------------
# Overview of map() function:
# -----------------------------------------------
# The map() function applies a given function to each item of an iterable (like a list or tuple)
# and returns an iterator. You can convert it to a list using the list() function.
#
# Syntax:
# map(function, iterable)

# Example function: int() to convert input to integers.

# -----------------------------------------------
# Step 1: Take Space-Separated Input
# -----------------------------------------------
# Prompt the user to input a list of numbers separated by spaces.
input_string = input("Enter numbers (space-separated): ")

# -----------------------------------------------
# Step 2: Split the Input String
# -----------------------------------------------
# The input string is split into individual components using the split() method.
# This returns a list of strings where each number is a string.
input_list = input_string.split()

# Example:
# Input: "1 2 3 4 5"
# After split: ['1', '2', '3', '4', '5']

# -----------------------------------------------
# Step 3: Use map() to Convert Strings to Integers
# -----------------------------------------------
# The map() function is used to apply the int() function to each element of the input_list.
# This will convert each string to its integer equivalent.
output_list = list(map(int, input_list))

# Example:
# ['1', '2', '3', '4', '5'] becomes [1, 2, 3, 4, 5]

# -----------------------------------------------
# Step 4: Display the Output
# -----------------------------------------------
# The result is printed as a list of integers.
print("Converted list:", output_list)

# -----------------------------------------------
# Type of the Output:
# -----------------------------------------------
# The type of the output list will be <class 'list'>.
# This is because map() returns an iterator, and list() converts it into a proper list.
print("Type of output_list:", type(output_list))
# Expected Output: <class 'list'>

# -----------------------------------------------
# Summary:
# -----------------------------------------------
# - We used the map() function to convert each space-separated input string into an integer.
# - The list() function was used to convert the map object into a list for easy access.
# - This approach is clean and avoids explicit loops for processing each item.