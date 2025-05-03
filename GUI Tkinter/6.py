from tkinter import *
from tkinter import messagebox  # Used to show pop-up message box

# Create the main window
window = Tk()
window.geometry("700x600")          # Set fixed size of the window: 700px width, 600px height
window.config(bg='#f0f0f0')         # Set background color to a light gray

# ----------------------------------------
# Title Label - Aligned to the center
# ----------------------------------------
label_title = Label(window,
                    text="DATASTORE",             # Text displayed
                    font=('Helvetica', 38, 'bold'),  # Font family, size, style
                    fg='#003366',                # Text color: dark blue
                    bg='#f0f0f0')                # Background same as window for blending
label_title.pack(anchor='center', pady=40)
# .pack() → Geometry manager that places widget in the window
# anchor='center' → Aligns the label to the center horizontally
# pady=40 → Adds 40px vertical space above and below the label

# ----------------------------------------
# Username Label - Aligned to the left
# ----------------------------------------
label_username = Label(window,
                       text="Username",
                       font=('Helvetica', 22),
                       fg='black',
                       bg='#f0f0f0')
label_username.pack(anchor='w', padx=40)
# anchor='w' → Aligns to the west (left side) of the window
# padx=40 → Horizontal padding from the left edge

# ----------------------------------------
# Username Entry Box - Aligned left
# ----------------------------------------
entry_username = Entry(window,
                       font=('Helvetica', 22),
                       bg='white',       # White background for input area
                       width=20)         # Width is in number of characters
entry_username.pack(anchor='w', padx=40, pady=10)
# pady=10 → Adds vertical space between this and label above

# ----------------------------------------
# Password Label - Aligned to the left
# ----------------------------------------
label_password = Label(window,
                       text="Password",
                       font=('Helvetica', 22),
                       fg='black',
                       bg='#f0f0f0')
label_password.pack(anchor='w', padx=40, pady=(20, 0))
# pady=(20, 0) → 20px padding on top only, no bottom padding

# ----------------------------------------
# Password Entry Box - Aligned to the left
# ----------------------------------------
entry_password = Entry(window,
                       font=('Helvetica', 22),
                       bg='white',
                       width=20,
                       show='*')   # show='*' masks characters for password security
entry_password.pack(anchor='w', padx=40, pady=10)

# ----------------------------------------
# Function to be called on Submit
# ----------------------------------------
def login():
    username = entry_username.get()  # Get text from username entry box
    # Pop-up info box with greeting
    messagebox.showinfo("Login Successful", f"Hello {username}, you have been logged in successfully")

# ----------------------------------------
# Submit Button - Center aligned
# ----------------------------------------
submit_button = Button(window,
                       text="Submit",              # Button text
                       font=('Helvetica', 18, 'bold'),
                       bg='#004080',               # Button background color (navy blue)
                       fg='white',                 # Text color
                       width=12,                   # Width in characters
                       command=login)              # Executes login() when clicked
submit_button.pack(anchor='center', pady=40)
# anchor='center' aligns button to the center horizontally
# pady=40 → adds vertical spacing above and below the button

# Run the GUI loop
window.mainloop()
