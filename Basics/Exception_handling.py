# ====================================================
# ✅ PYTHON EXCEPTION HANDLING - COMPLETE NOTES
# ====================================================

# ----------------------------------------------------
# 🔸 What is Exception Handling?
# ----------------------------------------------------
# Exception handling is the process of responding to unwanted or unexpected events
# that occur during program execution to prevent crashes.

# ----------------------------------------------------
# 🔸 Basic try-except Block
# ----------------------------------------------------
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("❌ Number entered is not an integer.")

# Output:
# Enter an integer: abc
# ❌ Number entered is not an integer.

# ----------------------------------------------------
# 🔸 try-except-else Block
# ----------------------------------------------------
# `else` runs only if try block has no exceptions.

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("❌ Invalid input. Not an integer.")
else:
    print("✅ Integer accepted.")

# Output:
# Enter an integer: 10
# ✅ Integer accepted.

# ----------------------------------------------------
# 🔸 try-except with Multiple Exceptions
# ----------------------------------------------------
try:
    num = int(input("Enter an index (0-1): "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("❌ Number entered is not an integer.")
except IndexError:
    print("❌ Index out of range.")

# Output 1:
# Enter an index: 1 ➝ 3
# Output 2:
# Enter an index: two ➝ ❌ Number entered is not an integer.

# ----------------------------------------------------
# 🔸 finally Block
# ----------------------------------------------------
# The `finally` block always runs regardless of error or return statements.

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("❌ Not an integer.")
else:
    print("✅ Integer accepted.")
finally:
    print("📌 This block is always executed.")

# Output:
# No matter what input, the finally block runs.

# ----------------------------------------------------
# 🔸 finally with return statement
# ----------------------------------------------------
def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("❌ Some error occurred")
        return 0
    finally:
        print("📌 I am always executed")

x = func1()
print(f"Returned: {x}")

# Output:
# - If valid index: prints value, "I am always executed", returns 1
# - If error: prints error, "I am always executed", returns 0

# ----------------------------------------------------
# 🔸 raise - Raising Custom Errors
# ----------------------------------------------------
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("❌ Not a valid salary (must be between 2000 and 5000)")

# Output:
# Enter salary: 1500 ➝ ValueError: Not a valid salary

# ----------------------------------------------------
# 🔸 Defining Custom Exceptions (User-defined)
# ----------------------------------------------------
# We can define our own exception types by inheriting from `Exception`.

class CustomError(Exception):
    """Custom exception class."""
    pass

try:
    a = int(input("Enter a value between 5 and 9: "))
    if a < 5 or a > 9:
        raise CustomError("❌ Value should be between 5 and 9.")
    print("✅ Valid input.")
except CustomError as ce:
    print(ce)

# Output:
# Enter: 3 ➝ ❌ Value should be between 5 and 9.

# ----------------------------------------------------
# 🔚 Summary
# ----------------------------------------------------
# ➤ `try`: Run this block of code.
# ➤ `except`: Handle errors if any.
# ➤ `else`: Run if no error occurs.
# ➤ `finally`: Always run this block.
# ➤ `raise`: Manually throw an error.
# ➤ Custom Errors: Use `class MyError(Exception)` to define your own.
