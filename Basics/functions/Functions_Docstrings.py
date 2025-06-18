# ------------------------------
# Python Docstrings Explanation
# ------------------------------

# Docstrings in Python are string literals that appear right after the definition
# of a function, method, class, or module. They serve as documentation and are 
# stored as the object's __doc__ attribute.

# ------------------------------
# Example 1: Simple Docstring
# ------------------------------
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)  # Output: 25

# The docstring here:
# '''Takes in a number n, returns the square of n'''
# is a string literal used for documentation. It doesn't affect runtime behavior.

# Output:
# 25


# -----------------------------------
# Example 2: Descriptive Function Docstring
# -----------------------------------
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2


# -----------------------------------
# Comments vs. Docstrings in Python
# -----------------------------------

# 1. Python Comments:
#    - Begin with a '#' symbol.
#    - Used for internal code explanation.
#    - Ignored by the Python interpreter.

# 2. Python Docstrings:
#    - Enclosed in triple quotes (''' or """).
#    - Placed immediately after function/class/module definition.
#    - Stored in the __doc__ attribute.
#    - Can be accessed programmatically for documentation purposes.


# -----------------------------------
# Accessing Docstrings Using __doc__
# -----------------------------------

def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

# Access and print the docstring
print(square.__doc__)

# Output:
# Takes in a number n, returns the square of n