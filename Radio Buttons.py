from tkinter import *
from PIL import ImageTk, Image
root= Tk()
root.title('Radio Button')

#creating modes for radiou button
MODES= [
    ("Pepperoni","Pepperoni"),
    ("Cheese", "Cheese"),
    ("Book", "Book"),
    ("Onion", "Onion")


]
Pizza = StringVar()
Pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root,text=text,variable=Pizza,value=mode).pack(anchor=W)

#function clicked
    def clicked(value):
        myLabel = Label(root,text=value)
        myLabel.pack()

myButton = Button(root,text='Click',command=lambda:clicked(Pizza.get())).pack()
mainloop()



