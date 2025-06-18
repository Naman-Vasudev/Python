# --------------------------------------------
# Local and Global Variables in Python
# --------------------------------------------

# 📌 What is a Variable?
# A variable is a named location in memory that stores a value.
# Values are assigned using the '=' operator.

# Example:
x = 5
y = "Hello, World!"
print(x)  # Output: 5
print(y)  # Output: Hello, World!


# --------------------------------------------
# 🔹 Local vs Global Variables
# --------------------------------------------

# ✅ Global Variable: Defined outside all functions and accessible throughout the file.
# ✅ Local Variable: Defined inside a function and only accessible within that function.

# Example:
x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print("Inside function - Local y:", y)

my_function()               # Output: Inside function - Local y: 5
print("Outside function - Global x:", x)  # Output: Outside function - Global x: 10
# print(y)  # ❌ Error: 'y' is not defined outside the function


# --------------------------------------------
# 🔹 The `global` Keyword
# --------------------------------------------

# If you want to **modify a global variable inside a function**, use the `global` keyword.

x = 10  # Global variable

def update_global():
    global x   # Declare x as global to modify it
    x = 5      # Modify the global variable
    y = 99     # Local variable

update_global()
print("Modified global x:", x)  # Output: Modified global x: 5
# print(y)  # ❌ Error: 'y' is a local variable and cannot be accessed here


# --------------------------------------------
# ⚠️ Best Practice Warning
# --------------------------------------------

# It is generally recommended to avoid modifying global variables from within functions,
# as it can lead to unpredictable behavior and makes debugging harder.

# ✅ Prefer passing arguments to functions and returning results instead of using `global`.

# Example of better practice:
def modify_value(value):
    value += 5
    return value

x = 10
x = modify_value(x)
print("Safely modified x:", x)  # Output: Safely modified x: 15
