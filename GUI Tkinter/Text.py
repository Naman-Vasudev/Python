from tkinter import *
#widgets = GUI elements: buttons, textboxes, labels, images
# #windows serves as a container to hold or contain these widgets
window=Tk() # instantiate a instance of a window

window.geometry("420x420") #size
window.title("Naman's first GUI") #Title (default is Tk)
window.config(background="#bdebf0") # Put hex value


textbox=Text(window,width=40,height=20,xscrollcommand="",yscrollcommand="") #To conmect a scrollbar widget
textbox.pack()

window.mainloop() # Places window on the screen