# Dictionaries store data in key-value pairs.
# They are unordered, mutable (changeable), and do not allow duplicate keys.

student_dict = {  # Dictionary with different types of values
    "name": "Naman",   # String value
    "cgpa": 9.6,       # Float value
    "marks": [98, 97, 95]  # List value
}

print(student_dict["name"])  # Output: Naman
print(student_dict["cgpa"])  # Output: 9.6
print(student_dict["marks"])  # Output: [98, 97, 95]

# --------------------------------------------
# Accessing Values in a Dictionary
# --------------------------------------------

student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}
print(student['name'])  # Output: John
print(student['age'])  # Output: 25
print(student.get('name'))  # Output: John (Same as above, but safer)

# If a key doesn't exist, get() returns None instead of an error.
print(student.get('phone'))  # Output: None

# --------------------------------------------
# Adding and Updating Dictionary Entries
# --------------------------------------------

# Adding a new key-value pair
student['phone'] = '9779972095'
print(student['phone'])  # Output: 9779972095

# Updating values
student.update({'name': 'Naman', 'college': 'PEC'})
print(student)  # Output: {'name': 'Naman', 'age': 25, 'courses': ['Maths', 'CompSci'], 'phone': '9779972095', 'college': 'PEC'}

# --------------------------------------------
# Removing Entries from a Dictionary
# --------------------------------------------

del student['age']  # Deletes the key 'age'
print(student)  # Output: Dictionary without 'age'

# --------------------------------------------
# Dictionary Methods
# --------------------------------------------

print(len(student))  # Number of key-value pairs in the dictionary
print(student.keys())  # Output: All dictionary keys
print(student.values())  # Output: All dictionary values
print(student.items())  # Output: All (key, value) pairs as tuples

# Using get() to retrieve a value safely
print(student.get("college"))  # Output: PEC

# Merging another dictionary into the existing one
new_data = {'hobby': 'Reading', 'city': 'Delhi'}
student.update(new_data)
print(student)  # Output: Dictionary updated with 'hobby' and 'city'

# --------------------------------------------
# Nested Dictionaries
# --------------------------------------------

student1 = {
    "name": "Rahul Kumar",
    "subjects": {
        "physics": 97,
        "chemistry": 100
    }
} 
print(student1['subjects']['chemistry'])  # Output: 100