# ====================== Caesar Cipher ======================
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("500x500")
root.minsize(450,450)

def encrypt():

    string = text_value.get()
    string = string.upper()
    ptext = string

    k = key_value.get()

    if k > 26:
        warning="Key Should be Less than or Equals to 26! Try to enter Key value from 1 - 26"
        tmsg.showwarning("Greater than 26", warning)
    else:
        with open("encrypt.txt", "a") as f:
            f.write("\nPlain Text: " + str(ptext) + " Key: " + str(k) + " Encrypted Text: " )
        for i in string:
            #print(i, end = " -> ")
            p = ord(i) - 65

            c = (p + k) % 26
            c = c + 65
            final = chr(c)
            print(final)
            with open("encrypt.txt", "a") as f:
                f.write(final)

        k = str(k)

        with open("encrypt.txt", "r") as f:
             show = f.read()
        Label(root, text=show, fg = "green").grid(row=7, column=1)

# Heading
Label(root, text="Caesar Cipher", font="Helvatica 20 bold", fg="Brown", padx=10, pady=5).grid(row=0,column=1)
# subheading
Label(root, text="Encryption", font="Helvatica 12 italic", fg="Brown", padx=10, pady=0).grid(row=1,column=1)

# Plain text
Label(root, text="Enter text to Encrypt", font="comicsansms 10").grid(row=2,column=0)
text_value = StringVar()
text_input = Entry(root, textvariable=text_value).grid(row=2, column=1)

# Key
Label(root, text="Enter Key", font="comicsansms 10").grid(row=3,column=0)
key_value = IntVar()
key_input = Entry(root, textvariable=key_value).grid(row=3, column=1)


# Button
Button(root,text="Encrypt!", bg="white",padx=10,pady=10, command=encrypt).grid(row=5, column=1, pady=10)




root.mainloop()
