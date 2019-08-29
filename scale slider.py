from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x500")

def rate():
    tmsg.showinfo("Thanks", f"Thanks for Giving us {horizontal_slider.get()} this rating!")

# Vertical Slider
# Default Slider is Vertical
Label(root, text="Vertical Slider").pack()
vertical_slider = Scale(root, from_=0, to=100, tickinterval=50) # tickinterval used to show the division of scale
vertical_slider.set(50) # Where the slider is start
vertical_slider.pack()

# Horizontal Slider
Label(root, text="Horizontal Slider").pack()
horizontal_slider = Scale(root, from_=0, to=10, tickinterval=5, orient=HORIZONTAL) # orient is used to show horizontal scale
horizontal_slider.set(5) # Where the slider is start
horizontal_slider.pack()

Button(root, text="Click to Rate", command=rate).pack()

root.mainloop()