from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("700x600")
window.config(bg='#f0f0f0')

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar,tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()  # Separator
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Zoom In")
view_menu.add_command(label="Zoom Out")
menu_bar.add_cascade(label="View", menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About Us")
menu_bar.add_cascade(label="About", menu=about_menu)

window.config(menu=menu_bar)

label_title = Label(window,
                    text="DATASTORE",
                    font=('Helvetica', 38, 'bold'),
                    fg='#003366',
                    bg='#f0f0f0')
label_title.pack(anchor='center', pady=40)

label_username = Label(window,
                       text="Username",
                       font=('Helvetica', 22),
                       fg='black',
                       bg='#f0f0f0')
label_username.pack(anchor='w', padx=40)

entry_username = Entry(window,
                       font=('Helvetica', 22),
                       bg='white',
                       width=20)
entry_username.pack(anchor='w', padx=40, pady=10)

label_password = Label(window,
                       text="Password",
                       font=('Helvetica', 22),
                       fg='black',
                       bg='#f0f0f0')
label_password.pack(anchor='w', padx=40, pady=(20, 0))

entry_password = Entry(window,
                       font=('Helvetica', 22),
                       bg='white',
                       width=20,
                       show='*')
entry_password.pack(anchor='w', padx=40, pady=10)

def login():
    username = entry_username.get()
    messagebox.showinfo("Login Successful", f"Hello {username}, you have been logged in successfully")

submit_button = Button(window,
                       text="Submit",
                       font=('Helvetica', 18, 'bold'),
                       bg='#004080',
                       fg='white',
                       width=12,
                       command=login)
submit_button.pack(anchor='center', pady=40)

window.mainloop()