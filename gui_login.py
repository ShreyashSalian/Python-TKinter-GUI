from tkinter import *
import mysql.connector
from tkinter import messagebox

def register():
    screen2 = Toplevel(screen1)
    screen2.title("Registration Form")
    screen2.geometry("500x500")
    global username
    global password
    global email
    global country
    global username_entry
    global password_entry
    global email_entry
    global country_entry
    country = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()
    Label(screen2,text="Registration", bg="lime", font=("Times", 18), width=200, height=2).pack()
    username_label = Label(screen2,text="Username").pack()
    username_entry = Entry(screen2,textvariable = username)
    username_entry.pack()
    Label(screen2,text="").pack()
    password_label = Label(screen2, text="password").pack()
    password_entry = Entry(screen2,textvariable = password)
    password_entry.pack()
    Label(screen2, text="").pack()
    email_label = Label(screen2, text="Email").pack()
    email_entry = Entry(screen2, textvariable = email)
    email_entry.pack()
    Label(screen2, text="").pack()
    country_label = Label(screen2, text="Country").pack()
    country_entry = Entry(screen2, textvariable = country)
    country_entry.pack()

    Label(screen2,text="").pack()
    register_button = Button(screen2,text = "submit",bg="green",command=register_user).pack()
    screen2.mainloop()

def register_user():


    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    country_info = country.get()

    sql = "INSERT INTO REGISTRATION(USERNAME,PASSWORD,EMAIL,COUNTRY) VALUES('%s','%s','%s','%s')"%(username_info,password_info,email_info,country_info)
    try:
        c = {
            "user": "root",
            "password": "",
            "database": "shreyashdb",
            "host": "localhost",
            "raise_on_warnings": True
        }
        db = mysql.connector.connect(**c)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo("Insert","You have been registered successfully")

    except Exception as e:
        s1 = "There is sime issue in inserting records",str(e)
        messagebox.showerror("Error",s1)
        db.rollback()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    country_entry.delete(0, END)




def login():
    global screen3
    screen3 = Toplevel(screen1)
    screen3.title("Login")
    screen3.geometry('500x500')
    global username_database
    global password_database
    global username_entry_database
    global password_entry_database
    username_database = StringVar()
    password_database = StringVar()

    Label(screen3, text="Login Form", bg="lime", font=("Times", 18), width=200, height=2).pack()
    username_label = Label(screen3, text="Username").pack()
    username_entry_database = Entry(screen3, textvariable=username_database)
    username_entry_database.pack()
    Label(screen3, text="").pack()
    password_label = Label(screen3, text="password").pack()
    password_entry_database = Entry(screen3, textvariable=password_database)
    password_entry_database.pack()
    Label(screen3, text="").pack()
    submit = Button(screen3,text = "Submit",command=login_check).pack()
    screen3.mainloop()

def database():
    global c
    global cursor
    global db
    c = {
        "user": "root",
        "password": "",
        "database": "shreyashdb",
        "host": "localhost",
        "raise_on_warnings": True
    }

def login_check():
    username_info = username_database.get()
    password_info = password_database.get()

    c = {
        "user": "root",
        "password": "",
        "database": "shreyashdb",
        "host": "localhost",
        "raise_on_warnings": True
    }
    db = mysql.connector.connect(**c)
    cursor = db.cursor()
    sql = "SELECT * FROM REGISTRATION WHERE USERNAME = '%s' AND PASSWORD = '%s'"%(username_info,password_info)
    try:
        cursor.execute(sql)

        res = cursor.fetchall()
        print("Result is %d"%len(res))
        if len(res) > 0:
            '''for r in res:
                print("%s\t%s\t%s\t%s "% (r[1], r[2], r[3], r[4]))
                messagebox.showinfo("Success", "You have login successfully")
            
            '''
            login_success()

        else:
            messagebox.showinfo("Incorrect","Sorry you have entered Incorrect username and password")
            username_entry_database.delete(0,END)
            password_entry_database.delete(0,END)
    except Exception as e:
        s1 = "Error while fetching data"
        messagebox.showerror("Error",s1)
    db.close()

def login_success():
    #screen4 = Toplevel()
    #screen4.title("Home")
    #screen4.geometry("500x500")
    import student_gui







def main_screen():
    global screen1
    screen1 = Tk()
    screen1.title("NoteBook")
    screen1.geometry("500x500")
    Label(text = "Notebook",bg="lime",font=("Times",18),width=200,height=2).pack()
    Label(text="").pack()
    b1 = Button(screen1,text = "Login",width=30,height=2,command=login).pack()
    Label(text="").pack()

    b2 = Button(screen1,text = "Register",width=30,height=2,command=register).pack()
    screen1.mainloop()

m = main_screen()
