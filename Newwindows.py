from tkinter import *
from tkinter import messagebox
top = Toplevel()
top.title('Check new window')
#creating new windows


def open():
    top= Toplevel()
    top.title('Check new window')
    MyLabel= Label(top, text='This is a new window').pack()
btn2=Button(top,text="Close window",command=top.destroy).pack()
btn=Button(top,text="Open",command=open).pack()
mainloop()