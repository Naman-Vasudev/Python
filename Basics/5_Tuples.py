# --------------------------------------------
# Tuples in Python
# --------------------------------------------

# Tuples are similar to lists but **immutable** (non-modifiable).
# Once created, their values cannot be changed.

# Example: Lists are mutable
list1 = [1, 2, 3]
list2 = list1  # list2 references the same list as list1
list1[0] = 99  # Modifying list1 will also affect list2
print(list2)  # Output: [99, 2, 3] (lists are mutable)

# Example: Tuples are immutable
tuple1 = (1, 2, 3)
# tuple1[0] = 99  # ❌ This will raise a TypeError because tuples cannot be modified.

# --------------------------------------------
# Creating Tuples
# --------------------------------------------

# Syntax: tuple_name = (element1, element2, ...)
tup = (87, 64, 33, 95, 76)
print(tup)  # Output: (87, 64, 33, 95, 76)

# Empty tuple
empty_tuple1 = ()  # Using parentheses
empty_tuple2 = tuple()  # Using tuple() constructor

# Single-element tuple (note the comma, required for it to be recognized as a tuple)
single_element_tuple = (1,)  # ✅ Correct
not_a_tuple = (1)  # ❌ Incorrect, this is just an integer

# Multiple elements tuple
multi_element_tuple = (1, 2, 3)

# --------------------------------------------
# Tuple Methods
# --------------------------------------------

tup = (2, 1, 3, 1)  # Sample tuple

# Finding the index of the first occurrence of an element
print(tup.index(1))  # Output: 1 (first occurrence of 1 is at index 1)

# Counting occurrences of an element
print(tup.count(1))  # Output: 2 (1 appears twice in the tuple)

# Accessing elements
print(tup[0])  # Output: 2 (first element)
print(tup[-1]) # Output: 1 (last element)

# Slicing tuples (same as lists)
print(tup[1:3])  # Output: (1, 3) (slicing from index 1 to 2, 3 is excluded)