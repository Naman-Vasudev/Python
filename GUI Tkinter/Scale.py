from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get())+ " degrees C")

window=Tk()

scale=Scale(window,from_=100,
            to=0,
            length=600,
            orient=VERTICAL,
            font=('Consolas',20),
            tickinterval=10, #This adds numeric indicators for the values for scale mentioned as tickinterval
            #showvalue=0,hide current value,

            #Cosmetic Changes
            troughcolor='blue',
            fg='red',
            bg='black'

            )
scale.set(((scale['from']-scale['to'])/2)+scale['to']) # set current value of slider 
scale.pack()

button=Button(window,text='Submit',font=('Consolas',10),command=submit)
button.pack()

window.mainloop()