"""
COMPREHENSIVE GUIDE TO DICTIONARY AND LIST ITERATION IN PYTHON
==============================================================

This file contains detailed explanations and examples of how to iterate through
dictionaries and lists in Python, with special focus on Tkinter applications.

Author: Python Learning Guide
Purpose: Understanding iteration methods for data structures
"""

# =============================================================================
# SAMPLE DATA STRUCTURES FOR EXAMPLES
# =============================================================================

# Simple dictionary (key-value pairs)
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 96
}

# Nested dictionary (like your syllabus)
course_syllabus = {
    "Mathematics": {
        "Algebra": "Linear equations, quadratic equations",
        "Calculus": "Derivatives, integrals, limits",
        "Statistics": "Mean, median, mode, probability"
    },
    "Physics": {
        "Mechanics": "Force, motion, energy",
        "Thermodynamics": "Heat, temperature, entropy",
        "Optics": "Light, reflection, refraction"
    },
    "Chemistry": {
        "Organic": "Carbon compounds, reactions",
        "Inorganic": "Metals, acids, bases"
    }
}

# Simple list
fruits = ["apple", "banana", "cherry", "date"]

# List of dictionaries
students = [
    {"name": "John", "age": 20, "grade": "A"},
    {"name": "Jane", "age": 19, "grade": "B"},
    {"name": "Mike", "age": 21, "grade": "A"}
]

# Dictionary with lists as values
subjects_teachers = {
    "Math": ["Mr. Smith", "Ms. Johnson"],
    "Science": ["Dr. Brown", "Prof. Wilson"],
    "English": ["Mrs. Davis"]
}

print("="*70)
print("DICTIONARY ITERATION METHODS")
print("="*70)

# =============================================================================
# METHOD 1: ITERATING OVER KEYS ONLY (Default behavior)
# =============================================================================
print("\n1. ITERATING OVER KEYS ONLY")
print("-" * 40)

print("Method: for key in dictionary")
print("Use when: You only need the keys, not the values")
print("Example:")

for student in student_grades:  # 'student' gets each key
    print(f"Student name: {student}")
    # Note: We only have the key here, not the value
    # To get value, we'd need: student_grades[student]

print("\nSame as using .keys() explicitly:")
for student in student_grades.keys():  # Explicitly getting keys
    print(f"Student name: {student}")

# =============================================================================
# METHOD 2: ITERATING OVER VALUES ONLY
# =============================================================================
print("\n\n2. ITERATING OVER VALUES ONLY")
print("-" * 40)

print("Method: for value in dictionary.values()")
print("Use when: You only need the values, not the keys")
print("Example:")

for grade in student_grades.values():  # Only gets values
    print(f"Grade: {grade}")
    # Note: We don't know which student this grade belongs to

print("\nPractical use - calculating average:")
total_grades = sum(student_grades.values())
average = total_grades / len(student_grades)
print(f"Class average: {average:.2f}")

# =============================================================================
# METHOD 3: ITERATING OVER KEY-VALUE PAIRS (.items())
# =============================================================================
print("\n\n3. ITERATING OVER KEY-VALUE PAIRS")
print("-" * 40)

print("Method: for key, value in dictionary.items()")
print("Use when: You need both keys and values")
print("Example:")

for student, grade in student_grades.items():  # Gets both key and value
    print(f"Student: {student}, Grade: {grade}")
    
    # This is equivalent to:
    # for student in student_grades:
    #     grade = student_grades[student]
    #     print(f"Student: {student}, Grade: {grade}")

print("\nWhy .items() is better than manual lookup:")
print("Without .items():")
for student in student_grades:
    grade = student_grades[student]  # Extra dictionary lookup (slower)
    print(f"{student}: {grade}")

print("\nWith .items():")
for student, grade in student_grades.items():  # Direct access (faster)
    print(f"{student}: {grade}")

# =============================================================================
# NESTED DICTIONARY ITERATION (Like your syllabus example)
# =============================================================================
print("\n\n4. NESTED DICTIONARY ITERATION")
print("-" * 40)

print("Your syllabus structure:")
print("course_syllabus = { 'subject': { 'topic': 'description' } }")
print()

# Level 1: Iterate through subjects
print("Level 1 - Subjects only:")
for subject in course_syllabus:
    print(f"Subject: {subject}")

