# ------------------------------------------------------
# FUNCTION ARGUMENTS & RETURN STATEMENT IN PYTHON
# ------------------------------------------------------

# Python supports multiple types of function arguments:
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Required (Positional) Arguments
# 4. Variable-Length Arguments (*args, **kwargs)
# 5. Return Statement

# ------------------------------------------------------
# 1. DEFAULT ARGUMENTS
# ------------------------------------------------------
# You can assign default values to function parameters.
# If the argument is not passed, the default is used.

def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")  
# Output: Hello, Amy Jhon Whatson

# ------------------------------------------------------
# 2. KEYWORD ARGUMENTS
# ------------------------------------------------------
# Arguments are passed using key=value format.
# Order does not matter in this case.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname="Peter", lname="Wesker", fname="Jade")  
# Output: Hello, Jade Peter Wesker

# ------------------------------------------------------
# 3. REQUIRED (POSITIONAL) ARGUMENTS
# ------------------------------------------------------
# Arguments must be passed in the correct order and count
# or Python will raise an error.

# ❌ Incorrect: Missing one argument
# name("Peter", "Quill")  
# Error: TypeError: name() missing 1 required positional argument: 'lname'

# ✅ Correct
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")  
# Output: Hello, Peter Ego Quill

# ------------------------------------------------------
# 4. VARIABLE-LENGTH ARGUMENTS
# ------------------------------------------------------

# 4.1. Arbitrary Positional Arguments (*args)
# Allows passing any number of positional arguments.
# They are received as a tuple.

def name(*names):
    print("Hello,", names[0], names[1], names[2])

name("James", "Buchanan", "Barnes")  
# Output: Hello, James Buchanan Barnes

# 4.2. Arbitrary Keyword Arguments (**kwargs)
# Allows passing any number of named arguments.
# They are received as a dictionary.

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")  
# Output: Hello, James Buchanan Barnes

# 4.3. Combine Positional, *args, and **kwargs
# Order: normal params -> *args -> default params -> **kwargs

def full_intro(title, *traits, status="Active", **info):
    print(f"Title: {title}")
    print("Traits:", traits)
    print("Status:", status)
    print("Additional Info:", info)

full_intro("Agent", "Loyal", "Stealthy", location="Wakanda", mission="Top Secret")
# Output:
# Title: Agent
# Traits: ('Loyal', 'Stealthy')
# Status: Active
# Additional Info: {'location': 'Wakanda', 'mission': 'Top Secret'}

# ------------------------------------------------------
# 5. RETURN STATEMENT
# ------------------------------------------------------
# Used to send back a value from a function to the caller.

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))  
# Output: Hello, James Buchanan Barnes

# ------------------------------------------------------
# EXTRA EXAMPLE: Default Parameters + Return
# ------------------------------------------------------

def hello_func(greeting, name='You'):
    """Returns a formatted greeting message with a default name."""
    return f"{greeting}, {name}!"

# Function calls
print(hello_func('Hi', 'Naman'))            # Output: Hi, Naman!
print(hello_func('Hello'))                  # Output: Hello, You!
print(hello_func('Good morning', name='Aman'))  # Output: Good morning, Aman!

# ------------------------------------------------------
# BONUS: Mixed Argument Example - Positional, Default, and Keyword
# ------------------------------------------------------

def demo_args(b, c, d, a=10):
    print("a:", a, "b:", b, "c:", c, "d:", d)

# Mixing positional and keyword arguments
# Positional: b=10, c=20 | Keyword: d=30 | a uses default=10
demo_args(10, 20, d=30)
# Output: a: 10 b: 10 c: 20 d: 30

# Another call overriding the default
demo_args(1, 2, 3, 4)
# Output: a: 4 b: 1 c: 2 d: 3

# ------------------------------------------------------
# Argument Order Rule Summary
# ------------------------------------------------------
# In function definitions:
# 1. Positional arguments (required)
# 2. *args (arbitrary positional)
# 3. Default arguments
# 4. **kwargs (arbitrary keyword)
