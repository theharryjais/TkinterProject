from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root= Tk()
root.title('Message Box')

def popup():
    #showing messagebox
    messagebox.showinfo("This is my  Popup","Harry jaiswal")

Button(root,text="Popup",command=popup).pack()
mainloop()