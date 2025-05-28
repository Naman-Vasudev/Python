from tkinter import *

def display():
    print("Menu item clicked!")

window = Tk()
window.geometry("400x300")

# Create menu bar
menu_bar = Menu(window)

# Create File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=display)
file_menu.add_command(label="Open", command=display)
file_menu.add_command(label="Save", command=display)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu) #LIKE PACK/PLACE menu arg specifies which hierachy to follow

# Create Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=display)
edit_menu.add_command(label="Copy", command=display)
edit_menu.add_command(label="Paste", command=display)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Configure window to use menu bar
window.config(menu=menu_bar)

# Add a simple label
label = Label(window, text="Basic Menu Example", font=('Arial', 16))
label.pack(pady=50)

window.mainloop()