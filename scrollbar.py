from tkinter import *
root = Tk()
root.geometry("300x300")

# For Connecting Scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

"""
# Text 
text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill = BOTH)
"""
# List Box
lbx = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(51):
    lbx.insert(END, f"Item: {i}")
lbx.pack(fill = "both", padx = 22)
scrollbar.config(command=lbx.yview)

root.mainloop()