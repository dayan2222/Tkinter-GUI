from tkinter import *

def get_values():
    with open("sample.txt", "a") as f:
        f.write(f"\n Name: {name_value.get()}\n Father Name: {father_name_value.get()} \n Faculty: {faculty_value.get()} \n Year: {year_value.get()}\n")

    print(f"\n Name: {name_value.get()}\n Father Name: {father_name_value.get()} \n Faculty: {faculty_value.get()} \n Year: {year_value.get()}\n Submitted Successfully!")
    done.grid(row=6, column=1)

root = Tk()
root.geometry("500x400")
f1 = Frame(root, bg="white", borderwidth=5, relief=SUNKEN)
f1.pack(fill=X, padx=10, side=TOP)

head = Label(f1, text="Form", font=("comicsansms 18 italic")).grid(row=0, column=3)
name = Label(f1, text="Name").grid(row=1, column=0)
Father_name = Label(f1, text="Father Name").grid(row=2, column=0)
faculty = Label(f1, text="Faculty").grid(row=3, column=0)
year = Label(f1, text="Year").grid(row=4, column=0)
# Calling Variable Classes
name_value = StringVar()
father_name_value = StringVar()
faculty_value = StringVar()
year_value = IntVar()
# Declaring in Variable
name_entry = Entry(f1, textvariable=name_value).grid(row=1,column=1)
father_name_entry = Entry(f1, textvariable=father_name_value).grid(row=2,column=1)
faculty_entry = Entry(f1, textvariable=faculty_value).grid(row=3,column=1)
year_entry = Entry(f1, textvariable=year_value).grid(row=4,column=1)
# Button
Button(f1, text="Submit", bg="Green", fg="white", command=get_values).grid()
done = Label(f1, text="Your Data is Submitted!", fg="green", bg="white")


root.mainloop()
