# -----------------------------------------------------
# 1️⃣ DELETING OBJECT ATTRIBUTES USING `del`
# -----------------------------------------------------
"""
✔️ The `del` keyword is used to delete object attributes.
✔️ Once deleted, trying to access the attribute raises an error.
"""

class Student:
    def __init__(self, name):
        self.name = name  # Instance attribute

# Creating an object
s1 = Student("Naman")
print(s1.name)  # Output: Naman

# Deleting an attribute
del s1.name  

# Trying to access deleted attribute (Uncommenting will cause an error)
# print(s1.name)  # ❌ AttributeError: 'Student' object has no attribute 'name'

# -----------------------------------------------------
# 2️⃣ PRIVATE (LIKE) ATTRIBUTES & METHODS (ENCAPSULATION)
# -----------------------------------------------------
"""
✔️ Python does **not** have true private attributes like Java or C++.
✔️ But by convention, we use **two leading underscores (`__`)** to indicate private attributes.
✔️ Private attributes cannot be accessed directly outside the class.
"""

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no  # Public attribute
        self.__acc_pass = acc_pass  # Private (like) attribute

    def reset_pass(self):
        """Method to access private attribute inside the class."""
        print(self.__acc_pass)

# Creating an object
acc1 = Account(12345, "abcde")

# Accessing public attribute
print(acc1.acc_no)  # Output: 12345

# Trying to access private attribute directly (Uncommenting will cause an error)
# print(acc1.__acc_pass)  # ❌ AttributeError: 'Account' object has no attribute '__acc_pass'

# Private attributes can still be accessed through class methods
acc1.reset_pass()  # Output: abcde

# -----------------------------------------------------
# 3️⃣ PRIVATE METHODS (HIDING INTERNAL LOGIC)
# -----------------------------------------------------
"""
✔️ We can also make methods private using double underscores (`__`).
✔️ Private methods cannot be called directly outside the class.
"""

class Person:
    __name = "Anonymous"  # Private attribute

    def __hello(self):  # Private method
        print("HELLO")

    def welcome(self):  
        """Public method that internally calls the private method."""
        self.__hello()

# Creating an object
p1 = Person()

# Trying to call private method directly (Uncommenting will cause an error)
# p1.__hello()  # ❌ AttributeError: 'Person' object has no attribute '__hello'

# Calling the private method via a public method
p1.welcome()  # Output: HELLO

# -----------------------------------------------------
# 4️⃣ INHERITANCE (REUSING PARENT CLASS METHODS & ATTRIBUTES)
# -----------------------------------------------------
"""
✔️ Inheritance allows a class (child) to inherit properties & methods from another class (parent).
✔️ It promotes **code reuse** and **organizational structure**.
"""

# Parent Class
class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

# -----------------------------------------------------
# 5️⃣ TYPES OF INHERITANCE
# -----------------------------------------------------

"""
1️⃣ **Single Inheritance** - Child inherits from one parent class.
2️⃣ **Multi-Level Inheritance** - A class inherits from a child class (grandchild concept).
3️⃣ **Multiple Inheritance** - A class inherits from multiple parent classes.
"""

# -----------------------------------------------------
# SINGLE INHERITANCE
# -----------------------------------------------------
class ToyotaCar(Car):  # Inheriting from `Car`
    def __init__(self, brand):
        self.brand = brand  # New attribute in child class

# Creating an object
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

# Calling parent class method from child class
car1.start()  # Output: Car started

# -----------------------------------------------------
# MULTI-LEVEL INHERITANCE (Grandchild Class)
# -----------------------------------------------------
class Fortuner(ToyotaCar):  # Fortuner inherits from ToyotaCar
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type  # New attribute in grandchild class

# Creating an object
car1 = Fortuner("Diesel")
car1.start()  # Output: Car started  (Inherited from `Car` class)

# -----------------------------------------------------
# MULTIPLE INHERITANCE (Inheriting from Multiple Parent Classes)
# -----------------------------------------------------
class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

class C(A, B):  # Inheriting from both A & B
    varC = "Welcome to Class C"

# Creating an object
c1 = C()

# Accessing attributes from multiple parent classes
print(c1.varC)  # Output: Welcome to Class C
print(c1.varA)  # Output: Welcome to Class A
print(c1.varB)  # Output: Welcome to Class B