from tkinter import *
root = Tk()
#Button without any functions
myButton=Button(root,text="Click Me")
myButton.pack()

#state disabled button
myButton1= Button(root,text="click",state=DISABLED)
myButton1.pack()
#button x and y padding
myButton2= Button(root,text="click",padx=50)
myButton2.pack()
myButton3= Button(root,text="click",padx=50,pady=50)
myButton3.pack()
root.mainloop()