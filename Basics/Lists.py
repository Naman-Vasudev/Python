# Python Basics - Lists and Tuples

# --------------------------------------------
# Lists in Python
# --------------------------------------------

# A list is an ordered, mutable collection of elements.

# Defining a List
courses = ["History", "Math", "Physics", "CompSci"]  # List of subjects
print(courses)  # Output: ['History', 'Math', 'Physics', 'CompSci']

# Creating an empty list
empty_list1 = []  # Using square brackets
empty_list2 = list()  # Using list() constructor

# --------------------------------------------
# Accessing Elements in a List
# --------------------------------------------

print(len(courses))   # Length of the list (Number of elements)
print(courses[0])     # First element ('History')
print(courses[-1])    # Last element ('CompSci')

# Slicing lists (Extracting a portion of a list)
print(courses[0:2])   # Returns ['History', 'Math'] (Index 0 to 1, 2 is excluded)
print(courses[:2])    # Same as above (Start from 0)
print(courses[1:])    # From index 1 to the end ['Math', 'Physics', 'CompSci']

# --------------------------------------------
# Modifying a List
# --------------------------------------------

# Lists are mutable (modifiable)

# Adding elements to a list
courses.append("Art")  # Adds 'Art' at the end
print(courses)

# Inserting elements at a specific index
courses.insert(0, "Naman")  # Adds 'Naman' at index 0
print(courses)

# Extending a list with another list
additional_courses = ["Chemistry", "English"]
courses.extend(additional_courses)  # Merges lists
print(courses)

# --------------------------------------------
# Removing Elements from a List
# --------------------------------------------

courses.remove("Naman")  # Removes 'Naman' from the list
courses.pop()  # Removes the last element ('English' in this case)
print(courses)

# --------------------------------------------
# Sorting and Reversing Lists
# --------------------------------------------

courses.reverse()  # Reverses the order of elements in the list
print(courses)

courses.sort()  # Sorts the list in ascending order (Alphabetical for strings, numerical for numbers)
print(courses)

courses.sort(reverse=True)  # Sorts in descending order
print(courses)

# --------------------------------------------
# Preserving Original List with Sorted()
# --------------------------------------------

# The `sort()` method modifies the original list.
# If we want to keep the original order, we use `sorted()`

sorted_courses = sorted(courses)  # Returns a sorted copy without modifying the original list
print(sorted_courses)

# copy() Returns copy of the list. This can be done to perform operations on the list without modifying the original list. Example:

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# count() Returns the count of the number of items with the given value.Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]

# --------------------------------------------
# List Functions
# --------------------------------------------

numbers = [1, 2, 3, 4, 5]

print(min(numbers))  # Smallest number in the list
print(max(numbers))  # Largest number in the list
print(sum(numbers))  # Sum of all elements in the list

# Finding the index of an element
print(numbers.index(1))  # Returns the index of 1 (Output: 0)

# --------------------------------------------
# Converting Between Lists and Strings
# --------------------------------------------

# Convert a list to a string (Joining elements with a separator)
courses_str = ', '.join(courses)  # Joins list elements into a string separated by commas
print(courses_str)  # Output: 'Physics, Math, History, CompSci, Chemistry'

# Convert a string back to a list (Splitting by a separator)
new_list = courses_str.split(', ')
print(new_list)  # Output: ['Physics', 'Math', 'History', 'CompSci', 'Chemistry']