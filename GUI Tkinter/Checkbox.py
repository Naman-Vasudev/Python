from tkinter import *
def display():
    if x.get()==1:
        print("I like Python")
    else:
        print("I don't like pyhton")

window=Tk() 
x=IntVar()
checkbox=Checkbutton(window,text="Python",variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial',20)) #changes the font
checkbox.config(fg='#00FF00') #foreground color
checkbox.config(bg='#000000') #background color
checkbox.config(activeforeground='#0000FF') #active foreground color
checkbox.config(activebackground='#000000') #active background color
window.mainloop()