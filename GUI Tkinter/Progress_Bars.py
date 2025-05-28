from tkinter import *
from tkinter.ttk import *
import time

#Progress Bar. The purpose of this widget is to reassure the user that something is happening. It can operate in one of two modes – • In determinate mode, the widget shows an indicator that moves from beginning to end under program control.
 
#In indeterminate mode, the widget is animated so the user will believe that something is in progress. In this mode, the indicator bounces back and forth between the ends of the widget.

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()