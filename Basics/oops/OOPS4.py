# -----------------------------------------------------
# 1️⃣ POLYMORPHISM: OPERATOR OVERLOADING
# -----------------------------------------------------
"""
✔️ **Polymorphism** allows the same operator or function to behave differently based on the context.
✔️ **Operator Overloading** enables us to define custom behavior for operators (`+`, `-`, `*`, etc.) in user-defined classes.
✔️ This is achieved using **dunder (double underscore) methods** like `__add__`, `__sub__`, etc.
"""

# -----------------------------------------------------
# 2️⃣ DEFAULT OPERATOR BEHAVIOR
# -----------------------------------------------------
"""
✔️ Operators behave differently depending on the data types they work with:
   - `"Hello" + "World"`  → Concatenation (`HelloWorld`)
   - `[1, 2] + [3, 4]`    → List merging (`[1, 2, 3, 4]`)
   - `5 + 10`             → Addition (`15`)
✔️ We can customize this behavior for user-defined classes using dunder methods.
"""

# -----------------------------------------------------
# 3️⃣ IMPLEMENTING OPERATOR OVERLOADING WITHOUT DUNDER METHODS
# -----------------------------------------------------
"""
✔️ Here’s how we **manually** add two complex numbers using a method.
✔️ We define an `add()` method inside the class.
"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        """Displays the complex number in a readable format."""
        print(f"{self.real} + {self.img}j")

    def add(self, num2):
        """Manually adds two complex numbers."""
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

# Creating two complex numbers
num1 = Complex(1, 3)
num2 = Complex(4, 6)

# Displaying the numbers
num1.showNumber()  # Output: 1 + 3j
num2.showNumber()  # Output: 4 + 6j

# Adding manually using a method
num3 = num1.add(num2)
num3.showNumber()  # Output: 5 + 9j

# -----------------------------------------------------
# 4️⃣ OPERATOR OVERLOADING USING DUNDER METHODS
# -----------------------------------------------------
"""
✔️ Instead of defining a separate `add()` method, we can **override the `+` operator** using `__add__()`.
✔️ This allows us to use `num1 + num2` directly instead of `num1.add(num2)`.
"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        """Displays the complex number in a readable format."""
        print(f"{self.real} + {self.img}j")

    def __add__(self, num2):
        """Overrides the `+` operator to add two complex numbers."""
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return Complex(new_real, new_img)

# Creating two complex numbers
num1 = Complex(1, 3)
num2 = Complex(4, 6)

# Displaying the numbers
num1.showNumber()  # Output: 1 + 3j
num2.showNumber()  # Output: 4 + 6j

# Using `+` operator directly (thanks to `__add__()`)
num3 = num1 + num2
num3.showNumber()  # Output: 5 + 9j
