"""
FILE HANDLING IN PYTHON
Python provides ways to perform file operations like reading, writing, and appending data.
Since RAM is volatile, we use files for permanent storage.
"""
import os  # Required for file deletion
# -------------------------------
# 1️⃣ OPENING A FILE (READ MODE)
# -------------------------------
# Syntax: open("filename", "mode")
# Mode 'r' is used to open a file for reading (default mode).



# Opening a file in read mode
# Assume `demo.txt` initially contains:
"""
My name is Naman Vasudev. I want to become the greatest of all time.
I don't need a miracle to reach the pinnacle. I am already on my way.
"""
f = open("demo.txt", "r")
data = f.read()  # Reads entire file content
print("📄 Initial File Content:\n", data)
f.close()

# ✅ Output:
"""
📄 Initial File Content:
My name is Naman Vasudev. I want to become the greatest of all time.
I don't need a miracle to reach the pinnacle. I am already on my way.
"""

# -------------------------------
# 2️⃣ FILE MODES IN PYTHON
# -------------------------------
"""
| Mode | Read | Write | Create | Truncate | Start Pos | End Pos |
|------|------|-------|--------|----------|-----------|---------|
| 'r'  | ✅   | ❌    | ❌     | ❌       | Start     | ❌      |
| 'r+' | ✅   | ✅    | ❌     | ❌       | Start     | ❌      |
| 'w'  | ❌   | ✅    | ✅     | ✅       | Start     | ❌      |
| 'w+' | ✅   | ✅    | ✅     | ✅       | Start     | ❌      |
| 'a'  | ❌   | ✅    | ✅     | ❌       | ❌        | End     |
| 'a+' | ✅   | ✅    | ✅     | ❌       | ❌        | End     |

- **Read (`r`)**: Opens a file for reading. (Default)
- **Write (`w`)**: Opens a file for writing, truncating the file first.
- **Append (`a`)**: Opens a file for writing, adding new data to the end.
- **Read+Write (`r+`, `w+`, `a+`)**: Allows both reading and writing.
- **Binary mode (`b`)**: Used for non-text files (e.g., images, videos).
"""

# -------------------------------
# 3️⃣ READING FILE CONTENT
# -------------------------------
# Reading one line at a time using `readline()`
f = open("demo.txt", "r")
line1 = f.readline()  # Reads first line
print("🔹 First Line:", line1.strip())  # Using `.strip()` to remove newline characters
f.close()

# ✅ Output:
"""
🔹 First Line: My name is Naman Vasudev. I want to become the greatest of all time.
"""

# Reading first 5 characters
f = open("demo.txt", "r")
first5chars = f.read(5)  # Reads first 5 characters
print("🔹 First 5 Characters:", first5chars)
f.close()

# ✅ Output:
"""
🔹 First 5 Characters: My na
"""

# -------------------------------
# 4️⃣ WRITING TO A FILE (OVERWRITE MODE)
# -------------------------------
# Using 'w' mode will overwrite the entire file
f = open("demo.txt", "w")
f.write("This is a new line.\n")  # Overwrites previous content
f.close()

# Reading back the updated content
with open("demo.txt", "r") as f:
    print("📄 Updated File Content:\n", f.read())

# ✅ Output:
"""
📄 Updated File Content:
This is a new line.
"""

# -------------------------------
# 5️⃣ APPENDING TO A FILE (ADDING DATA)
# -------------------------------
# Using 'a' mode to append content at the end
f = open("demo.txt", "a")
f.write("This is an appended line.\n")  # Adds new content
f.close()

# Reading back the updated content
with open("demo.txt", "r") as f:
    print("📄 After Appending:\n", f.read())

# ✅ Output:
"""
📄 After Appending:
This is a new line.
This is an appended line.
"""

# -------------------------------
# 6️⃣ USING `with open()` (Auto-closes File)
# -------------------------------
# `with open()` ensures the file is automatically closed after use
with open("demo.txt", "r") as f:
    data = f.read()
print("📄 Using `with open()`, File Content:\n", data)

# ✅ Output:
"""
📄 Using `with open()`, File Content:
This is a new line.
This is an appended line.
"""

# -------------------------------
# 7️⃣ CREATING A NEW FILE (USING 'x' MODE)
# -------------------------------
try:
    f = open("new_file.txt", "x")  # Creates a new file
    f.write("This is a newly created file.\n")
    f.close()
    print("✅ File 'new_file.txt' created successfully!")
except FileExistsError:
    print("⚠️ File 'new_file.txt' already exists.")

# -------------------------------
# 8️⃣ DELETING A FILE
# -------------------------------
# Deleting 'demo.txt' (uncomment to execute)
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("🗑️ File deleted successfully!")
# else:
#     print("⚠️ File does not exist.")
