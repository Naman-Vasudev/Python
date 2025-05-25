#button- You click it it does something
from tkinter import *
count=0
def click():
    global count
    count+=1
    label.config(text=count)
window=Tk()



button=Button(window,text=('Click me !!!'))
button.config(command=click) # Performs call back of fucntion
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#ff6200')
button.config(fg='#fffb1f')
button.place(x=0,y=0)
button.config(activebackground='#ff0000')
button.config(activeforeground='#fffb1f')
# button.config(state=DISABLED) or ACTIVE
label = Label(window,text=count)
label.config(font=('Monospace',50))
label.pack()

window.mainloop()