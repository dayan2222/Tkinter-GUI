from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("GUI")
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar = self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def create_button(self, inptext):
        Button(self, text = inptext, command = self.click).pack()

    def click(self):
        print("Button Clicked")

if __name__ == '__main__':
    window  = GUI()
    window.status()
    window.create_button("Click me")
    window.mainloop()