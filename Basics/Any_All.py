"""
Title: Understanding `any()` and `all()` Functions in Python

Author: Naman (formalized with ChatGPT assistance)

---

📌 Objective:
To understand the behavior and equivalence of the built-in functions `any()` and `all()` in Python compared to traditional for-loop constructs.

---

🔹 any(iterable)

- Returns `True` if **at least one element** in the iterable is truthy.
- Short-circuits on the first `True`.
- Equivalent to:
    for element in iterable:
        if element:
            return True
    return False

Example (manual vs any):

# Task: Check if any character in `s` is alphanumeric

s = "abc#"

# Manual loop
for i in s:
    if i.isalnum():
        print(True)
        break
else:
    print(False)

# Pythonic
print(any(i.isalnum() for i in s))

---

🔹 all(iterable)

- Returns `True` if **all elements** in the iterable are truthy.
- Short-circuits on the first `False`.
- Equivalent to:
    for element in iterable:
        if not element:
            return False
    return True

Example (manual vs all):

# Task: Check if all characters in `s` are digits

s = "12345"

# Manual loop
for i in s:
    if not i.isdigit():
        print(False)
        break
else:
    print(True)

# Pythonic
print(all(i.isdigit() for i in s))

---

🧠 Summary Table:

| Built-in | Manual Equivalent Logic |
|----------|--------------------------|
| any(...) | for i in s:<br>if cond(i): return True<br>return False |
| all(...) | for i in s:<br>if not cond(i): return False<br>return True |

---

✅ Use Cases:

- Use `any()` to test **if at least one** condition is true.
- Use `all()` to test **if every** condition is true.
- These enhance clarity, conciseness, and efficiency in Pythonic code.

"""