# ============================================
# ✅ Python Dictionaries - Complete Notes
# ============================================

# ============================================
# 🔹 What is a Dictionary?
# ============================================
# A dictionary is an ordered collection of key-value pairs.
# - Keys must be unique and immutable (like strings, numbers, tuples).
# - Values can be of any data type.
# - Dictionaries are mutable (changeable) and enclosed in {}.

# Basic Example:
student_dict = {
    "name": "Naman",              # String value
    "cgpa": 9.6,                  # Float value
    "marks": [98, 97, 95]         # List value
}
print(student_dict["name"])   # Output: Naman
print(student_dict["cgpa"])   # Output: 9.6
print(student_dict["marks"])  # Output: [98, 97, 95]


# ============================================
# 🔹 Creating a Dictionary
# ============================================

info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
# Output: {'name': 'Karan', 'age': 19, 'eligible': True}


# ============================================
# 🔹 Accessing Dictionary Items
# ============================================

# I. Accessing single values
print(info['name'])           # Output: Karan
print(info.get('eligible'))   # Output: True

# II. Accessing multiple values
print(info.values())  
# Output: dict_values(['Karan', 19, True])

# III. Accessing all keys
print(info.keys())  
# Output: dict_keys(['name', 'age', 'eligible'])

# IV. Accessing all key-value pairs
print(info.items())
# Output: dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])


# ============================================
# 🔹 get() vs [] for Accessing Values
# ============================================

student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}

print(student['name'])       # Output: John
print(student.get('name'))   # Output: John

# Using get() is safer when key might not exist
print(student.get('phone'))  # Output: None (instead of error)