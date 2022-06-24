from email import message
from os import system
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk


class Database:
    
    def creat_admin_db(self):
        conn = sqlite3.connect("administrator.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS administrators (
            db_user_name TEXT,
            db_company_name TEXT,
            db_password TEXT,
            db_unique_code TEXT
            )
            """)
        conn.commit()
        conn.close()
        
        
    def admin():
        user_name = user_name_entry.get()
        company_name = company_name_entry.get()
        password = password_entry.get()
        unique_code = unique_code_entry.get()

        conn = sqlite3.connect("administrator.db")
        c = conn.cursor()
        c.execute("SELECT * FROM administrators")
        results = c.fetchall()
       
        if len(results) == 0:
            if user_name_entry != "" and company_name_entry != "" and password_entry != "":
                c.execute("INSERT INTO administrators VALUES (?, ?, ?, ?)", (user_name, company_name, password, unique_code))
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS", "Successfuly Loged In")
                import AdministratPannel
                main.destroy()
                
            
        else:
            fetch = c.execute("SELECT ROWID, db_unique_code FROM administrators")
            result = fetch.fetchone()

            if unique_code == result[1]:
                messagebox.showinfo("SUCCESS", "Successfuly Loged In")
                print(result[1])
                import AdministratPannel
                

            else:
                messagebox.showerror("MISMATCHED", "Please Your Details Are Not In Our RECORDS")
            conn.close()

    
        user_name_entry.delete(0, END)
        company_name_entry.delete(0, END)
        password_entry.delete(0, END)
        unique_code_entry.delete(0, END)


class Login_com:
    def __init__(self, main):
        self.main = main
        # Getting the height and width of current Machine
        self.x = main.winfo_screenwidth()
        self.y = main.winfo_screenheight()
        self.main.geometry(f"{self.x}x{self.y}")
        self.main.title("made by xCoder")
        # Usin( Book for the Login Pages
        self.login_note = ttk.Notebook(self.main)
        self.login_note.pack()

        # TAB for first Login
        self.login_tab = Frame(self.login_note, width=self.x, height=self.y)
        self.login_note.add(self.login_tab)

        # TAB for user to choose who to Continuoe as (Admin or Emloyee)
        self.cont_tab = Frame(self.login_note, width=self.x, height=self.y)
        self.login_note.add(self.cont_tab)

        # Tab for Loging in to the Administrator Panel
        self.admin_log_tab = Frame(self.login_note, width=self.x, height=self.y)
        self.login_note.add(self.admin_log_tab)

    def to_admin():
        user_name = user_name_entry.get()
        company_name = company_name_entry.get()
        password = password_entry.get()

        if user_name=="" or company_name=="" or password=="":
                messagebox.showerror("Error", "Please fill all Entry Fields")
                
        else:
            
            Database.admin()

            
        
        

    # ########################## LOGIN PAGE AFTER CLIENT CHOOSE TO CONTINUOE AS ADMINISTRATOR #########################################
    def admin_login(self):
        self.login_note.hide(1)
        self.login_note.hide(0)
        self.login_note.select(2)
        signin_title = Frame(self.admin_log_tab, width=self.x-20, height=self.y/154)
        signin_title.pack(anchor="center")
        signin_title_lbl = Label(signin_title, text="TO THE ADMINISTRATOR PANNEL", font=("Arial", int((self.x+self.y)//70)))
        signin_title_lbl.pack(anchor="center")
        
        login_frame = Frame(self.admin_log_tab, width=self.x, height=self.y)
        login_frame.pack(anchor="center")
        center_login = Frame(login_frame, width=self.x/2, height=self.y)
        center_login.pack(anchor="center")
        
        global user_name_entry
        user_name = StringVar
        user_name_lb = Label(center_login, text="User Name", font=("Arial", int((self.x+self.y)//130)))
        user_name_lb.place(x=10, y=30)
        user_name_entry = Entry(center_login, width=40, textvariable=user_name)
        user_name_entry.place(x=180, y=30)

        global company_name_entry
        company_name = StringVar
        company_name_lb = Label(center_login, text="Company Name:", font=("Arial", int((self.x+self.y)//130)))
        company_name_lb.place(x=10, y=60)
        company_name_entry = Entry(center_login, width=40, textvariable=company_name)
        company_name_entry.place(x=180, y=60)

        global password_entry
        password = StringVar
        password_lbl = Label(center_login, text="Password:", font=("Arial", int((self.x+self.y)//130)))
        password_lbl.place(x=10, y=90)
        password_entry = Entry(center_login, width=40, show="*", textvariable=password)
        password_entry.place(x=180, y=90)

        global unique_code_entry
        unique_code = StringVar()
        unique_code_lbl = Label(center_login, text="UNIQUE CODE", font=("Arial", int((self.x+self.y)//130)))
        unique_code_lbl.place(x=10, y=130)
        unique_code_entry = Entry(center_login, width=40, show="*", textvariable=password)
        unique_code_entry.place(x=180, y=130)

        login_btn = Button(center_login, text="Login", bg="blue", fg="white", width=10, command=Login_com.to_admin)
        login_btn.place(x=320, y=170)
        
        go_back_btn = Button(center_login, width=20, height=3, bd=4, text="<< Go Back", bg="gray", command= lambda: Login_com.continue_as(self))
        go_back_btn.place(x=10, y=400)

        
        
        # #########################################################################################################################
        
        
    # ################################# WINDOW TO CHOOSE WHO TO LOGIN AS (EITHER AS ADMIN OR EMPLOYEE) ##############################################
    def continue_as(self):
        Database.creat_admin_db(self)
        self.login_note.hide(0)
        self.login_note.hide(2)
        self.login_note.select(1)
        main_title = Frame(self.cont_tab, width=self.x, height=self.x/154)
        main_title.pack(anchor="center")
        main_title_lbl = Label(main_title, text="PRODUCTS MANAGEMENT SYSTEM", font=("ALGERIAN", int((self.x+self.y)//70)), fg="green")
        main_title_lbl.pack(anchor="center")

        choice_frame = Frame(self.cont_tab, width=self.x, height=self.y)
        choice_frame.pack(anchor="center")
        # center_choice = Frame(choice_frame, width=x/2, height=y)
        # center_choice.pack(anchor="center")

        continue_lbl = Label(choice_frame, text="Continue As......................", font=("Arial black", 20), justify="left", padx=15)
        continue_lbl.place(x=self.x/4, y=50)

        cont_addminist_btn = Button(choice_frame, text="An Administrator", font=("Arial", 10), width=50, height=4, bg="light yellow", command= lambda: Login_com.admin_login(self))
        cont_addminist_btn.place(x=self.x/3, y=120)

        cont_emplyee_btn = Button(choice_frame, text="An Emplyee", font=("Arial", 10), width=50, height=4, bg="light yellow")
        cont_emplyee_btn.place(x=self.x/3, y=210)
    # ########################################################################################################################################################

    # ############################# LOGIN PAGE FOR EVERY STARTUP ###################################################################
    def login(self):
        Database.creat_admin_db(self)
        self.login_note.hide(1)
        self.login_note.hide(2)
        self.login_note.select(0)
        signin_title = Frame(self.login_tab, width=self.x-20, height=self.y/154)
        signin_title.pack(anchor="center")
        signin_title_lbl = Label(signin_title, text="LOGIN TO YOUR ACCOUNT", font=("Arial", int((self.x+self.y)//70)))
        signin_title_lbl.pack(anchor="center")
        
        login_frame = Frame(self.login_tab, width=self.x, height=self.y)
        login_frame.pack(anchor="center")
        center_login = Frame(login_frame, width=self.x/2, height=self.y)
        center_login.pack(anchor="center")
        
        global user_name_entry
        user_name = StringVar
        user_name_lb = Label(center_login, text="User Name", font=("Arial", int((self.x+self.y)//130)))
        user_name_lb.place(x=10, y=30)
        user_name_entry = Entry(center_login, width=40, textvariable=user_name)
        user_name_entry.place(x=180, y=30)

        global company_name_entry
        company_name = StringVar
        company_name_lb = Label(center_login, text="Company Name:", font=("Arial", int((self.x+self.y)//130)))
        company_name_lb.place(x=10, y=60)
        company_name_entry = Entry(center_login, width=40, textvariable=company_name)
        company_name_entry.place(x=180, y=60)

        global password_entry
        password = StringVar
        password_lbl = Label(center_login, text="Password:", font=("Arial", int((self.x+self.y)//130)))
        password_lbl.place(x=10, y=90)
        password_entry = Entry(center_login, width=40, show="*", textvariable=password)
        password_entry.place(x=180, y=90)

        login_btn = Button(center_login, text="Login", bg="blue", fg="white", width=10, command=lambda: Login_com.continue_as(self))
        login_btn.place(x=320, y=130)

        main.destroy()
        # ###############################################################################################################
    

if __name__ == '__main__':
    main = Tk()
    app = Login_com(main)
    app.continue_as()
    main.mainloop()