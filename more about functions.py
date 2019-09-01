from tkinter import *
root =Tk()
root.geometry("500x500")
root.title("Title")
root.wm_iconbitmap("1.ico")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width} x {height}")

Button(text="Close", command=root.destroy).pack()


root.mainloop()
