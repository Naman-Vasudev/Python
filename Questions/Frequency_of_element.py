# ================================
# Count Occurrence of Elements
# Using 3 Different Methods
# ================================

# Sample list (mixed types: int + str)
sample_list = [1, "apple", 2, "banana", "apple", 1, 2, 3]

# ------------------------------
# Method 1: Using a Regular Dict
# ------------------------------
print("Method 1: Using a regular dictionary")
count_dict = dict()
for element in sample_list:
    if element not in count_dict:
        count_dict[element] = 1
    else:
        count_dict[element] += 1

print(count_dict)  # Output: {1: 2, 'apple': 2, 2: 2, 'banana': 1, 3: 1}
print()

# ---------------------------------
# Method 2: Using defaultdict(int)
# ---------------------------------
from collections import defaultdict

print("Method 2: Using defaultdict")
count_defaultdict = defaultdict(int)
for element in sample_list:
    count_defaultdict[element] += 1

print(dict(count_defaultdict))  # Converted to regular dict for clean output
print()

# -----------------------------
# Method 3: Using Counter
# -----------------------------
from collections import Counter

print("Method 3: Using Counter")
count_counter = Counter(sample_list)

print(count_counter)  # Output: Counter({1: 2, 'apple': 2, 2: 2, 'banana': 1, 3: 1})

x="apple"
print(f"Count of {x} is:", count_dict.get(x, 0))


# Print the count of x
print(f"Count of {x} is:", count_defaultdict[x])  # No need for .get(), defaults to 0

# Print the count of x
print(f"Count of {x} is:", count_counter[x])  # Same as defaultdict: missing keys return 0