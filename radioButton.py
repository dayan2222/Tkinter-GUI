from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x400")
root.title("Radio Button")

def order():
    tmsg.showinfo("Order Received", f"We've received order for {var.get()}.\nThanks for ordering!")
var = StringVar()
var.set("Radio")
# var = IntVar()
Label(root,text="What would you like to have sir?",font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="PIZZA", padx=14, variable = var, value="PIZZA").pack(anchor="w")
radio = Radiobutton(root, text="Burger", padx=14, variable = var, value="Burger").pack(anchor="w")
radio = Radiobutton(root, text="Chicken Grill", padx=14, variable = var, value="Chicken Grill").pack(anchor="w")
radio = Radiobutton(root, text="Broast", padx=14, variable = var, value="Broast").pack(anchor="w")
Button(root, text="Order Now", command=order).pack()
root.mainloop()

"""
# Radio Button with For loop
var = StringVar()
var.set("Radio")
list = ["Chowmin", "Pasta", "Menchuriun", "Chilli", "Burger"]

for item in list:
    radio = Radiobutton(root, text=f"{item}", variable=var, value=f"{item}", font="lucida 9").pack(anchor="w")
"""