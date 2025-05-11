# --------------------------------------------
# Loops in Python
# --------------------------------------------

# --------------------------------------------
# While Loop
# --------------------------------------------

# A while loop executes a block of code as long as a condition is true.
count = 1
while count <= 5:
    print("Aman")  # Output: Aman (5 times)
    count += 1  # Increments count

print(count)  # Output: 6 (loop stops when count > 5)

# --------------------------------------------
# Example: Print numbers from 1 to 100
# --------------------------------------------
i = 1
while i <= 100:
    print(i, end=" ")  # Prints numbers in a single line
    i += 1
print()  # Newline

# --------------------------------------------
# Example: Print numbers from 100 to 1
# --------------------------------------------
j = 100
while j >= 1:
    print(j, end=" ")
    j -= 1
print()  # Newline

# --------------------------------------------
# Example: Print multiplication table of 3
# --------------------------------------------
k = 1
while k <= 10:
    print(f"3 x {k} = {3 * k}")
    k += 1



'''
Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop 
'''
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break

# --------------------------------------------
# Break and Continue in While Loop
# --------------------------------------------
i = 0
while i <= 5:
    if i == 3:
        i += 1  # Increment before continue to avoid infinite loop
        continue  # Skips printing 3
    print(i)  # Output: 0 1 2 4 5
    i += 1

# --------------------------------------------
# For Loop
# --------------------------------------------

# A for loop is used for iterating over a sequence (list, tuple, string, etc.)
nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)  # Output: 1 2 3 4 5

# Iterating over a string
string = "Naman"
for char in string:
    print(char)  # Output: N a m a n
else:
    print("END")  # This runs only if the loop wasn't exited with 'break'

# --------------------------------------------
# Break Statement
# --------------------------------------------
string = "Naman"
for char in string:
    if char == 'm':
        print("m found")  # Output: m found
        break  # Exits the loop
    print(char)  # Output: N a
else:
    print("END")  # Not executed because loop was broken

# --------------------------------------------
# Example: Print elements of a list using for loop
# --------------------------------------------
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for number in numbers:
    print(number)

# --------------------------------------------
# Example: Search for a number in a tuple and print its index
# --------------------------------------------
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
for index, num in enumerate(tup):
    if x == num:
        print(f"The number {x} is found at index {index}")

# --------------------------------------------
# Nested For Loop
# --------------------------------------------
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# --------------------------------------------
# The range() Function
# --------------------------------------------

# range(start, stop, step) generates a sequence of numbers
for el in range(5):  # Default start is 0, step is 1
    print(el)  # Output: 0 1 2 3 4

for el in range(1, 5):
    print(el)  # Output: 1 2 3 4

for el in range(1, 10, 2):  # Increment by 2
    print(el)  # Output: 1 3 5 7 9

# --------------------------------------------
# While Loop using Range Logic
# --------------------------------------------
x = 0
while x < 10:
    print(x)
    x += 1
