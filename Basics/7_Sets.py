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

# --------------------------------------------
# Basic Set Operations
# --------------------------------------------

cs_courses = {'History', 'Maths', 'Physics', 'CompSci'}
art_courses = {'History', 'Geography', 'Maths'}

# Union - Combines elements from both sets, removing duplicates
print(cs_courses.union(art_courses))  # Output: {'History', 'Maths', 'Physics', 'CompSci', 'Geography'}

# Intersection - Returns only elements common to both sets
print(cs_courses.intersection(art_courses))  # Output: {'History', 'Maths'}

# Difference - Elements present in the first set but not in the second
print(cs_courses.difference(art_courses))  # Output: {'CompSci', 'Physics'}
# --------------------------------------------
# Set Methods
# --------------------------------------------

# Adding an element to a set
numbers.add(5)
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Removing an element from a set (raises KeyError if not found)
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5}

# Discard an element (does NOT raise an error if not found)
numbers.discard(10)  # No error even if 10 is not in the set

# Clearing all elements from a set
numbers.clear()
print(numbers)  # Output: set()

# Popping an element (removes and returns a random element)
sample_set = {10, 20, 30}
popped_element = sample_set.pop()
print(popped_element)  # Output: Random element from {10, 20, 30}
print(sample_set)  # Remaining elements after pop()

# --------------------------------------------
# Key Notes about Sets
# --------------------------------------------

# - Set elements must be immutable (strings, numbers, tuples, etc.).
# - A set itself is mutable, meaning we can add or remove elements.
# - Sets do NOT support indexing or slicing as they are unordered.