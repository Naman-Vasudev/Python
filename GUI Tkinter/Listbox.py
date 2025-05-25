#Listbox= A listing of selectable text items within its own container
from tkinter import *

def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("YOU HAVE ORDERED: ")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size()) # ADJUSTS SIZE DYNAMICALLY

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size()) # ADJUSTS SIZE DYNAMICALLY

window=Tk()
listbox=Listbox(window,bg='#f7ffde',font=('Constantia',35),
                width=15,
                selectmode=MULTIPLE # MORE THAN 1 item, if you don't write this default is 1.
                )

food_menu=['Pizza','Hamburger','Soup and Salad','Garlic Bread']
for index,food in enumerate(food_menu,start=1):
    listbox.insert(index,food)

listbox.config(height=listbox.size()) # ADJUSTS SIZE DYNAMICALLY
listbox.pack()

entrybox=Entry(window)
entrybox.config(font=("Arial",35))
entrybox.pack()

submit_button=Button(window)
submit_button.config(text="SUMBIT",font=('Consolas',20),command=submit)
submit_button.pack()

add_button=Button(window)
add_button.config(text="ADD this item",font=('Consolas',20),command=add)
add_button.pack()

del_button=Button(window)
del_button.config(text="DELETE this item",font=('Consolas',20),command=delete)
del_button.pack()



window.mainloop()