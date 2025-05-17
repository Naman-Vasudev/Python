# ----------------------------
# ENUMERATE() FUNCTION IN PYTHON
# ----------------------------

# ✅ Description:
# The built-in enumerate() function adds a counter (index) to an iterable and returns it as an enumerate object.
# It is often used in loops where both the index and value are needed.

# ----------------------------
# Example 1: Basic Usage with a List
# ----------------------------
fruits = ['apple', 'banana', 'mango']

# Looping over the list with enumerate to access both index and value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 mango

# ----------------------------
# Example 2: Custom Start Index
# ----------------------------

# You can set the starting index using the 'start' argument
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 mango

# ----------------------------
# Example 3: Formatted Output Using f-Strings
# ----------------------------
for index, fruit in enumerate(fruits):
    print(f'{index + 1}: {fruit}')  # Adds 1 to start counting from 1

# Output:
# 1: apple
# 2: banana
# 3: mango

# ----------------------------
# Example 4: Using Enumerate to Trigger Action at Specific Index
# ----------------------------
marks = [12, 56, 32, 98, 12, 45, 1, 4]

# Using enumerate to access both index and mark value
for index, mark in enumerate(marks, start=1):  # Start index from 1
    print(mark)
    if index == 3:
        print("Harry, awesome!")  # Custom message at the 3rd item

# ----------------------------
# Example 5: Enumerate with Tuple
# ----------------------------
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

# Output:
# 0 red
# 1 green
# 2 blue

# ----------------------------
# Example 6: Enumerate with String
# ----------------------------
s = 'hello'
for index, char in enumerate(s):
    print(index, char)

# Output:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o

# ----------------------------
# ✅ Conclusion:
# ----------------------------
# ✔ enumerate() is useful when:
#    - You need both index and value while looping
#    - You want readable, concise code instead of manually managing counters
#
# ✔ Works with: Lists, Tuples, Strings, and any iterable.
#
# ➕ Tip: Use the 'start' argument if you want the index to begin from a number other than 0.
