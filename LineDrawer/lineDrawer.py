from tkinter import *
root = Tk()
canvas_width = 800
canvas_height = 750

root.title("Lets Draw Lines")
root.configure(background='#ABEBC6')
root.geometry(f"{canvas_width}x{canvas_height}")
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)

def line():
    print(f"The value of x1 is {x1_value.get()}, y1 is {y1_value.get()}. The value of x2 is {x2_value.get()}, and the value of y2 is {y2_value.get()}.")
    x1 = x1_value.get()
    y1 = y1_value.get()

    x2 = x2_value.get()
    y2 = y2_value.get()

    canvas_widget.create_line(x1, y1, x2, y2, fill="red")




canvas_widget = Canvas(root, width=800, height=590, background='#EBF5FB')
canvas_widget.grid(row=0, column=0, columnspan=5)#pack()

# The line goes from the point x1, y1 to x2, y2
# x-axis {(x1,y1), (x2,y2)},{(5,380), (800,380)}
canvas_widget.create_line(5,550, 800,550, fill="green")
# canvas_widget.create_text(35,10, text="y-axis", fill="green")
# y-axis {(x1,y1), (x2,y2)},{(15,400), (15,2)}
canvas_widget.create_line(15,580, 15,2, fill="red")


Label(root, text="Lets Draw the line",bg="#ABEBC6", fg="#34495E", font="Times 18 bold", pady=10 ).grid(row=1, column=0, columnspan=5)

Label(root, text="Value of X1-axis",bg="#ABEBC6",font="Helvetica 12 bold", fg="#424949").grid(row=2, column=0)
x1_value = StringVar()
Entry(root, textvariable=x1_value).grid(row=2, column=1)

Label(root, text="Value of Y1-axis",bg="#ABEBC6", font="Helvetica 12 bold", fg="#424949").grid(row=3, column=0)
y1_value = StringVar()
Entry(root, textvariable=y1_value).grid(row=3, column=1)

Label(root, text="Value of X2-axis",bg="#ABEBC6",font="Helvetica 12 bold", fg="#424949").grid(row=2, column=3)
x2_value = StringVar()
Entry(root, textvariable=x2_value).grid(row=2, column=4)

Label(root, text="Value of Y2-axis",bg="#ABEBC6",font="Helvetica 12 bold", fg="#424949").grid(row=3, column=3)
y2_value = StringVar()
Entry(root, textvariable=y2_value).grid(row=3, column=4)

Button(root,text="Draw", command = line).grid(row=4, column= 2)
Label(root,text="Under Construction", fg = "red").grid(row=5, column= 2)

root.mainloop()