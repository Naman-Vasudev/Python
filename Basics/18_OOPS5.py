# ===========================================================================
# 🔹 DUNDER (MAGIC) METHODS FOR OPERATOR OVERLOADING IN PYTHON
# ===========================================================================
"""
✔ **Dunder (Double Underscore) Methods**, also known as **Magic Methods**, allow us to:
   - Define custom behavior for built-in operators (`+`, `-`, `*`, etc.) in user-defined classes.
   - Enable objects to interact with Python's built-in functions (`len()`, `str()`, etc.).
✔ **Operator Overloading** lets us redefine how operators work for user-defined objects.
✔ These methods **must be defined inside a class** and follow the `__method__()` format.
"""

# ===========================================================================
# 1️⃣ COMMONLY USED DUNDER METHODS FOR ARITHMETIC OPERATORS
# ===========================================================================
"""
✔️ These methods allow us to overload arithmetic operations like `+`, `-`, `*`, `/`, etc.
✔️ They help define how objects of a class behave when these operators are used.
"""

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        """Overloads the `+` operator."""
        return Number(self.value + other.value)

    def __sub__(self, other):
        """Overloads the `-` operator."""
        return Number(self.value - other.value)

    def __mul__(self, other):
        """Overloads the `*` operator."""
        return Number(self.value * other.value)

    def __truediv__(self, other):
        """Overloads the `/` operator (true division)."""
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        """Overloads the `//` operator (floor division)."""
        return Number(self.value // other.value)

    def __mod__(self, other):
        """Overloads the `%` operator (modulus)."""
        return Number(self.value % other.value)

    def __pow__(self, other):
        """Overloads the `**` operator (exponentiation)."""
        return Number(self.value ** other.value)

    def __str__(self):
        """Returns a string representation of the object."""
        return str(self.value)

# Creating objects
num1 = Number(10)
num2 = Number(3)

# Testing arithmetic operations
print(num1 + num2)  # Output: 13
print(num1 - num2)  # Output: 7
print(num1 * num2)  # Output: 30
print(num1 / num2)  # Output: 3.3333...
print(num1 // num2) # Output: 3
print(num1 % num2)  # Output: 1
print(num1 ** num2) # Output: 1000

# ===========================================================================
# 2️⃣ DUNDER METHODS FOR BITWISE OPERATIONS
# ===========================================================================
"""
✔️ These methods allow us to define custom behavior for bitwise operations.
✔️ Bitwise operations include AND (`&`), OR (`|`), XOR (`^`), left shift (`<<`), and right shift (`>>`).
"""

class Binary:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        """Overloads the `&` (bitwise AND) operator."""
        return Binary(self.value & other.value)

    def __or__(self, other):
        """Overloads the `|` (bitwise OR) operator."""
        return Binary(self.value | other.value)

    def __xor__(self, other):
        """Overloads the `^` (bitwise XOR) operator."""
        return Binary(self.value ^ other.value)

    def __lshift__(self, other):
        """Overloads the `<<` (left shift) operator."""
        return Binary(self.value << other.value)

    def __rshift__(self, other):
        """Overloads the `>>` (right shift) operator."""
        return Binary(self.value >> other.value)

    def __str__(self):
        """Returns the binary representation of the number."""
        return bin(self.value)[2:]

# Creating objects
b1 = Binary(5)  # Binary: 101
b2 = Binary(3)  # Binary: 011

# Testing bitwise operations
print(b1 & b2)  # Output: 1  (Binary: 001)
print(b1 | b2)  # Output: 7  (Binary: 111)
print(b1 ^ b2)  # Output: 6  (Binary: 110)
print(b1 << b2) # Output: 40 (Binary: 101000)
print(b1 >> b2) # Output: 0  (Binary: 0)

# ===========================================================================
# 3️⃣ SPECIAL MATH FUNCTIONS
# ===========================================================================
"""
✔️ The following methods provide additional mathematical operations.
✔️ `__divmod__()` is used for simultaneous division & modulus operation.
"""

class Number:
    def __init__(self, value):
        self.value = value

    def __divmod__(self, other):
        """Overloads the `divmod()` function."""
        return divmod(self.value, other.value)

# Creating objects
num1 = Number(10)
num2 = Number(3)

# Testing divmod()
print(divmod(num1, num2))  # Output: (3, 1) → (quotient, remainder)

# ===========================================================================
# 🔹 SUMMARY OF COMMONLY USED DUNDER METHODS
# ===========================================================================
"""
✔️ **Arithmetic Operators**:
   - `__add__(self, other)`      → `+` (Addition)
   - `__sub__(self, other)`      → `-` (Subtraction)
   - `__mul__(self, other)`      → `*` (Multiplication)
   - `__truediv__(self, other)`  → `/` (True Division)
   - `__floordiv__(self, other)` → `//` (Floor Division)
   - `__mod__(self, other)`      → `%` (Modulus)
   - `__pow__(self, other)`      → `**` (Exponentiation)
   - `__divmod__(self, other)`   → `divmod()`

✔️ **Bitwise Operators**:
   - `__and__(self, other)`      → `&` (Bitwise AND)
   - `__or__(self, other)`       → `|` (Bitwise OR)
   - `__xor__(self, other)`      → `^` (Bitwise XOR)
   - `__lshift__(self, other)`   → `<<` (Left Shift)
   - `__rshift__(self, other)`   → `>>` (Right Shift)

✔️ **Other Useful Methods**:
   - `__str__(self)`             → Converts object to string
   - `__repr__(self)`            → Returns official string representation
   - `__eq__(self, other)`       → `==` (Equality comparison)
   - `__ne__(self, other)`       → `!=` (Not Equal comparison)
   - `__lt__(self, other)`       → `<` (Less than comparison)
   - `__le__(self, other)`       → `<=` (Less than or equal to)
   - `__gt__(self, other)`       → `>` (Greater than comparison)
   - `__ge__(self, other)`       → `>=` (Greater than or equal to)
"""