print("\nLevel 2 - Subject and topics:")
for subject, topics in course_syllabus.items():
    print(f"\nSubject: {subject}")
    print(f"Number of topics: {len(topics)}")
    
    # Now iterate through the inner dictionary
    for topic, description in topics.items():
        print(f"  Topic: {topic}")
        print(f"  Description: {description}")

print("\nAlternative approach without .items() (more verbose):")
for subject in course_syllabus:
    print(f"\nSubject: {subject}")
    topics = course_syllabus[subject]  # Get the inner dictionary
    
    for topic in topics:  # Iterate through topic names
        description = topics[topic]  # Manual lookup for description
        print(f"  Topic: {topic}")
        print(f"  Description: {description}")

# =============================================================================
# TKINTER SPECIFIC EXAMPLES
# =============================================================================
print("\n\n5. TKINTER BUTTON CREATION EXAMPLES")
print("-" * 40)

print("Creating buttons from dictionary - The RIGHT way:")
print()

"""
# This is how you'd create buttons in Tkinter:

# WRONG WAY - Common mistake:
for subject in course_syllabus:
    for topic in subject:  # ERROR! 'subject' is a string, not a dictionary
        # This iterates over letters: "M", "a", "t", "h", "e", "m", "a", "t", "i", "c", "s"
        button = Button(window, text=topic)

# RIGHT WAY - Method 1 (using .items()):
for subject, topics in course_syllabus.items():
    # Create subject button
    subject_button = Button(window, text=subject, 
                           command=lambda s=subject: show_topics(s))
    
    # In the show_topics function:
    for topic, description in topics.items():
        topic_button = Button(window, text=topic,
                             command=lambda d=description: show_description(d))

# RIGHT WAY - Method 2 (without .items(), but more work):
for subject in course_syllabus:
    topics = course_syllabus[subject]  # Get inner dictionary
    
    subject_button = Button(window, text=subject,
                           command=lambda s=subject: show_topics(s))
    
    for topic in topics:
        description = topics[topic]  # Manual lookup
        topic_button = Button(window, text=topic,
                             command=lambda d=description: show_description(d))
"""

# =============================================================================
# LIST ITERATION METHODS
# =============================================================================
print("\n\n6. LIST ITERATION METHODS")
print("-" * 40)

print("Simple list iteration:")
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\nList iteration with index using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Position {index}: {fruit}")

