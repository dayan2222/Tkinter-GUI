from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

def info():
    tmsg.showinfo("Info", "This is info message")

def ask_question():
    value = tmsg.askquestion("Rate This App", "Do you Like this app?")
    if value == "yes":
        value = "Rate us on App Store"
    else:
        value = "We will contact you soon!"
    tmsg.showinfo("Your Rating", value)

def retry():
    value = tmsg.askretrycancel("Fail", "Application Fail")
    if value == True:
        value = "Retrying"
    else:
        value = "Close Application"
    tmsg.showinfo("Status", value)

def warning():
    tmsg.showwarning("Stop Working", "Application is stopped!")

def quit():
    value = tmsg.askyesno("Exit","Do You Want to exit this app?")
    if value == True:
        value = "Save all the programs"
    else:
        value = "Application is working"
    tmsg.showinfo("Status", value)
main_menu = Menu(root)

sub_menu = Menu(main_menu, tearoff=0)
sub_menu.add_command(label="Info", command=info)
sub_menu.add_command(label="Ask Question", command=ask_question)
sub_menu.add_command(label="Retry", command=retry)
sub_menu.add_command(label="Warning", command=warning)
sub_menu.add_command(label="Yes No", command=quit)
root.config(menu=main_menu)
main_menu.add_cascade(label="Message Box", menu=sub_menu)


root.mainloop()