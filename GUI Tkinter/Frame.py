from tkinter import *  # Import all tkinter functions and classes

# Basic function to demonstrate button click
def show_content():
    print("Button clicked!")  # This prints to console when button is pressed

# Function to clear frame and add new content dynamically
def change_content():
    # .winfo_children() gets list of all widgets inside the frame
    # .destroy() removes each widget from the frame completely
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Create new label widget and add it to the frame
    # font=("Arial", 12) sets the font family and size
    new_label = Label(frame, text="New content added!", font=("Arial", 12))
    new_label.pack(pady=10)  # pady=10 adds 10 pixels padding above and below
    
    # Create new button that calls reset_content function when clicked
    # command= tells button which function to run when clicked
    new_button = Button(frame, text="Go Back", command=reset_content)
    new_button.pack(pady=5)

# Function to reset frame back to original content
def reset_content():
    # Clear all widgets from frame again
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Recreate the original button
    original_button = Button(frame, text="Click to Change Content", command=change_content)
    original_button.pack(pady=10)

# Create main window object
window = Tk()
window.geometry("400x300")  # Set window size: width x height in pixels

# Create title label at top of window
# This label is attached to main window, not the frame
title_label = Label(window, text="Frame Tutorial", font=("Arial", 16))
title_label.pack(pady=20)  # Add 20 pixels spacing above and below title

# Create a frame widget - this is like a container box inside the window
# Frame holds other widgets and can be cleared/refilled dynamically
frame = Frame(window)
frame.pack(pady=20)  # Add the frame to window with 20 pixels spacing

# Add initial button to the frame when program starts
initial_button = Button(frame, text="Click to Change Content", command=change_content)
initial_button.pack(pady=10)

# Start the tkinter event loop - keeps window open and responsive
window.mainloop()