# ------------------------------------------------------
# LIST COMPREHENSION IN PYTHON
# ------------------------------------------------------

# List comprehensions provide a concise way to create lists.
# It is more readable and compact compared to using traditional loops.

# ------------------------------------------------------
# SYNTAX:
# new_list = [expression(item) for item in iterable if condition]
#
# - expression: What to do with each item (like modify or keep as is)
# - iterable: Any iterable like list, tuple, set, string, etc.
# - condition: Optional; filter to include items based on logic
# ------------------------------------------------------

# ------------------------------------------------------
# Example 1: Filter names that contain the letter 'o'
# ------------------------------------------------------
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]

# Create a new list with only names containing 'o'
names_with_o = [name for name in names if "o" in name]
print("Names with 'o':", names_with_o)
# Output: ['Milo', 'Bruno', 'Rosa']

# ------------------------------------------------------
# Example 2: Filter names with more than 4 letters
# ------------------------------------------------------
# Create a new list with names longer than 4 characters
long_names = [name for name in names if len(name) > 4]
print("Names longer than 4 letters:", long_names)
# Output: ['Sarah', 'Bruno', 'Anastasia']

# ------------------------------------------------------
# BONUS: You can also apply expressions to transform items
# ------------------------------------------------------
# Example: Convert all names to uppercase
upper_names = [name.upper() for name in names]
print("Uppercase names:", upper_names)
# Output: ['MILO', 'SARAH', 'BRUNO', 'ANASTASIA', 'ROSA']

# ------------------------------------------------------
# Example with numbers: Square of even numbers in a range
# ------------------------------------------------------
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of even numbers from 0 to 9:", even_squares)
# Output: [0, 4, 16, 36, 64]