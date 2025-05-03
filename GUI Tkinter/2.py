from tkinter import *
window =Tk()

label=Label(window,
            text="Hello World",
            font=('Arial',40,'bold'),
            fg='#00FF00',
            bg='black',
            relief=RAISED, # Border Style
            bd=10,#bd option sets width or stroke of the border around the outside of the button.
            padx=20, # It shows the distance between x/y axes and border
            pady=20,
            compound='bottom') #Relative position of image wrt to text

# label.pack() by default center
label.place(x=0,y=0)

window.mainloop()