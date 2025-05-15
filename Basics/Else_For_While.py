# ============================================
# ✅ Python - else in for and while Loops
# ============================================

# ------------------------------------------------
# 🔹 Purpose of 'else' in Loops
# ------------------------------------------------
# In Python, the 'else' block after a for or while loop:
# ✅ Executes **only if the loop completes normally** (i.e., NOT terminated by a break).
# ❌ It does NOT execute if the loop is exited via a `break` statement.

# ============================================
# 🔸 Example 1: 'else' in a for loop (No break)
# ============================================
for x in range(5):
    print(f"Iteration {x+1} inside for loop")
else:
    print("✅ else block executed because loop was not broken")

# Output:
# Iteration 1 inside for loop
# Iteration 2 inside for loop
# Iteration 3 inside for loop
# Iteration 4 inside for loop
# Iteration 5 inside for loop
# ✅ else block executed because loop was not broken

# ============================================
# 🔸 Example 2: 'else' in a for loop (With break)
# ============================================
for x in range(5):
    print(f"Iteration {x+1} inside for loop")
    if x == 2:
        break  # Loop breaks when x == 2
else:
    print("❌ This will NOT be printed because loop was broken")

# Output:
# Iteration 1 inside for loop
# Iteration 2 inside for loop
# Iteration 3 inside for loop

# (Note: else block does NOT run here because of break)

# ============================================
# 🔸 Example 3: 'else' in a while loop (No break)
# ============================================
i = 0
while i < 5:
    print(f"While loop iteration: {i}")
    i += 1
else:
    print("✅ else block executed because while loop ended normally")

# Output:
# While loop iteration: 0
# While loop iteration: 1
# While loop iteration: 2
# While loop iteration: 3
# While loop iteration: 4
# ✅ else block executed because while loop ended normally

# ============================================
# 🔸 Example 4: 'else' in a while loop (With break)
# ============================================
i = 0
while i < 5:
    print(f"While loop iteration: {i}")
    if i == 2:
        break  # Loop breaks when i == 2
    i += 1
else:
    print("❌ This will NOT be printed because loop was broken")

# Output:
# While loop iteration: 0
# While loop iteration: 1
# While loop iteration: 2

# (Note: else block does NOT run here because of break)


# ============================================
# ✅ Summary:
# ============================================

# - The 'else' clause in loops is a Pythonic way to handle "completed without interruption".
# - It’s often used in **search** algorithms:
#     → Loop through items
#     → If item found → break
#     → else: print("Not found")

# ============================================
# 🔸 Bonus Example: Searching with else
# ============================================
nums = [2, 4, 6, 8, 10]
target = 7

for num in nums:
    if num == target:
        print(f"{target} found in list!")
        break
else:
    print(f"{target} not found in list.")  # Only runs if loop completes with no break

# Output:
# 7 not found in list.