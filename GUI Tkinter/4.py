# Entry widget = Textbox that accepts a single line of user input

from tkinter import *

# Create main window
window = Tk()

# ------------------------
# Entry Widget
# ------------------------

entry = Entry()  # Create entry widget (textbox)

# Configure entry widget
entry.config(font=('Ink Free', 50))       # Set font style and size
entry.config(bg='#00FF00')                # Set background color (green)
entry.config(width=10)                    # Width in number of characters

# Optional configurations (commented):
# entry.insert(0, 'Spongebob')            # Inserts default text at index 0
# entry.config(show='*')                 # Masks input like a password field

entry.pack()  # Add entry widget to the window

# ------------------------
# Functions for Button Actions
# ------------------------

def submit():
    username = entry.get()  # Get current text from entry
    print("Hello", username)  # Print greeting with entered name

def delete():
    entry.delete(0, END)  
    # Deletes all text from index 0 to END
    # 0 → start index
    # END → special tkinter constant representing the end of text

def backspace():
    entry.delete(len(entry.get()) - 1, END)  
    # Deletes only the last character
    # len(entry.get()) - 1 → index of the last character
    # END → delete till the end (only one char in this case)

# ------------------------
# Buttons
# ------------------------

submit = Button(window, text="Submit", command=submit)
submit.pack(side=RIGHT)

delete = Button(window, text="Delete", command=delete)
delete.pack(side=RIGHT)

backspace = Button(window, text="Backspace", command=backspace)
backspace.pack(side=RIGHT)

# Run the GUI loop
window.mainloop()