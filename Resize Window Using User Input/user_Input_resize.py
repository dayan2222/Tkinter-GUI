from tkinter import ttk
import tkinter as tk


def apply():
    width = entry1.get()
    height = entry2.get()
    root.geometry(f"{width}x{height}")


root = tk.Tk()
root.title("Problem 1")
root.geometry("300x200")
# labels
ttk.Label(root, text="Enter width ", padding=10).grid(row=0, column=0)
ttk.Label(root, text="Enter height ", padding=10).grid(row=0, column=1)
# Entry
entryVar1 = tk.IntVar()
entry1 = ttk.Entry(root, width=10, textvariable=entryVar1)
entry1.grid(row=1, column=0, padx=10)

entryVar2 = tk.IntVar()
entry2 = ttk.Entry(root, textvariable=entryVar2, width=10)
entry2.grid(row=1, column=1, padx=10)

# button
button = ttk.Button(root, text="Apply", command=apply, padding=5)
button.grid(row=2, column=1, pady=10)

root.mainloop()


