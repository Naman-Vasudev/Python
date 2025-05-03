# -----------------------------------------------------
# 1️⃣ SUPER METHOD (ACCESSING PARENT CLASS METHODS)
# -----------------------------------------------------
"""
✔️ The `super()` method allows access to the parent class's methods and attributes.
✔️ It is commonly used in inheritance to reuse code from the parent class.
"""

class Car:
    def __init__(self, car_type):
        self.type = car_type  # Parent class attribute

    @staticmethod
    def start(): 
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

# Child class inheriting from Car
class ToyotaCar(Car):
    def __init__(self, name, car_type):
        super().__init__(car_type)  # Calling the parent class constructor
        self.name = name  # Child class attribute

# Creating an object
car1 = ToyotaCar("Prius", "Electric")

# Accessing attributes
print(car1.type)  # Output: Electric

# -----------------------------------------------------
# 2️⃣ CLASS METHOD (MODIFYING CLASS ATTRIBUTES)
# -----------------------------------------------------
"""
✔️ A `classmethod` modifies or accesses class attributes.
✔️ It takes `cls` as the first parameter instead of `self`.
"""

class Person:
    name = "Anonymous"  # Class attribute

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name  # Modifies the class attribute

# Creating an object
p1 = Person()
p1.change_name("Rahul Kumar")  # Changing class attribute using class method

# Accessing class attributes
print(p1.name)        # Output: Rahul Kumar
print(Person.name)    # Output: Rahul Kumar

# -----------------------------------------------------
# 3️⃣ TYPES OF METHODS IN A CLASS
# -----------------------------------------------------
"""
✔️ **Instance Methods (`self`)**: Can access and modify instance attributes.
✔️ **Class Methods (`cls`)**: Can modify class attributes but not instance attributes.
✔️ **Static Methods (`@staticmethod`)**: Cannot modify class or instance attributes.
"""

# -----------------------------------------------------
# 4️⃣ PROPERTY METHOD (DYNAMIC ATTRIBUTE CALCULATION)
# -----------------------------------------------------
"""
✔️ A property method allows us to define an attribute whose value is dynamically calculated.
✔️ This prevents the need to manually update the attribute after modifying other attributes.
"""

# Without using @property (Incorrect way)
class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths) / 3) + " %"  # Calculated only once

# Creating an object
stu1 = Student(98, 97, 99)
print(stu1.percentage)  # Output: 98.0 %

# Modifying a subject score
stu1.phy = 86
print(stu1.percentage)  # ❌ Still shows the old percentage (doesn't update dynamically)

# -----------------------------------------------------
# 5️⃣ USING @PROPERTY (CORRECT WAY)
# -----------------------------------------------------
"""
✔️ The `@property` decorator creates a read-only attribute that dynamically updates.
✔️ This ensures the latest data is always used when accessing the attribute.
"""

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + " %"

# Creating an object
stu1 = Student(98, 97, 99)
print(stu1.percentage)  # Output: 98.0 %

# Modifying a subject score
stu1.phy = 86
print(stu1.percentage)  # ✅ Now correctly updates to reflect the new value