from tkinter import *
import fontawesome as fa
root = Tk()

root.title("Lets Draw Lines")
width = 900
height = 850
root.configure(background='black')#ABEBC6
root.wm_iconbitmap("line.ico")
root.geometry(f"{width}x{height}")
root.maxsize(width,height)
root.minsize(width,height)
x1_value = StringVar()
x2_value = StringVar()
y1_value = StringVar()
y2_value = StringVar()
#"""
def new_winF(): 
    new_win = Toplevel(root)

    Label(new_win, text="Lets Draw the line", fg="#34495E", font="Times 18 bold", pady=10 ).grid(row=1, column=0, columnspan=5)

    Label(new_win, text="Value of X1-axis",font="Helvetica 12 bold", fg="#424949").grid(row=2, column=0)
    #x1_value = StringVar()
    Entry(new_win, textvariable=x1_value).grid(row=2, column=1)

    Label(new_win, text="Value of Y1-axis", font="Helvetica 12 bold", fg="#424949").grid(row=3, column=0)
    #y1_value = StringVar()
    Entry(new_win, textvariable=y1_value).grid(row=3, column=1)

    Label(new_win, text="Value of X2-axis",font="Helvetica 12 bold", fg="#424949").grid(row=2, column=3)
    #x2_value = StringVar()
    Entry(new_win, textvariable=x2_value).grid(row=2, column=4)

    Label(new_win, text="Value of Y2-axis",font="Helvetica 12 bold", fg="#424949").grid(row=3, column=3)
    #y2_value = StringVar()
    Entry(new_win, textvariable=y2_value).grid(row=3, column=4)

    Button(new_win,text="Draw", command = line, bg="#EBF5FB", fg="#34495E", padx=15).grid(row=4, column= 2)
    font = fa.icons['check']#fas fa-fw fa-tachometer-alt
    Label(new_win,text=f"{font} Completed", fg = "green").grid(row=5, column= 2)
#"""
def line():
    print(f"The value of x1 is {x1_value.get()}, y1 is {y1_value.get()}. The value of x2 is {x2_value.get()}, and the value of y2 is {y2_value.get()}.")

    x1 = x1_value.get()
    y1 = y1_value.get()

    x2 = x2_value.get()
    y2 = y2_value.get()

    canvas_widget_line.create_line(x1, y1, x2, y2, fill="red")

canvas_width = 800
canvas_height = 600

# TODO: Y-Axis
canvas_widget = Canvas(root, width=95, height=600, background='#EBF5FB')
canvas_widget.grid(row=1, column=0)

#  x,y
canvas_widget.create_text(50,10, text="y-axis", fill="green")
# y-axis {(x1,y1), (x2,y2)}
#canvas_widget.create_line(50,600, 50,2, fill="red")

#  x,y , 0,0
canvas_widget.create_text(55,597, text="0", fill="green")
# x-axis {(x1,y1), (x2,y2)}}
canvas_widget.create_line(60,600, 95,600, fill="green")

#  x,y , 0,0
canvas_widget.create_text(50,500, text="500", fill="green")
# x-axis {(x1,y1), (x2,y2)}}
canvas_widget.create_line(60,500, 95,500, fill="green")

#  x,y , 0,0
canvas_widget.create_text(50,400, text="400", fill="green")
# x-axis {(x1,y1), (x2,y2)}}
canvas_widget.create_line(60,400, 95,400, fill="green")

#  x,y , 0,0
canvas_widget.create_text(50,300, text="300", fill="green")
# x-axis {(x1,y1), (x2,y2)}}
canvas_widget.create_line(60,300, 95,300, fill="green")

#  x,y , 0,0
canvas_widget.create_text(50,200, text="200", fill="green")
# x-axis {(x1,y1), (x2,y2)}}
canvas_widget.create_line(60,200, 95,200, fill="green")

#  x,y , 0,0
canvas_widget.create_text(50,100, text="100", fill="green")
# x-axis {(x1,y1), (x2,y2)}}
canvas_widget.create_line(60,100, 95,100, fill="green")

# TODO: Common Graph

# width=800, height=590,
canvas_widget_line = Canvas(root, width=canvas_width, height=canvas_height, background='#EBF5FB')
canvas_widget_line.grid(row=1, column=1, columnspan=5)#pack()

# TODO: X-Axis

canvas_widget = Canvas(root, width=900, height=50, background='#EBF5FB')
canvas_widget.grid(row=0, column=0, columnspan=6, pady=1)
# Define the coordinate of x,y only
canvas_widget.create_text(880,20, text="x-axis", fill="red")

#  x,y , 0,0
canvas_widget.create_text(800,45, text="700", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(800,0, 800,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(700,45, text="600", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(700,0, 700,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(600,45, text="500", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(600,0, 600,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(500,45, text="400", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(500,0, 500,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(400,45, text="300", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(400,0, 400,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(300,45, text="200", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(300,0, 300,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(200,45, text="100", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(200,0, 200,35, fill="red")


#  x,y , 0,0
canvas_widget.create_text(100,45, text="0", fill="green")
# y-axis {(x1,y1), (x2,y2)}
canvas_widget.create_line(99,0, 99,35, fill="black")


# TODO: BUTTOn
Button(root,text="Start Drawing", command=new_winF, bg="#EBF5FB", fg="#34495E", padx=15, pady=10).grid(row=3, column=3,pady=10)

root.mainloop()