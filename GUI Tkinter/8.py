from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("Engineering Branch Selection")
window.geometry("500x600")
window.config(bg='#000000')

# List of branch names
branches = ["CSE", "ECE", "EE", "VLSI", "MNC", "AI", "DS", "PROD", "METTA", "CIVIL"]

# Dictionary to store the IntVar() for each branch
vars = {}

# Define the function that will be triggered when the submit button is clicked
def display():
    selected = []
    
    # Check each branch's IntVar() and append the selected branch name to the list
    for branch, var in vars.items():
        if var.get() == 1:
            selected.append(branch)
    
    # Show a message box with the count of selected branches and the names of those branches
    messagebox.showinfo("Branch Selection", f"Dear Student, You have selected {len(selected)} branches: {', '.join(selected)}, good luck!")

# Create checkboxes dynamically using a loop
for branch in branches:
    vars[branch] = IntVar()  # Create an IntVar() for each branch
    checkbox = Checkbutton(window, text=branch, variable=vars[branch], onvalue=1, offvalue=0)
    checkbox.pack(anchor='w')  # Pack the checkbox and align it to the left (west)
    checkbox.config(font=('Arial', 20), fg='#00FF00', bg='#000000', activeforeground='#0000FF', activebackground='#000000')

# Create a submit button to trigger the display function when clicked
submit_button = Button(window, text="Submit", font=('Arial', 20, 'bold'), bg='#004080', fg='white', command=display)
submit_button.pack(anchor='center', pady=20)

# Start the Tkinter event loop to display the window and respond to user interaction
window.mainloop()
