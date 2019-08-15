from tkinter import *
from PIL import Image, ImageTk
root = Tk()
# width x height
root.geometry("1255x944")

# using PNG Format

photoPNG = PhotoImage(file="baby.png")
photoLabel = Label(image=photoPNG)
photoLabel.pack()
txtPNG = Label(text="This is PNG Picture Format")
txtPNG.pack()

# using PIL

image = Image.open("babyJPG.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()
txt = Label(text="This is JPEG Picture using PIL")
txt.pack()

root.mainloop()

