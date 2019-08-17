from tkinter import *
import csv
root = Tk()

def submit():
    with open("check_box.csv", "a", newline="") as f:
        sub = csv.writer(f, delimiter=",")
        sub.writerow([username_value.get(), password_value.get(), remember_value.get()])
    print("Function Complete")
    done.grid(row=5, column=1)
    print("Submitted")


root.geometry("400x300")
root.title("Login Form")
root.maxsize(400, 400)
root.minsize(300, 300)
Label(root, text="Login Form", font="comicsansms 22 bold", pady=15, fg="Green" ).grid(row=0, column=1)

username = Label(root,text="Username").grid(row=1, column=0)
password = Label(root,text="Password").grid(row=2, column=0)

# value
username_value = StringVar()
password_value = StringVar()
remember_value = IntVar()

# Entries
username_entry = Entry(root, textvariable=username_value).grid(row=1, column=1)
password_entry = Entry(root, textvariable=password_value).grid(row=2, column=1)

# checkbox
remember_entry = Checkbutton(text="Remember Password?", variable = remember_value).grid(row=3, column=1)

# Button
Button(text = "Login", command=submit, bg="Green", fg="white").grid(row=4, column=1)

# Done
done = Label(root, text="Your Data is Submitted!", fg="green", bg="white")

root.mainloop()