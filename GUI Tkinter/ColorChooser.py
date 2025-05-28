from tkinter import *
from tkinter import colorchooser #sub-module

def click():
    color=colorchooser.askcolor() #stores as a tuple
    print(type(color))
    window.config(bg=f'{color[1]}') # to change background color
window=Tk()

window.geometry("420x420")
button=Button(text='click me', command=click)
button.pack()
window.mainloop()