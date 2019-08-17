from tkinter import *
root = Tk()

root.geometry("500x400")
root.title("My GUI")

# Important Label Options
# text - add the text
# bd - background
# fg - foreground
# font - set the font
# 1. font=("comicsansms", 19, "bold")
# 2. font=("comicsansms 19 bold")

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text="Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia. \n It is the world’s sixth-most populous country with a population exceeding 212,742,631 people. \n In area, it is the 33rd-largest country, spanning 881,913 square kilometres", bg="green", fg="white", padx=13, pady=50, font=("comicsansms 12 bold"), borderwidth=3, relief=SUNKEN)


# Important Pack Options
# anchor = nw, ne, se, sw (NorthEast, SouthEast....)
# side = top, bottom, left, right
# fill - fill=X,Y
# padx
# pady

title_label.pack(side=TOP, anchor="nw", fill=X)


bottom_label = Label(text="I'm ready!", bg="green", fg="white", padx=13, pady=50, font=("comicsansms 9 bold"), borderwidth=3, relief=SUNKEN)
bottom_label.pack(side=BOTTOM, anchor="sw", fill=X, padx=34, pady=12)
root.mainloop()
