from tkinter import *
import sys
import MySQLdb
# host,user,password,databaseName
conn = MySQLdb.connect("localhost","root","","Tkinter")
if(conn):
    print("Connection Successful")
else:
    print("Connection Failed")
# connection set.......
cur = conn.cursor()
def SaveData():
    f = a.get()
    g = b.get()
    e = c.get()
    cur.execute("""INSERT INTO students(fname,lname,course) VALUES("%s","%s","%s")"""%(f,g,e))
    print(f"Number of rows inserted: {cur.rowcount}")

    if cur != 0:
        conn.commit()
    else:
        conn.rollback()
        conn.close()

root =Tk()
Label(root,text="First Name:").pack()
a = Entry(root,width=15)
a.pack()

Label(root,text="Last Name:").pack()
b = Entry(root,width=15)
b.pack()

Label(root,text="Course:").pack()
c = Entry(root,width=15)
c.pack()

Button(root,text="Save", command=SaveData).pack()
root.mainloop()
