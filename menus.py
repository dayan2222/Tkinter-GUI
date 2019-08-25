from tkinter import *
root= Tk()
def my_function():
    print("Hello World!")

# Non-Drop Down
# menu = Menu(root)
# menu.add_command(label="File", command=my_function)
# menu.add_command(label="Quit", command=quit)
# root.config(menu=menu)

# Drop Down
main_menu = Menu(root)

sub_menu1 = Menu(main_menu, tearoff=0)
sub_menu1.add_command(label="New", command=my_function)
sub_menu1.add_separator()
sub_menu1.add_command(label="Quit", command=quit)
root.config(menu=main_menu)
main_menu.add_cascade(label="File", menu=sub_menu1)

sub_menu2 = Menu(main_menu, tearoff=0)
sub_menu2.add_command(label="Test1", command=my_function)
sub_menu2.add_separator()
sub_menu2.add_command(label="Quit", command=quit)
root.config(menu=main_menu)
main_menu.add_cascade(label="Test", menu=sub_menu2)

root.mainloop()