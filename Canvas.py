from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas GUI")
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
canvas_widget = Canvas(root, width=canvas_width, height=canvas_height)
canvas_widget.pack()

# Define the coordinate of x,y only
canvas_widget.create_text(780,370, text="x-axis", fill="red")
# The line goes from the point x1, y1 to x2, y2
# x-axis {(x1,y1), (x2,y2)},{(5,380), (800,380)}
canvas_widget.create_line(5,380, 800,380, fill="green")
canvas_widget.create_text(35,10, text="y-axis", fill="green")
# y-axis {(x1,y1), (x2,y2)},{(15,400), (15,2)}
canvas_widget.create_line(15,400, 15,2, fill="red")
# rectangle text
canvas_widget.create_text(400,365, text="Rectangle", fill="DarkGoldenRod")
# To create rectangle specify parameters in this order - co-ordinate of top left & co-ordinate of bottom right
# {(x-of top left,y1-of top left),(x2-of bottom right,y2-of bottom right)}, {(55,25),(750,350)}
canvas_widget.create_rectangle(55, 25, 750, 355, fill="LightGray")
# oval
canvas_widget.create_oval(250, 35, 550, 335, fill="MintCream")
# oval text
canvas_widget.create_text(400,345, text="Oval", fill="Navy")
root.mainloop()