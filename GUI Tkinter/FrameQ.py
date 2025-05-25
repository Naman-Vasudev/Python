from tkinter import *  # Import all tkinter components

# Advanced function that receives parameter to show specific unit's topics
def show_topics(unit):
    # Clear all existing widgets from the frame to make space for new content
    # .winfo_children() returns list of all child widgets inside frame
    # .destroy() completely removes each widget from memory
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a back button that calls show_units() function when clicked
    # width=40 makes button 40 characters wide for consistent appearance
    back_button = Button(frame, text="Back to Units", width=40, command=show_units)
    back_button.pack(pady=10)  # pady=10 adds vertical spacing of 10 pixels

    # Create label showing which unit's topics are being displayed
    # f"..." is f-string formatting to insert variable value into text
    unit_label = Label(frame, text=f"The topics of {unit} are below:", font=("Arial", 14))
    unit_label.pack(pady=10)

    # Conditional logic to determine which topics to show based on unit parameter
    # Each if/elif checks the exact unit name and assigns corresponding topics
    if unit == "Unit 1: Vectors, Fields, and Electrostatics":
        topics = ["Cartesian Coordinate System", "Gauss's Law & its Applications", 
                 "Maxwell's 1st Equation", "Electrostatic Boundary-Value Problems"]
    elif unit == "Unit 2: Magnetostatics":
        topics = ["Biot-Savart's Law", "Magnetic Flux Density", 
                 "Inductors and Inductances", "Magnetic Boundary Conditions"]
    elif unit == "Unit 3: Maxwell's Equations and EM Waves":
        topics = ["Faraday's Law", "Maxwell's Equations", 
                 "EM Waves in Lossy Dielectrics", "Power & Poynting Vector"]
    elif unit == "Unit 4: Quantum Physics":
        topics = ["Photoelectric Effect", "Uncertainty Principle", 
                 "Schrödinger Wave Equation", "Introduction to Nanoscience"]

    # Loop through each topic in the topics list
    # Create a button for each topic but make it disabled (unclickable)
    # state=DISABLED makes button grayed out and non-functional
    for topic in topics:
        Button(frame, text=topic, width=40, state=DISABLED).pack(pady=5)

# Function to display main unit selection screen
def show_units():
    # Clear frame completely to remove any existing content
    for widget in frame.winfo_children():
        widget.destroy()

    # List containing all available units as strings
    # Each string exactly matches what will be passed to show_topics() function
    units = ["Unit 1: Vectors, Fields, and Electrostatics", 
             "Unit 2: Magnetostatics", 
             "Unit 3: Maxwell's Equations and EM Waves", 
             "Unit 4: Quantum Physics"]

    # Create a button for each unit in the units list
    # lambda u=unit: creates anonymous function that captures current unit value
    # Without u=unit, all buttons would use the last unit value (closure problem)
    # lambda u=unit: show_topics(u) ensures each button passes correct unit
    for unit in units:
        Button(frame, text=unit, width=40, command=lambda u=unit: show_topics(u)).pack(pady=10)

# Create main application window
window = Tk()
window.geometry("700x600")  # Set window dimensions: 700 pixels wide, 600 pixels tall

# Create main title label attached to window (not frame)
# This label stays visible throughout the application
label_title = Label(window, text="Electromagnetic Theory and Quantum Physics", 
                   font=("Arial", 20), pady=10)
label_title.pack()  # Add title to top of window

# Create frame widget that will hold dynamic content
# Frame acts as container that can be cleared and refilled with different content
frame = Frame(window)
frame.pack(pady=20)  # Add frame to window with 20 pixels vertical spacing

# Initialize application by showing unit selection screen
# This is the starting point - user sees list of units when program runs
show_units()

# Start tkinter main event loop
# This keeps window open and responsive to user interactions
window.mainloop()