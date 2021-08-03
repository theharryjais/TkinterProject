from tkinter import *
root = Tk()
# add widgets here
redbutton = Button(root,text = "LEFT", fg = "green")
#shoving it onto the screen
redbutton.pack( side = LEFT)
greenbutton = Button(root,text = "RIGHT",fg = "black")
greenbutton.pack(side = RIGHT)
bluebutton = Button(root,text = "TOP",fg = "blue")
bluebutton.pack(side = TOP)
blackbutton = Button(root,text = "BOTTOM",fg = "black")
blackbutton.pack(side = BOTTOM)
root.mainloop()


