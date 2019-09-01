from tkinter import *

root = Tk()
def pr():
    print("Button clicked!")
def new_winF(): # new window definition
    newwin = Toplevel(root)


button1 =Button(root, text ="open new window", command =new_winF) #command linked
button1.pack()

root.mainloop()