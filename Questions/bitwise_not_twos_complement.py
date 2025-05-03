# The ~ operator is the bitwise NOT operator in Python
# For any integer n, ~n equals -(n+1) due to two's complement representation

# PROOF FOR THE FORMULA ~n = -(n+1):
# In two's complement representation:
# 1. Positive integers are represented in standard binary form
# 2. Negative integers are represented by flipping all bits of the absolute value and adding 1
#
# Case 1: For x = ~1
# First, represent 1 in binary (using 8 bits for simplicity): 00000001
# Applying bitwise NOT (~) flips all bits: 11111110
# This is a negative number in two's complement
# To find its decimal value:
#   - Flip all bits: 00000001
#   - Add 1: 00000010 (which is 2 in decimal)
#   - Add the negative sign: -2
# Therefore, ~1 = -2
#
# Case 2: For y = ~0
# First, represent 0 in binary: 00000000
# Applying bitwise NOT (~) flips all bits: 11111111
# This is a negative number in two's complement
# To find its decimal value:
#   - Flip all bits: 00000000
#   - Add 1: 00000001 (which is 1 in decimal)
#   - Add the negative sign: -1
# Therefore, ~0 = -1

# In Python, we can verify this directly:
x = ~1  # x equals -2
y = ~0  # y equals -1
print(x, y)  # This will print: -2 -1

# The correct output is -2 -1