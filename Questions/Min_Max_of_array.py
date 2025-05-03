list1=[1,2,3,66,56,45,4,404,45]
# import math

# min_value = -math.inf   # Negative infinity
# max_value = math.inf    # Positive infinity

# print("Using math module:")
# print("Minimum value:", min_value)
# print("Maximum value:", max_value)

neg_inf = float('-inf')   # Negative infinity
pos_inf = float('inf')    # Positive infinity


# Initialize with extreme values
min_value = pos_inf  # Start with positive infinity for the minimum
max_value = neg_inf  # Start with negative infinity for the maximum

for num in list1:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print("The max value is ", max_value)
print("The min value is ", min_value)