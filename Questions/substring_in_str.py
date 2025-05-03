# The string to search within
string = "Hello, welcome to the world of Python."
# The substring to find
substring = "welcome"

# 1. Using the find() method
index = string.find(substring)
if index != -1:
    print(f"Method 1: Substring '{substring}' found at index {index}")
else:
    print(f"Method 1: Substring '{substring}' not found.")

# 2. Using a for loop
found_for = False
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        print(f"Method 2: Substring '{substring}' found at index {i}")
        found_for = True
        break

if not found_for:
    print(f"Method 2: Substring '{substring}' not found.")

# 3. Using the 'in' operator
if substring in string:
    print(f"Method 3: Substring '{substring}' found!")
else:
    print(f"Method 3: Substring '{substring}' not found.")
