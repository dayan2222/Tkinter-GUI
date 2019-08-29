from tkinter import *
root = Tk()
root.geometry("300x300")
root.title("List Box")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1

i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of List")

Button(root, text="Add item", command=add).pack()

root.mainloop()