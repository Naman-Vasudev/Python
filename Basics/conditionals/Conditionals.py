# Python Basics - Conditional Statements and Logical Operators

# --------------------------------------------
# Conditional Statements (if-elif-else)
# --------------------------------------------

language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No match")

# --------------------------------------------
# Logical Operators (and, or, not)
# --------------------------------------------

# Example: Checking user authentication
user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin Page")  # Both conditions must be True
else:
    print("Bad Credentials")

# Explanation of logical operators:
#   and  -> Returns True only if both conditions are True
#   or   -> Returns True if at least one condition is True
#   not  -> Reverses the boolean value (True becomes False, False becomes True)

# Example: Weather conditions
temp = 20
is_sunny = True  # Used meaningful variable name

if temp <= 0 or temp >= 30:
    print("The temperature is bad")  # Executes if temp is ≤ 0 or ≥ 30
else:
    print("The temperature is good") # Executes if temp is within the range (0,30)

if not is_sunny:
    print("It is cloudy")  # Executes if is_sunny is False
else:
    print("It is sunny")    # Executes if is_sunny is True

# --------------------------------------------
# Identity Operators (is, is not)
# --------------------------------------------

# Lists comparison
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # Prints memory address of 'a'
print(id(b))  # Prints memory address of 'b' (Different from 'a')

# 'a' and 'b' have the same values but are different objects in memory
print(a is b)  # False (Different objects)
print(a == b)  # True (Same values)

# Assigning 'a' to 'c' (Reference Copy)
c = a
print(id(c))  # Memory address of 'c' is same as 'a'
print(a is c)  # True (Both refer to the same object)

# --------------------------------------------
# False Values in Python
# --------------------------------------------

# The following values evaluate to False in conditional statements:
#   - False
#   - None
#   - Zero of any numeric type (0, 0.0, 0j)
#   - Any empty sequence ( "", (), [] )
#   - Any empty mapping ( {} )

condition = ()  # Empty tuple (Evaluates to False)

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")  # This will execute
