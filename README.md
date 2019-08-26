# Tkinter-GUI
My initial practice code of TKINTER GUI

1- Welcome = Label <br>
2- Image = Declaring Images<br>
3- Attribiutes of Labels<br>
    such as<br>
    
    # Important Label Options
    # text - add the text
    # bd - background
    # fg - foreground
    # font - set the font
    # 1. font=("comicsansms", 19, "bold")
    # 2. font=("comicsansms 19 bold")
    # padx - x padding
    # pady - y padding
    # relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
    # and
    # Important Pack Options
    # anchor = nw, ne, se, sw (NorthEast, SouthEast....)
    # side = top, bottom, left, right
    # fill - fill=X,Y
    # padx
    # pady
    
4- Newspaper using Attribiutes <br>
5- Frames<br>
6- Button <br>

    # We can decalre fucntion in button using "commannd = function_name "
7- Grids <br>
8- CheckBox Buttons along with csv file<br><br>

<center><img src="Login Form.PNG" alt-text="Login Form"></center><br>
9- Canvas GUI<br><br>
<center><img src="Canvas GUI.PNG" alt-text="Login Form"></center><br>
10- Mouse Event Handling<br>
    
     # bind is the keyword used to bind the mouse events
     # <Button-1> = Left Mouse Button
     # <Button-1> = Left Mouse Button
     # <Button-2> = Middle Mouse Button
     # <Button-3> = Right Mouse Button
     # Double is used for double click   

11- Exercise: Newspaper<br>
<center><img src="Newspaper on TKinter/Newspaper.PNG" alt-text="Newspaper"></center><br>
12- Ceaser Cipher using filling.<br>

<center><img src="Cipher/encypt.PNG" alt-text="Encrypt" height="50%"><center>
13- Menus<br>
    
    # Non-Drop Down
    menu = Menu(root)
    menu.add_command(label="File", command=my_function)
    menu.add_command(label="Quit", command=quit)
    root.config(menu=menu)

    # Drop Down
    main_menu = Menu(root)
    # tearoff use to fix the menu
    sub_menu1 = Menu(main_menu, tearoff=0)
    sub_menu1.add_command(label="New", command=my_function)
    # for seprating in menus
    sub_menu1.add_separator()
    sub_menu1.add_command(label="Quit", command=quit)
    root.config(menu=main_menu)
    main_menu.add_cascade(label="File", menu=sub_menu1)
    
14- Mesage Box<br>
    
    # important tags 
    # import tkinter.messagebox as tmsg
    # tmsg.askquestion("Label", "Message")
    # tmsg.showinfo("Label", "Message")
    # tmsg.askretrycancel("Label", "Message")
    # tmsg.showwarning("Label", "Message")
    



