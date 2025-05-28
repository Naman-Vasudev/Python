from tkinter import *
#It is used to place the widget in a window and organizes the widget’s positions based on row and column pattern
'''Options
row, column- row index and column index
padx, pady- horizontal and vertical space
Columnspan, rowspan '''
window=Tk()
titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2) #columnspan shows how many columns it can take

firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0,sticky=W)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0,sticky=E) #STICKY SHOWS RELATIVE POSITION
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)
window.mainloop()