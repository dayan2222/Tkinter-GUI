from tkinter import *

def status():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now...")

root = Tk()
root.geometry("300x300")
root.title("Status Bar")

statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Click me to check the status!", command=status).pack()

root.mainloop()