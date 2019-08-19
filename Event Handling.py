from tkinter import *
root = Tk()
root.geometry("300x300")
root.title("Mouse Events")

def call_me(event):
    print(f"You clicked on the left mouse button at {event.x}, {event.y}")


widget = Button(root, text="Click Me!")
widget.pack()
# bind is the keyword used to bind the mouse events
widget.bind('<Button-1>', call_me)
# <Button-1> = Left Mouse Button
# <Button-2> = Middle Mouse Button
# <Button-3> = Right Mouse Button

# Double is used for double click
widget.bind('<Double-3>', quit)

root.mainloop()