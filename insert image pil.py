from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title('image')

root.iconbitmap('you.png')
button_click=Button(root,text='click',)
button_click.pack()

my_image=ImageTk.PhotoImage(Image.open('you.png'))
my_label=Label(image=my_image)
my_label.pack()

button_quit=Button(root,text='EXIT',command=root.quit,)
button_quit.pack()
root.mainloop()
