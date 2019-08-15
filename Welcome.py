from tkinter import *

root = Tk()
# width x height
root.geometry("733x734")
# width , height
root.minsize(300,100)
root.maxsize(1200,988)

# Label
welcome = Label(text=" Welcome to PyCharm ")
welcome.pack()

root.mainloop()