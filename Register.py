from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Register_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")


        #----------------variables----------------
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_pswd = StringVar()
        self.var_conf_pswd = StringVar()






        frame = Frame(self.root, bg="skyblue")
        frame.place(x=520, y=100, width=800, height=550)

        #register label
        register_lbl=Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="blue",bg="pink")
        register_lbl.place(x=20,y=20)


        #==========Label and entry========

        #-------------row1

        fname = label = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="white", bg="black")
        fname.place(x=50, y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname = label = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lname.place(x=370, y=100)

        frame_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        frame_entry.place(x=370, y=130, width=250)

        #-----------row2

        contact = lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), fg="white", bg="black")
        contact.place(x=50, y=200)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact,font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=230, width=250)

        email = lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        email.place(x=370, y=200)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=370, y=230, width=250)



        #---------------row3

        pswd = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pswd, font=("times new roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        conf_pswd = lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        conf_pswd.place(x=370, y=315)

        self.txt_conf_pswd = ttk.Entry(frame,textvariable=self.var_conf_pswd, font=("times new roman", 15, "bold"))
        self.txt_conf_pswd.place(x=370, y=340, width=250)




        #==========register button






        regi_btn = Button(frame,command=self.register_data, text="Register", font=("times new roman", 15, "bold"), borderwidth=0, fg="white",
                         bg="black", activebackground="black")
        regi_btn.place(x=10, y=420, width=300)

        #===========loginbutton

        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3,
                           relief=RIDGE, fg="white", bg="red")
        login_btn.place(x=330, y=420, width=300)





        #================Function===============
    def register_data(self):
        if self.var_lname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pswd.get()!= self.var_conf_pswd.get():
            messagebox.showerror("Error","password and confirm password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="4747",database="sarvesh")
            my_cursor=conn.cursor()
            query=("select * from register where contact=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another contact no")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",(self.var_fname.get(),
                                  self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_pswd.get()))


            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register successfully")

















if __name__ == "__main__":
    root=Tk()
    app=Register_Window(root)
    root.mainloop()