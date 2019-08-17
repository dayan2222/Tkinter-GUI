from tkinter import *
root = Tk()
root.geometry("655x333")

# Frame declaration
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y, pady=50)

f2 = Frame(root, bg="green", borderwidth="8", relief=GROOVE)
f2.pack(side=TOP, fill=X)

# Labels
l1 = Label(f1, text="This is frame")
l1.pack(pady=142)

l2 = Label(f2, text="This is a Right Side of Frame", fg="white", bg="green")
l2.pack()


root.mainloop()