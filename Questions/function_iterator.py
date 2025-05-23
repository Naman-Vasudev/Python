"""
🔍 Problem Statement:
Given a string `S`, determine whether it contains:
1. Any alphanumeric characters
2. Any alphabetical characters
3. Any digits
4. Any lowercase characters
5. Any uppercase characters

---

📥 Input Format:
A single line string, S  
(0 < len(S) < 1000)

📤 Output Format:
Five lines, each printing `True` or `False` based on the respective conditions above.

---

✅ Built-in Python Methods Overview:
- str.isalnum() → True if all characters are alphanumeric (a-z, A-Z, 0-9)
- str.isalpha() → True if all characters are alphabetical (a-z, A-Z)
- str.isdigit() → True if all characters are digits (0-9)
- str.islower() → True if all characters are lowercase (a-z)
- str.isupper() → True if all characters are uppercase (A-Z)

"""

# Accept input string
s = input("Enter a string: ").strip()

print("=== Naive Approach Using 5 Separate Loops ===")
# Naive approach: Repeats string traversal unnecessarily

for i in s:
    if i.isalnum():
        print("True")
        break
else:
    print("False")

for i in s:
    if i.isalpha():
        print("True")
        break
else:
    print("False")

for i in s:
    if i.isdigit():
        print("True")
        break
else:
    print("False")

for i in s:
    if i.islower():
        print("True")
        break
else:
    print("False")

for i in s:
    if i.isupper():
        print("True")
        break
else:
    print("False")


print("\n=== Optimized Using First-Class Functions ===")
# We define a list of function references (first-class functions)
# In Python, functions are first-class citizens: they can be stored in variables, passed around, etc.
# Here, we pass the string methods (like str.isalpha) directly and call them on each character.

checks = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

# Loop through each method in the checks list
for check in checks:
    for char in s:
        if check(char):  # dynamically calls the method on each character
            print("True")
            break
    else:
        print("False")


print("\n=== Pythonic Approach Using any() Function ===")
# The any() function returns True if at least one element in the iterable is True.
# It stops iterating as soon as it finds the first True — making it efficient.
# We use generator expressions for concise and memory-efficient iteration.

print(any(i.isalnum() for i in s))  # True if any character is alphanumeric
print(any(i.isalpha() for i in s))  # True if any character is alphabetic
print(any(i.isdigit() for i in s))  # True if any character is a digit
print(any(i.islower() for i in s))  # True if any character is lowercase
print(any(i.isupper() for i in s))  # True if any character is uppercase
