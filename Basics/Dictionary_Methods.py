# ============================================
# Python Dictionary Methods - Complete Notes
# ============================================

# A dictionary is a collection of key-value pairs.
# Let's explore the various methods to update, delete, and retrieve data from dictionaries.

# ------------------------------------------------
# 1. update() - Add or Modify Key-Value Pairs
# ------------------------------------------------

# If the key exists, its value is updated. If not, a new key-value pair is added.

info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)  
# Output: {'name': 'Karan', 'age': 19, 'eligible': True}

info.update({'age': 20})       # Updates 'age'
info.update({'DOB': 2001})     # Adds new key 'DOB'
print(info)
# Output: {'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}


# ------------------------------------------------
# 2. clear() - Remove All Items from Dictionary
# ------------------------------------------------

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.clear()
print(info)  
# Output: {}


# ------------------------------------------------
# 3. pop() - Remove a Specific Key-Value Pair
# ------------------------------------------------

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')  # Removes the key 'eligible'
print(info)  
# Output: {'name': 'Karan', 'age': 19}


# ------------------------------------------------
# 4. popitem() - Remove the Last Inserted Key-Value Pair
# ------------------------------------------------

info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()  # Removes the last inserted item ('DOB': 2003)
print(info)  
# Output: {'name': 'Karan', 'age': 19, 'eligible': True}


# ------------------------------------------------
# 5. del - Delete a Key or Entire Dictionary
# ------------------------------------------------

# Deleting a specific key
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info['age']
print(info)
# Output: {'name': 'Karan', 'eligible': True, 'DOB': 2003}

# Deleting the entire dictionary
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info
# print(info)  # Uncommenting this will raise: NameError: name 'info' is not defined


# ------------------------------------------------
# 6. Adding and Updating Dictionary Entries
# ------------------------------------------------

student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'CompSci']}

# Adding a new key-value pair
student['phone'] = '9779972095'
print(student['phone'])  
# Output: 9779972095

# Updating multiple values
student.update({'name': 'Naman', 'college': 'PEC'})
print(student)
# Output: {'name': 'Naman', 'age': 25, 'courses': ['Maths', 'CompSci'], 'phone': '9779972095', 'college': 'PEC'}


# ------------------------------------------------
# 7. Removing Entries from a Dictionary
# ------------------------------------------------

del student['age']  # Removes the 'age' key
print(student)
# Output: Dictionary without 'age'


# ------------------------------------------------
# 8. Useful Dictionary Methods
# ------------------------------------------------

print(len(student))        # Number of key-value pairs → Output: 4
print(student.keys())      # All dictionary keys → dict_keys(['name', 'courses', 'phone', 'college'])
print(student.values())    # All values → dict_values([...])
print(student.items())     # All items as (key, value) tuples

# Safe value access using get()
print(student.get("college"))  # Output: PEC
print(student.get("gender"))   # Output: None (no error)


# ------------------------------------------------
# 9. Merging Dictionaries with update()
# ------------------------------------------------

new_data = {'hobby': 'Reading', 'city': 'Delhi'}
student.update(new_data)
print(student)
# Output: Updated dictionary with 'hobby' and 'city'


# ------------------------------------------------
# 10. Nested Dictionaries
# ------------------------------------------------

student1 = {
    "name": "Rahul Kumar",
    "subjects": {
        "physics": 97,
        "chemistry": 100
    }
}
# Accessing a nested value
print(student1['subjects']['chemistry'])  
# Output: 100