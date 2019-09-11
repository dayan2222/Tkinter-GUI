from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
#"window width x window height + position right + position down"
root.geometry("600x400+200+200")
root.configure(background="#3C3F41")
root.wm_iconbitmap("lock.ico")
root.title("Caesar Cipher v.1.1")
text_value = StringVar()
key_value = IntVar()

def encrypt():

    string = text_value.get()
    string = string.upper()
    ptext = string

    k = key_value.get()

    if k > 26 or k == 0:
        warning="Key Should be Less than or Equals to 26! Try to enter Key value from 1 - 26"
        tmsg.showwarning("Invalid key Enter", warning)
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
        Label(root,text="Encryption", font="Times 14 bold",fg="#FFFFFF", bg="#3C3F41").grid(row=4,column=1)
        Label(root, text=show, fg="#E8EAED", bg="#3C3F41", font="Times 12 italic").grid(row=5, column=1)

def decrypt():

    string = text_value.get()
    string = string.upper()
    ptext = string

    k = key_value.get()

    if k > 26 or k == 0:
        warning="Key Should be Less than or Equals to 26! Try to enter Key value from 1 - 26"
        tmsg.showwarning("Invalid key Enter", warning)
    else:
        with open("decrypted.txt", "a") as f:
            f.write("\nEncrypted Text: " + str(ptext) + " Key: " + str(k) + " Decrypted Text: " )
        for i in string:
            #print(i, end = " -> ")
            p = ord(i) - 65

            c = (p - k) % 26
            c = c + 65
            final = chr(c)
            print(final)
            with open("encrypt.txt", "a") as f:
                f.write(final)

        k = str(k)

        with open("encrypt.txt", "r") as f:
             show = f.read()
        Label(root, text="Decryption", font="Times 14 bold", fg="#FFFFFF", bg="#3C3F41").grid(row=4, column=3)
        Label(root, text=show, fg="#E8EAED", bg="#3C3F41", font="Times 12 italic").grid(row=5, column=3)

def encrypt_win():
    root.geometry("1000x400")
    new_win = Toplevel(root)
    new_win.configure(background="#070E16")
    # "window width x window height + position right + position down")
    new_win.geometry("400x300+800+250")
    new_win.maxsize(400, 300)
    new_win.minsize(400, 300)
    new_win.title("Encryption")
    new_win.wm_iconbitmap("lock.ico")
    # Heading
    Label(new_win, text="Caesar Cipher", font="Helvatica 20 bold",fg="#E8EAED", bg="#070E16", padx=10, pady=5).grid(row=0, column=1)
    # subheading
    Label(new_win, text="Encryption", font="Helvatica 12 italic",fg="#E8EAED", bg="#070E16", padx=10, pady=0).grid(row=1, column=1)

    # Plain text
    Label(new_win, text="Enter text to Encrypt",fg="#E8EAED", bg="#070E16",font="comicsansms 10").grid(row=2, column=0)
    #text_value = StringVar()
    text_input = Entry(new_win, textvariable=text_value, fg="#E8EAED", bg="#3C3F41").grid(row=2, column=1)

    # Key
    Label(new_win, text="Enter Key",fg="#E8EAED", bg="#070E16", font="comicsansms 10").grid(row=3, column=0)
    #key_value = IntVar()
    key_input = Entry(new_win, textvariable=key_value, fg="#E8EAED", bg="#3C3F41").grid(row=3, column=1)

    # Button
    Button(new_win, text="Encrypt!", bg="#5DADE2", fg="#F4F6F7", padx=10, pady=10,command=encrypt).grid(row=5, column=1,pady=10)

def decrypt_win():
    root.geometry("1000x400")
    new_win = Toplevel(root)
    new_win.configure(background="#070E16")
    # "window width x window height + position right + position down")
    new_win.geometry("400x300+800+250")
    new_win.geometry("400x300")
    new_win.maxsize(400,300)
    new_win.minsize(400,300)
    new_win.title("Decryption")
    new_win.wm_iconbitmap("lock.ico")
    # Heading
    Label(new_win, text="Caesar Cipher", font="Helvatica 20 bold",fg="#E8EAED", bg="#070E16", padx=10, pady=5).grid(row=0, column=1)
    # subheading
    Label(new_win, text="Decryption", font="Helvatica 12 italic", padx=10, pady=0, fg="#E8EAED", bg="#070E16").grid(row=1, column=1)

    # Plain text
    Label(new_win, text="Enter text to Decrypt", font="comicsansms 10", fg="#E8EAED", bg="#070E16").grid(row=2, column=0)
    #text_value = StringVar()
    text_input = Entry(new_win, textvariable=text_value, fg="#E8EAED", bg="#3C3F41").grid(row=2, column=1)

    # Key
    Label(new_win, text="Enter Key", font="comicsansms 10", fg="#E8EAED", bg="#070E16").grid(row=3, column=0)
    #key_value = IntVar()
    key_input = Entry(new_win, textvariable=key_value, fg="#E8EAED", bg="#3C3F41").grid(row=3, column=1)

    # Button
    Button(new_win, text="Decrypt!", bg="#5DADE2", fg="#F4F6F7", padx=10, pady=10,command=decrypt).grid(row=5, column=1,pady=10)


# TODO: MAIN
Label(root,text="Caesar Cipher", font="Baskerville 18 italic", fg="#E8EAED", bg="#3C3F41", pady=10).grid(row=0,column=2)
Label(root,text="Select anyone of the following", font="Times 16 italic", fg="#E8EAED", bg="#3C3F41", pady=5).grid(row=1,column=2)

# Lock Image
lock = PhotoImage(file=r"C:\Users\Dayan Ahmed\Desktop\Cipher\locked.png")
Label(image=lock,bg="#3C3F41",pady=5).grid(row=2,column=1,padx=5)
Button(root,text="Encryption", font="Baskerville  16 italic", fg="#E8EAED", bg="#3C3F41", command=encrypt_win).grid(row=3,column=1,padx=15,pady=5)



photoa = PhotoImage(file=r"C:\Users\Dayan Ahmed\Desktop\Cipher\unlocked.png")
Label(image=photoa,bg="#3C3F41",pady=5).grid(row=2,column=3,padx=5)

Button(root,text="Decryption", font="Baskerville  16 italic", fg="#E8EAED", bg="#3C3F41", command=decrypt_win).grid(row=3,column=3,padx=15,pady=5)




root.mainloop()

