from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class Showdata:

    conn = mysql.connector.connect(host="localhost", user="root", password="4747", database="sarvesh")
    my_cursor = conn.cursor()

    sql="select * from register"
    my_cursor.execute(sql)
    rows=my_cursor.fetchall()

    win=Tk()

    frm=Frame(win)
    frm.pack(side=tk.LEFT,padx=20)

    tv=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings",height="5")
    tv.pack()

    tv.heading(1, text="fname")
    tv.heading(2, text="lname")
    tv.heading(3, text="contact")
    tv.heading(4, text="email")
    tv.heading(5, text="password")


    for i in rows:
        tv.insert('','end',values=i)

    win.title("Showdata")
    win.geometry("1600x900+0+0")
    win.mainloop()






