from tkinter import *
root = Tk()
root.geometry("400x400")

def user():
    width = entry_width.get()
    height = entry_height.get()
    root.geometry(f"{width}x{height}")
    result = "Width: " + str(width) + " Height:" + str(height)
    Label(root, text=f"You Entered: {result}", fg="green").grid(row=4, column=1)


# width
entry_width = IntVar()
Label(root, text="Enter Width", padx=10, pady=20).grid(row=0, column=0)
width_input = Entry(root, textvariable=entry_width).grid(row=1, column=0, padx=10, pady=10)

# height
entry_height = IntVar()
Label(root, text="Enter Height", padx=10, pady=20).grid(row=0, column=2)
height_input = Entry(root, textvariable=entry_height).grid(row=1, column=2, padx=10, pady=10)

# Button
b = Button(root, text="Apply", pady=10, padx= 10, command=user, fg="Brown", bg="White").grid(row=2, column=1, pady=12)
root.mainloop()

