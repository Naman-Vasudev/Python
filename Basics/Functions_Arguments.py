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