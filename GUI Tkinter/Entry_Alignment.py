from tkinter import *

# Create the main window
window = Tk()
window.geometry("600x400")
window.config(bg="lightgray")
window.title("Tkinter Positioning Demo")

# ---------------------------------------------
# Using pack() for simple alignment
# This method automatically positions widgets from top to bottom by default.
# You can change alignment using 'side' and 'anchor' options.

# Label with pack() - center alignment by default
label1 = Label(window, text="This is a label using pack()", font=("Arial", 16), bg="yellow")
label1.pack(pady=20)  # pady adds vertical padding between widgets

# Button with pack() - align it to the left side
button1 = Button(window, text="Left Aligned Button", font=("Arial", 16), bg="lightblue")
button1.pack(side="left", padx=20)  # padx adds horizontal padding

# Entry with pack() - aligns to the top by default
entry1 = Entry(window, font=("Arial", 16))
entry1.pack(pady=20)

# -------------------------------
# Using place() for absolute positioning
# This method uses x, y coordinates to position widgets.

# Label with place() - positioned at a specific coordinate
label3 = Label(window, text="This label is placed using place()", font=("Arial", 16), bg="lightyellow")
label3.place(x=150, y=200)

# Button with place() - positioned using x and y
button3 = Button(window, text="Placed Button", font=("Arial", 16), bg="orange")
button3.place(x=100, y=300)

# Entry with place() - positioned at a fixed location
entry3 = Entry(window, font=("Arial", 16))
entry3.place(x=250, y=300)

# -------------------------------
# Using anchor for text alignment
# The anchor option specifies the alignment of the widget's content inside its space.

# Label with anchor - aligned text to the top-left corner
label4 = Label(window, text="This label has anchor='nw' (top-left)", font=("Arial", 16), bg="lightblue")
label4.pack(anchor="nw", padx=10, pady=10)

# Run the window
window.mainloop()
