# ------------------------------------------------------
# 📌 Q1: Circle Class - Calculate Area & Perimeter
# ------------------------------------------------------

class Circle:
    """
    A class to represent a circle with radius.
    Provides methods to calculate area and perimeter.
    """
    def __init__(self, radius):
        self.radius = radius  # Instance attribute: radius of the circle

    def area(self):
        """Calculates and returns the area of the circle."""
        return (22/7) * (self.radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter (circumference) of the circle."""
        return 2 * (22/7) * self.radius

# Creating an instance of Circle with radius 21
c1 = Circle(21)

# Displaying area and perimeter
print("Circle Area:", c1.area())         # Output: 1386.0
print("Circle Perimeter:", c1.perimeter()) # Output: 132.0


# ------------------------------------------------------
# 📌 Q2: Employee & Engineer Classes - Inheritance
# ------------------------------------------------------

class Employee:
    """
    A class to represent an Employee with role, department, and salary.
    """
    def __init__(self, role, department, salary):
        self.role = role          # Employee role
        self.department = department  # Department of work
        self.salary = salary      # Salary of the employee
    
    def show_details(self):
        """Displays employee details."""
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

# Creating an Employee object
e1 = Employee("Accountant", "Finance", "60000")
e1.show_details()

# -----------------------------------------------
# 🔹 Inheritance: Engineer class inherits Employee
# -----------------------------------------------

class Engineer(Employee):
    """
    A class to represent an Engineer.
    Inherits properties from Employee and adds name & age.
    """
    def __init__(self, name, age):
        self.name = name  # Engineer's name
        self.age = age    # Engineer's age

        # Call the parent class (Employee) constructor
        super().__init__("Engineer", "IT", "75000")

# Creating an Engineer object
eng1 = Engineer("Elon Musk", 40)

# Displaying Engineer details
eng1.show_details()


# ------------------------------------------------------
# 📌 Q3: Order Class - Operator Overloading (__gt__)
# ------------------------------------------------------

class Order:
    """
    A class to represent an order with item name and price.
    Implements operator overloading for comparison.
    """
    def __init__(self, item, price):
        self.item = item    # Item name
        self.price = price  # Price of the item

    def __gt__(self, other_order):
        """
        Overloading '>' operator to compare orders by price.
        Returns True if the first order's price is greater.
        """
        return self.price > other_order.price

# Creating two order objects
order1 = Order("Chips", 20)
order2 = Order("Tea", 15)

# Comparing orders using overloaded '>' operator
print("Is order1 more expensive than order2?", order1 > order2)  # Output: True