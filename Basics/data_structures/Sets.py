# Python Basics - Sets
# --------------------------------------------

# Sets are unordered collections of unique and immutable elements.
# They do not allow duplicate values and are mutable themselves.

# --------------------------------------------
# Defining a Set

numbers = {1, 2, 3, 4}  # A set with unique numbers
print(numbers)  # Output: {1, 2, 3, 4}

# Duplicate elements are ignored in sets
set_with_duplicates = {1, 2, 2, 2, 3}
print(set_with_duplicates)  # Output: {1, 2, 3}

# --------------------------------------------
# Creating an Empty Set
# --------------------------------------------

empty_dict = {}  # ⚠️ This creates an empty dictionary, NOT a set
empty_set = set()  # ✅ Correct way to create an empty set
print(empty_set)  # Output: set()