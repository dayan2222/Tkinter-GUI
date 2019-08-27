from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.title("Give us Your Precious Feedback")
root.configure(background='#F4ECF7')

def rating():
    name = name_value.get()
    contact = contact_value.get()
    rate = rating_scale.get()
    with open("feedback.txt", "a") as f:
        f.write(f"\nName: {name}\nContact No: {contact}\nRating: {rate}")
        tmsg.showinfo("Thank You", f"Thanks for Rating us {rate}!")


# heading
Label(root, text="Fair Restaurant", pady=25, fg="#2980B9",bg="#F4ECF7", font="algerian 18 bold").grid(row=0, column=1)
# form_Label
Label(root, text="Feedback Form",fg="#2980B9",bg="#F4ECF7", font="Helvetica 16 italic").grid(row=1, column=1, pady=10)
# Fields

name_value = StringVar()
contact_value = StringVar()

Label(root, text="Name: ",bg="#F4ECF7", fg="#2980B9", font="Helvetica 12 italic").grid(row=2, column=0)
name_entry = Entry(root, textvariable=name_value,bg="#D4E6F1", fg="#2980B9").grid(row=2, column=1)

Label(root, text="Contact No: ",bg="#F4ECF7", fg="#2980B9", font="Helvetica 12 italic").grid(row=3, column=0)
contact_entry = Entry(root, textvariable=contact_value, bg="#D4E6F1", fg="#2980B9").grid(row=3, column=1)

Label(root, text="Rating: ",bg="#F4ECF7", fg="#2980B9", font="Helvetica 12 italic").grid(row=4, column=0)
rating_scale = Scale(root,fg="#2980B9", from_=0, to=10, tickinterval=5, orient=HORIZONTAL)
rating_scale.set(5)
rating_scale.grid(row=4, column=1)

Button(root, text="Submit Rating", bg = "#2980B9" , fg="#F4ECF7", padx=5, pady =10 , command=rating).grid(row=5, column=1,pady=5)

root.mainloop()