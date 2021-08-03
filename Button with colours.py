from tkinter import *
root = Tk()
def  myClick():
    myLabel = Label(root,text="Button is clicked!!")
    myLabel.pack()
myButton=Button(root,text="CLICK",command=myClick,fg="green",bg="red")
myButton.pack()
root.mainloop()