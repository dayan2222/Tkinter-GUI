from tkinter import *

root = Tk()
root.geometry('500x500')
root.title("NewsPaper")

photo = PhotoImage(file='baby.png')
# label=Label(text="show it ...........",font=('arial',19))
label = Label(image=photo)
label.pack(side='right')

explain='''
Pakistan, officially the Islamic Republic of Pakistan, is a country in South Asia.\n It is the world’s sixth-most populous country with a population exceeding 212,742,631 people. \n In area, it is the 33rd-largest country, spanning 881,913 square kilometres. '''
label1 = Label(text=explain,padx=20, pady=40, font=('arial', 10))
label2 = Label(text='''
Daily NewsPaper
    ''', font=("Helvetica", 20, 'bold'), fg='white', bg='green')
label2.pack(fill=X)
label1.pack(side='top', anchor='nw')
root.mainloop()