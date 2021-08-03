from tkinter import*
root =Tk()
frame = LabelFrame(root,text="My frame",padx=60,pady=60)
frame.pack(padx=15,pady=15)

btn =Button(frame,text="Harry")
btn.grid(row=0,column=0)
mainloop()