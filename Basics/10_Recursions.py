# --------------------------------------------
# Recursion in Python
# --------------------------------------------

"""
Recursion is a programming technique where a function calls itself repeatedly.
It is useful for problems that can be broken down into smaller subproblems.
Similar to loops but works by reducing the problem size in each call.
"""

# --------------------------------------------
# Example 1: Basic Recursive Function
# --------------------------------------------

def show(n):
    """Prints numbers from n to 1 using recursion."""
    if n == 0:
        return  # Base case: stops recursion when n reaches 0
    print(n)
    show(n - 1)  # Recursive call with n-1

show(5)
# Output:
# 5
# 4
# 3
# 2
# 1

# --------------------------------------------
# Example 2: Recursive Sum of First n Natural Numbers
# --------------------------------------------

def calc_sum(n):
    """Returns the sum of the first n natural numbers using recursion."""
    if n == 0:
        return 0  # Base case: sum of 0 numbers is 0
    return calc_sum(n - 1) + n  # Recursive step: sum(n) = sum(n-1) + n

# Taking user input for sum calculation
n = int(input("Enter n: "))  
print("Sum of first", n, "natural numbers:", calc_sum(n))

# --------------------------------------------
# Example 3: Recursive Function to Print List Elements
# --------------------------------------------

def print_list(lst, idx=0):
    """Prints all elements of a list recursively."""
    if idx == len(lst):
        return  # Base case: stop when index reaches list length
    print(lst[idx])
    print_list(lst, idx + 1)  # Recursive call with the next index

# List of fruits to print
fruits = ['mango', 'orange', 'apple', 'banana']
print_list(fruits)

# Output:
# mango
# orange
# apple
# banana
