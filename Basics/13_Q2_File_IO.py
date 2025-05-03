"""
📂 QUESTION: Count the number of even integers from a file.
The file "Q2.FileIO.txt" contains:
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,233,3465,6663,765,65,67,5,567,576
"""

# Initialize counter for even numbers
count = 0

# -----------------------------
# 1️⃣ OPEN THE FILE & READ DATA
# -----------------------------
with open("Q2.FileIO.txt", "r") as f:
    data = f.read()  # Read entire file as a string

# ✅ Checking file content
print("📄 File Content:\n", data)

# ✅ Output:
"""
📄 File Content:
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,233,3465,6663,765,65,67,5,567,576
"""

# -----------------------------
# 2️⃣ PROCESS THE DATA
# -----------------------------
# 🔹 `data.split(",")` breaks the string at each comma and returns a list of string numbers.
nums = data.split(",") 

# ✅ Example Output:
"""
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '20', '22', '233', '3465', '6663', '765', '65', '67', '5', '567', '576']
"""

# -----------------------------
# 3️⃣ COUNT EVEN NUMBERS
# -----------------------------
for val in nums:
    if int(val) % 2 == 0:  # Convert string to integer and check if it's even
        count += 1

# -----------------------------
# 4️⃣ DISPLAY OUTPUT
# -----------------------------
print("🔢 Total Even Numbers:", count)

# ✅ Example Output:
"""
🔢 Total Even Numbers: 12
"""