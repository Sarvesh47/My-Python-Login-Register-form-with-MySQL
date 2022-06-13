from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class Output_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        self.root=tk.Tk()





        conn = mysql.connector.connect(host="localhost", user="root", password="4747", database="sarvesh")
        my_cursor = conn.cursor()

        sql="select * from register"
        my_cursor.execute(sql)
        rows=my_cursor.fetchall()

        frame = Frame(self.root, bg="skyblue")
        frame.place(x=520, y=100, width=800, height=550)

        columns=('fname','lname','contact','email','password')
        tv=ttk.Treeview(root,columns,show='headings')
        tv.pack()

        tv.heading(1, text="fname")
        tv.heading(2, text="lname")
        tv.heading(3, text="contact")
        tv.heading(4, text="email")
        tv.heading(5, text="password")


        for i in rows:
            tv.insert('','end',values=i)



if __name__ == "__main__":
    root=Tk()
    app=Output_Window(root)
    root.mainloop()
