# ----------------------------
# SHORTHAND IF-ELSE IN PYTHON
# ----------------------------

# ✅ Description:
# Python supports a compact form of if-else called the "shorthand if-else".
# This is ideal for short conditions and simple statements on a single line.

# ----------------------------
# Example 1: Basic One-Line If-Else
# ----------------------------
a = 2
b = 330

# If 'a' is greater than 'b', print "A", else print "B"
print("A") if a > b else print("B")  # Output: B

# ----------------------------
# Example 2: One-Line If-Else with Multiple Conditions
# ----------------------------
a = 330
b = 330

# This checks multiple conditions in one line:
# If a > b → print "A"
# Else if a == b → print "="
# Else → print "B"
print("A") if a > b else print("=") if a == b else print("B")  # Output: =

# ----------------------------
# Example 3: Assigning Values Using Shorthand If-Else
# ----------------------------

# Syntax:
# result = value_if_true if condition else value_if_false

x = 10
y = 20

# Assigns the larger value to 'max_val' using shorthand if-else
max_val = x if x > y else y
print("Max value is:", max_val)  # Output: Max value is: 20

# Equivalent long form:
# if x > y:
#     max_val = x
# else:
#     max_val = y

# ----------------------------
# ✅ Conclusion:
# ----------------------------
# ✔ Shorthand if-else is useful for:
#    - Quick comparisons
#    - Simple assignments
#    - Readable one-liners
#
# ❌ Avoid using it when:
#    - You need to perform multiple operations
#    - The logic is too complex (as it can reduce readability)

# ➕ Tip: Use it wisely to write cleaner, more concise code when appropriate.
