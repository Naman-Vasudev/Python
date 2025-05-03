from tkinter import *

# List of food items
food = ["pizza", "hamburger", "hotdog"]

# Define the function to handle the selection and print the order
def order():
    # Create a list of order messages
    order = ["You bought the pizza!", "You bought the hamburger!", "You bought the hotdog!"]
    
    # Print the message based on the index selected by the user
    print(order[x.get()])  # x.get() returns the index of the selected radio button (0, 1, or 2)

# Initialize the main window
window = Tk()

# Create an IntVar to track the selected radio button
x = IntVar()

# Loop through each food item to create the corresponding radio button
for index in range(len(food)):
    # Create a Radiobutton for each food item
    radiobutton = Radiobutton(window,
                              text=food[index],  # Add the food name as text to the radio button
                              variable=x,  # Group all radio buttons under the same variable x
                              value=index,  # Assign a unique value (0, 1, or 2) to each radio button
                              padx=25,  # Add padding on the x-axis
                              font=("Impact", 50),  # Set the font size and style
                              compound='left',  # Display the text and image on the left side
                              command=order)  # Call the order function when a radio button is selected
    radiobutton.pack(anchor=W)  # Pack the radio button to the window

# Run the Tkinter event loop to display the window
window.mainloop()
