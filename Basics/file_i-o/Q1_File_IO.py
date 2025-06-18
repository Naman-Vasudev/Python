"""
📂 PRACTICE QUESTIONS ON FILE HANDLING

This program performs various file operations on "practice.txt":
1️⃣ Create a new file and write given data.
2️⃣ Replace occurrences of "Java" with "Python".
3️⃣ Check if a user-input word exists in the file.
4️⃣ Find the first line where a user-input word appears.
"""

# -----------------------------------
# 1️⃣ CREATE A NEW FILE "practice.txt"
# -----------------------------------
# Using 'w' mode to write initial content (Overwrites if file exists)
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java.")

# Reading and displaying the content
with open("practice.txt", "r") as g:
    data = g.read()
print("📄 Initial File Content:\n", data)

# ✅ Output:
"""
📄 Initial File Content:
Hi everyone
we are learning File I/O
using Java
I like programming in Java.
"""

# -----------------------------------
# 2️⃣ REPLACING "Java" WITH "Python"
# -----------------------------------
# Replacing "Java" with "Python" in the file content
new_data = data.replace("Java", "Python")
print("📄 Updated Content After Replacement:\n", new_data)

# Writing the updated content back to the file
with open("practice.txt", "w") as h:
    h.write(new_data)

# ✅ Output:
"""
📄 Updated Content After Replacement:
Hi everyone
we are learning File I/O
using Python
I like programming in Python.
"""

# -----------------------------------
# 3️⃣ CHECK IF A USER-INPUT WORD EXISTS IN FILE
# -----------------------------------
# Taking user input for word search
word = input("🔍 Enter the word to search: ")

# Opening file in read mode and checking if word exists
with open("practice.txt", "r") as i:
    words = i.read()
    if words.find(word) != -1:
        print("✅ Word Found in File!")
    else:
        print("❌ Word Not Found!")

# ✅ Example Output:
"""
🔍 Enter the word to search: Python
✅ Word Found in File!
"""

# -----------------------------------
# 4️⃣ FIND FIRST OCCURRENCE OF A WORD IN LINES
# -----------------------------------
# Function to find in which line a word appears first
def check_for_line():
    """
    Reads the file line by line and checks where the given word occurs first.
    If found, prints the line number. If not found, returns -1.
    """
    word_to_be_checked = input("🔍 Enter the word to find its first occurrence: ")
    
    line_no = 1  # Line counter
    with open("practice.txt", "r") as j:
        for line in j:  # Reading line by line
            if word_to_be_checked in line:
                print(f"✅ Word found at line {line_no}")
                return
            line_no += 1
    
    print("❌ Word Not Found in Any Line!")
    return -1

# Calling the function
check_for_line()

# ✅ Example Output:
"""
🔍 Enter the word to find its first occurrence: Python
✅ Word found at line 3
"""
