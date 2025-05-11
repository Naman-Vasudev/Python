"""
📖 OBJECT-ORIENTED PROGRAMMING (OOP) IN PYTHON

➡️ **OOP allows us to model real-world entities in code using Objects and Classes.**
➡️ **Key Concepts in OOP:**
   - **Class**: A blueprint for creating objects.
   - **Object (Instance)**: A specific entity created from a class.
   - **Encapsulation**: Wrapping data and methods into a single unit (object).
   - **Abstraction**: Hiding implementation details and exposing only necessary functionalities.
   - **Inheritance**: One class can inherit attributes and methods from another.
   - **Polymorphism**: Same function name can have different implementations.
"""

# -----------------------------------------------------
# 1️⃣ CLASSES AND OBJECTS
# -----------------------------------------------------

# Creating a simple class
class Student:
    name = "Naman Vasudev"  # Class Attribute (shared by all instances)

# Creating objects (instances of the class)
s1 = Student()
s2 = Student()

# Accessing class attributes through objects
print(s1.name)  # Output: Naman Vasudev
print(s2.name)  # Output: Naman Vasudev

# -----------------------------------------------------
# 2️⃣ CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES
# -----------------------------------------------------
"""
✔️ **Class Attributes**: Shared among all instances (saves memory).
✔️ **Instance Attributes**: Unique for each object.
"""

class Car:
    color = "Blue"  # Class Attribute
    brand = "Mercedes"

car1 = Car()
print(car1.color)  # Output: Blue
print(car1.brand)  # Output: Mercedes

# -----------------------------------------------------
# 3️⃣ THE __init__() METHOD (CONSTRUCTOR)
# -----------------------------------------------------
"""
✔️ The __init__() method is automatically called when an object is created.
✔️ It initializes the object's attributes.
✔️ The `self` parameter refers to the current instance.
"""

class Student:
    def __init__(self, name, marks):  
        self.name = name  # Instance Attribute
        self.marks = marks  # Instance Attribute
        print("Adding new student to database...")

# Creating objects
s1 = Student("Naman", 100)  # Constructor is called automatically
print(s1.name, s1.marks)  # Output: Naman 100

s2 = Student("Aman", 99)  # Constructor is called again
print(s2.name, s2.marks)  # Output: Aman 99

# -----------------------------------------------------
# 4️⃣ CLASS ATTRIBUTES vs INSTANCE ATTRIBUTES
# -----------------------------------------------------
"""
✔️ **Class Attribute**: Shared by all instances (saves memory).
✔️ **Instance Attribute**: Unique to each object.
"""

class Student:
    college_name = "PEC"  # Class Attribute (same for all instances)

    def __init__(self, name, marks):
        self.name = name  # Instance Attribute (unique for each object)
        self.marks = marks  # Instance Attribute

# Creating objects
s1 = Student("Naman", 100)

# Accessing class attributes
print(s1.college_name)  # Output: PEC
print(Student.college_name)  # Output: PEC (accessed directly via class)

# Accessing instance attributes
print(s1.name)  # Output: Naman (instance attribute overrides class attribute)

# -----------------------------------------------------
# 5️⃣ METHODS (FUNCTIONS INSIDE A CLASS)
# -----------------------------------------------------
"""
✔️ Methods are functions that belong to an object.
✔️ They must have `self` as the first parameter to access instance attributes.
"""

class Student:
    college_name = "PEC"  # Class Attribute

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to display a welcome message
    def welcome(self):
        print(f"Welcome, {self.name}!")  # Uses instance attribute

    # Method to return marks
    def get_marks(self):
        return self.marks

# Creating an object
s1 = Student("Naman", 100)

# Calling methods
s1.welcome()  # Output: Welcome, Naman!
print(s1.get_marks())  # Output: 100

# -----------------------------------------------------
# 6️⃣ CALCULATING AVERAGE MARKS USING A METHOD
# -----------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name  # Instance attribute
        self.marks = marks  # List of marks

    def get_avg(self):
        total = sum(self.marks)  # Sum of marks
        avg = total / len(self.marks)  # Calculate average
        print(f"{self.name}'s average marks: {avg}")  

# Creating an object and calling the method
s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()  # Output: Tony Stark's average marks: 98.0

# -----------------------------------------------------
# 7️⃣ STATIC METHODS IN A CLASS
# -----------------------------------------------------
"""
✔️ Static methods do **not** use `self`.
✔️ They belong to the class but don't access instance attributes.
✔️ It can be created for one time and can be used by objects whenever required
✔️ Used when a function is related to the class but doesn't modify objects.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod  # Decorator for static methods
    def hello():
        print("Hello! Welcome to the Student Database.")

# Calling the static method
Student.hello()  # Output: Hello! Welcome to the Student Database.
# -----------------------------------------------------
# 8️⃣ ABSTRACTION & ENCAPSULATION
# -----------------------------------------------------
"""
✔️ **Abstraction**: Hiding complex implementation details and exposing only the necessary functionality.
✔️ **Encapsulation**: Wrapping data and methods into a single unit (class), restricting direct access to data.
"""

class Car:
    def __init__(self):
        self.__accelerator = False  # Private attribute (not directly accessible outside the class)
        self.__brake = False
        self.__clutch = False

    def start(self):
        self.__clutch = True
        self.__accelerator = True
        print("Car started...")

# Creating an object
car1 = Car()
car1.start()  # Output: Car started...
# The internal working of how the car starts is hidden (abstraction).

# -----------------------------------------------------
# 9️⃣ BANK ACCOUNT CLASS (ENCAPSULATION EXAMPLE)
# -----------------------------------------------------
"""
✔️ Implements encapsulation by keeping balance as a private attribute.
✔️ Provides methods for debit, credit, and balance retrieval.
"""

class Account:
    def __init__(self, balance, acc_no):
        self.__balance = balance  # Private attribute
        self.acc_no = acc_no  

    def debit(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Rs. {amount} debited. Remaining balance: Rs. {self.get_balance()}")

    def credit(self, amount):
        self.__balance += amount
        print(f"Rs. {amount} credited. Total balance: Rs. {self.get_balance()}")

    def get_balance(self):
        return self.__balance

# Creating an account object
acc1 = Account(10000, 12345)
print("Account Number:", acc1.acc_no)

# Performing transactions
acc1.debit(1000)  # Rs. 1000 debited. Remaining balance: Rs. 9000
acc1.credit(500)  # Rs. 500 credited. Total balance: Rs. 9500

# Trying to access private attribute directly (will cause an error)
# print(acc1.__balance)  # AttributeError: 'Account' object has no attribute '__balance'


