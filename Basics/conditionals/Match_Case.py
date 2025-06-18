# --------------------------------------------
# Match Case in Python (Similar to Switch-Case)
# --------------------------------------------

# A match statement compares a variable’s value to patterns (cases).
# Syntax:
# match variable:
#     case pattern1:
#         # statements
#     case pattern2 if condition:
#         # statements
#     case _:
#         # default fallback (like else)

# Example 1: Basic use of match-case
x = 4
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")  # Output
    case _ if x < 10:
        print("x is less than 10")
    case _:
        print(x)

# Output:
# x % 2 == 0 and case is 4

# Example 2: Dynamic input from user
x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x != 90:
        print(x, "is not 90")
    case _ if x != 80:
        print(x, "is not 80")
    case _:
        print(x)

# Notes:
# - `case _:` acts as the default case (like `else`)
# - You can use conditions (`if`) inside each case
# - Pattern matching works well with constants and simple conditions
