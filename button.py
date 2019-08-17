from tkinter import *
def hello():
    print("Hello World")
def print_me():
    print("Print it")
root = Tk()
root.geometry("500x400")

f1 = Frame(root, borderwidth=3, bg="grey", relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

b1 = Button(f1, fg="green", text="Click me!", bg="white", command=hello)
b1.pack(side=LEFT, padx=23, pady=10)

b2 = Button(f1, fg="white", text="Click me!", bg="green", command=print_me)
b2.pack(side=LEFT, pady=10)




root.mainloop()