print("\nWhen you need only indices:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("\nIterating over list of dictionaries:")
for student in students:  # Each 'student' is a dictionary
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

print("\nAlternative with index:")
for i, student in enumerate(students):
    print(f"Student {i+1}: {student['name']} (Age: {student['age']})")

# =============================================================================
# DICTIONARY WITH LISTS AS VALUES
# =============================================================================
print("\n\n7. DICTIONARY WITH LISTS AS VALUES")
print("-" * 40)

print("Structure: { 'key': [list of values] }")
print()

for subject, teachers in subjects_teachers.items():
    print(f"\nSubject: {subject}")
    print(f"Teachers: {', '.join(teachers)}")  # Join list elements
    
    # Or iterate through each teacher:
    for teacher in teachers:
        print(f"  - {teacher}")

# =============================================================================
# ADVANCED ITERATION TECHNIQUES
# =============================================================================
print("\n\n8. ADVANCED ITERATION TECHNIQUES")
print("-" * 40)

print("Dictionary comprehension:")
# Create new dictionary with modified values
grade_letters = {student: "Pass" if grade >= 80 else "Fail" 
                for student, grade in student_grades.items()}
print("Pass/Fail status:", grade_letters)

print("\nFiltering during iteration:")
# Only iterate over students with grades >= 90
high_performers = {student: grade for student, grade in student_grades.items() 
                  if grade >= 90}
print("High performers:", high_performers)

print("\nSorted iteration:")
# Iterate in sorted order by keys
for student in sorted(student_grades.keys()):
    print(f"{student}: {student_grades[student]}")

# Iterate sorted by values
for student, grade in sorted(student_grades.items(), key=lambda x: x[1], reverse=True):
    print(f"{student}: {grade}")

# =============================================================================
# COMMON PITFALLS AND SOLUTIONS
# =============================================================================
print("\n\n9. COMMON PITFALLS AND SOLUTIONS")
print("-" * 40)

print("PITFALL 1: Confusing string iteration with dictionary iteration")
print("WRONG:")
sample_dict = {"Unit 1": {"topic1": "desc1"}}
for unit in sample_dict:  # unit = "Unit 1" (string)
    print(f"Unit: {unit}")
    # for topic in unit:  # This iterates over "U", "n", "i", "t", " ", "1"
    #     print(topic)    # WRONG!

print("CORRECT:")
for unit, topics in sample_dict.items():  # Get both unit name and topics dict
    print(f"Unit: {unit}")
    for topic, description in topics.items():
        print(f"  Topic: {topic}, Description: {description}")

print("\nPITFALL 2: Lambda functions in loops")
print("WRONG:")
"""
buttons = []
for unit in course_syllabus:
    # All buttons will call show_topics with the LAST unit value
    button = Button(window, text=unit, command=lambda: show_topics(unit))
    buttons.append(button)
"""

print("CORRECT:")
"""
buttons = []
for unit in course_syllabus:
    # Each button captures its own copy of the unit value
    button = Button(window, text=unit, command=lambda u=unit: show_topics(u))
    buttons.append(button)
"""

print("\nPITFALL 3: Modifying dictionary while iterating")
print("WRONG:")
"""
for student, grade in student_grades.items():
    if grade < 80:
        del student_grades[student]  # RuntimeError: dictionary changed size
"""

print("CORRECT:")
"""
# Create a list of keys to remove
to_remove = [student for student, grade in student_grades.items() if grade < 80]
for student in to_remove:
    del student_grades[student]
"""

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================
print("\n\n10. PERFORMANCE COMPARISON")
print("-" * 40)

print("Most efficient to least efficient:")
print("1. for key, value in dict.items()     # Best for key-value pairs")
print("2. for key in dict                    # Best for keys only")
print("3. for value in dict.values()         # Best for values only")
print("4. for key in dict.keys()             # Unnecessary explicit call")
print("5. Manual lookup in loop              # Slowest")

# =============================================================================
# SUMMARY AND BEST PRACTICES
# =============================================================================
print("\n\n11. SUMMARY AND BEST PRACTICES")
print("-" * 40)

print("""
WHEN TO USE EACH METHOD:

1. dict.keys() or just 'for key in dict':
   - When you only need dictionary keys
   - Example: Getting list of all student names

2. dict.values():
   - When you only need dictionary values
   - Example: Calculating sum/average of grades

3. dict.items():
   - When you need both keys and values
   - Most common in Tkinter for button creation
   - Always use this instead of manual key lookup

4. enumerate() for lists:
   - When you need both index and value
   - Example: Numbering items in a list

5. Lambda with default parameters:
   - Always use in Tkinter command callbacks within loops
   - Prevents all buttons from using the last loop value

MEMORY:
- .items() creates key-value pairs on demand (efficient)
- .keys() and .values() create views (very efficient)
- Manual lookup does extra work (less efficient)

READABILITY:
- .items() makes code more readable
- Shows intent clearly (need both key and value)
- Reduces chance of errors
""")

print("\n" + "="*70)
print("END OF COMPREHENSIVE ITERATION GUIDE")
print("="*70)

# =============================================================================
# PRACTICAL TKINTER EXAMPLE (Commented out - for reference)
# =============================================================================
"""
from tkinter import *

def create_syllabus_app():
    # This function demonstrates the concepts in a real Tkinter app
    
    def show_topics(subject_name):
        topic_window = Toplevel()
        topic_window.title(f"Topics in {subject_name}")
        
        # Get topics for this subject
        topics = course_syllabus[subject_name]
        
        # Method 1: Using .items() (RECOMMENDED)
        for topic, description in topics.items():
            btn = Button(topic_window, text=topic,
                        command=lambda d=description: show_description(d))
            btn.pack(pady=5)
        
        # Method 2: Without .items() (MORE WORK)
        # for topic in topics:
        #     description = topics[topic]  # Extra lookup
        #     btn = Button(topic_window, text=topic,
        #                 command=lambda d=description: show_description(d))
        #     btn.pack(pady=5)
    
    def show_description(desc):
        desc_window = Toplevel()
        Label(desc_window, text=desc, wraplength=300).pack(pady=20)
    
    # Main window
    root = Tk()
    root.title("Course Syllabus")
    
    # Create subject buttons
    for subject in course_syllabus:
        btn = Button(root, text=subject,
                    command=lambda s=subject: show_topics(s))
        btn.pack(pady=10)
    
    root.mainloop()

# Uncomment to run:
# create_syllabus_app()
"""