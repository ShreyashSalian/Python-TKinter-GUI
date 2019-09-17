from tkinter import *
import tkinter
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

class Employee():

    def __init__(self):
        self.root = Tk()
        #self.root.configure(background='lime')
        self.root.geometry("500x500")


        self.root.title("Student Details")
        Label(self.root, text="Student Details", bg="lime", font=("Times", 18), width=80, height=1).pack()
        label_student_name = Label(self.root, text="Student Name", anchor=tkinter.E,width=70,height=2)
        self.entry_student_name = Entry(self.root)
        label_subject_1 = Label(self.root, text="Subject 1", anchor=tkinter.E)
        self.entry_subject_1 = Entry(self.root)
        label_subject_2 = Label(self.root, text="Subject 2", anchor=tkinter.E)
        self.entry_subject_2 = Entry(self.root)
        label_subject_3 = Label(self.root, text="Subject 3", anchor=tkinter.E)
        self.entry_subject_3 = Entry(self.root)
        label_subject_4 = Label(self.root, text="Subject 4", anchor=tkinter.E)
        self.entry_subject_4 = Entry(self.root)
        label_subject_5 = Label(self.root, text="Subject 5", anchor=tkinter.E)
        self.entry_subject_5 = Entry(self.root)
        label_gender = Label(self.root, text="Gender", anchor=tkinter.E)
        self.entry_gender = Entry(self.root)
        label_email = Label(self.root, text="Email", anchor=tkinter.E)
        self.entry_email = Entry(self.root)


        label_total = Label(self.root, text="Total", anchor=tkinter.E)
        self.entry_total = Entry(self.root)
        label_percentage = Label(self.root, text="Percentage", anchor=tkinter.E)
        self.entry_percentage = Entry(self.root)
        self.res = Label(self.root, anchor=tkinter.E)

        self.b_new = Button(self.root,text="New",command=self.new_record)
        self.b_save = Button(self.root, text="Save",command=self.save_record)
        self.b_delete = Button(self.root, text="Delete",command=self.delete_record)
        self.b_exit = Button(self.root, text="Exit",command=self.exit_records)
        self.b_first = Button(self.root, text="First",command=self.first_record)
        self.b_next = Button(self.root, text="Next",command=self.next_record)
        self.b_previous = Button(self.root, text="Previous",command=self.previous_record)
        self.b_last = Button(self.root, text="last",command=self.last_record)
        label_student_name.place(x=140, y=50, width=90, height=25)
        self.entry_student_name.place(x=240, y=50, width=100, height=25)

        label_subject_1.place(x=140, y=80, width=90, height=25)
        self.entry_subject_1.place(x=240, y=80, width=100, height=25)

        label_subject_2.place(x=140, y=110, width=90, height=25)
        self.entry_subject_2.place(x=240, y=110, width=100, height=25)

        label_subject_3.place(x=140, y=140, width=90, height=25)
        self.entry_subject_3.place(x=240, y=140, width=100, height=25)

        label_subject_4.place(x=140, y=170, width=90, height=25)
        self.entry_subject_4.place(x=240, y=170, width=100, height=25)
        label_subject_5.place(x=140, y=200, width=90, height=25)
        self.entry_subject_5.place(x=240, y=200, width=100, height=25)
        label_gender.place(x=140, y=230, width=90, height=25)
        self.entry_gender.place(x=240, y=230, width=100, height=25)
        label_email.place(x=140, y=260, width=90, height=25)
        self.entry_email.place(x=240, y=260, width=100, height=25)


        label_total.place(x=140, y=290, width=90, height=25)
        self.entry_total.place(x=240, y=290, width=100, height=25)

        label_percentage.place(x=140, y=320, width=90, height=25)
        self.entry_percentage.place(x=240, y=320, width=100, height=25)

        self.b_new.place(x=140, y=350, width=40, height=25)
        self.b_save.place(x=190, y=350, width=40, height=25)

        self.b_delete.place(x=240, y=350, width=40, height=25)
        self.b_exit.place(x=290, y=350, width=40, height=25)

        self.b_first.place(x=140, y=390, width=40, height=25)
        self.b_next.place(x=190, y=390, width=40, height=25)
        self.b_previous.place(x=240, y=390, width=50, height=25)
        self.b_last.place(x=300, y=390, width=40, height=25)
        self.res.place(x=220,y=420)


        c ={
            "user":"root",
            "password":"",
            "database":"shreyashdb",
            "host":"localhost",
            "raise_on_warnings":True
        }
        self.db = mysql.connector.connect(**c)
        try:
            self.cursor = self.db.cursor()
            self.cursor.execute("SELECT * FROM STUDENT")
            self.results = self.cursor.fetchall()
            self.current_record = 0
        except Exception as e:
            messagebox.showerror("Message","Error fetching Data")
        self.first_record()
        self.root.mainloop()


    def result(self):
        if percentage >= 80:
           # print("hello")
            result = "You have got First Class"
            print(result)
        elif percentage < 80 and percentage >= 70:
            result = "You have got first class"
            print(result)

        elif percentage < 70 and percentage >= 60:
            result = "You have got Second class"
            print(result)
        else:
            result = " Sorry you are fail"
            print(result)

        #self.res.config(text=result)


    def first_record(self):
        if len(self.results) > 0:
            self.current_record = 0
            self.populate_record()

    def populate_record(self):
        r = self.results[self.current_record]
        self.entry_student_name.delete(0,END)
        self.entry_student_name.insert(0,r[0])
        self.entry_subject_1.delete(0, END)
        self.entry_subject_1.insert(0, r[1])
        self.entry_subject_2.delete(0, END)
        self.entry_subject_2.insert(0, r[2])
        self.entry_subject_3.delete(0, END)
        self.entry_subject_3.insert(0, r[3])
        self.entry_subject_4.delete(0, END)
        self.entry_subject_4.insert(0, r[4])
        self.entry_subject_5.delete(0, END)
        self.entry_subject_5.insert(0, r[5])
        self.entry_gender.delete(0, END)
        self.entry_gender.insert(0, r[6])
        self.entry_email.delete(0, END)
        self.entry_email.insert(0, r[7])
        self.entry_total.delete(0, END)
        self.entry_total.insert(0, r[8])
        self.entry_percentage.delete(0, END)
        self.entry_percentage.insert(0, r[9])

    def populate_blank(self):
        self.entry_student_name.delete(0,END)
        self.entry_subject_1.delete(0, END)
        self.entry_subject_2.delete(0, END)
        self.entry_subject_3.delete(0, END)
        self.entry_subject_4.delete(0, END)
        self.entry_subject_5.delete(0, END)
        self.entry_gender.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_total.delete(0, END)
        self.entry_percentage.delete(0,END)


    def new_record(self):
        self.b_new['state'] = DISABLED
        self.populate_blank()

    def save_record(self):
        student_name = self.entry_student_name.get()
        subject1 = float(self.entry_subject_1.get())
        subject2 = float(self.entry_subject_2.get())
        subject3 = float(self.entry_subject_3.get())
        subject4 = float(self.entry_subject_4.get())
        subject5 = float(self.entry_subject_5.get())
        gender = self.entry_gender.get()
        email = self.entry_email.get()
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = float(total)*100/500
        #print(self.percentage)
        #print(percentage)
        if self.b_new['state'] == DISABLED:
            sql = "INSERT INTO STUDENT(STUDENT_NAME,SUBJECT_1,SUBJECT_2,SUBJECT_3,SUBJECT_4,SUBJECT_5,GENDER,EMAIL,TOTAL,PERCENTAGE) VALUES('%s','%f','%f','%f','%f','%f','%s','%s','%f','%f')"%(student_name,subject1,subject2,subject3,subject4,subject5,gender,email,total,percentage)
            print("Hello")


        else:
            sql = "UPDATE STUDENT set SUBJECT_1='%f',SUBJECT_2='%f',SUBJECT_3='%f',SUBJECT_4='%f',SUBJECT_5='%f',GENDER='%s','EMAIL='%s',TOTAL='%f',PERCENTAGE='%f' WHERE STUDENT_NAME='%s'"%(subject1,subject2,subject3,subject4,subject5,gender,email,total,percentage,student_name)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            sql = "SELECT * FROM STUDENT"
            self.cursor.execute(sql)
            self.results = self.cursor.fetchall()
            messagebox.showinfo("INSERT||UPDATE","Records is either inserted or updated successfully")
        except Exception as e:
            self.db.rollback()
            s1 = "Error while Inserting Records",str(e)
        if percentage >= 80:
           # print("hello")
            result = "You have got First Class"
            print(result)
        elif percentage < 80 and percentage >= 70:
            result = "You have got first class"
            print(result)

        elif percentage < 70 and percentage >= 50:
            result = "You have got Second class"
            print(result)
        else:
            result = " Sorry you are fail"
            print(result)

        self.res.config(text = result)
        self.b_new['state']=NORMAL
    def delete_record(self):
        student_name = self.entry_student_name.get()
        sql = "DELETE FROM STUDENT WHERE STUDENT_NAME = '%s'"%(student_name)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            sql = "SELECT * FROM STUDENT"
            self.cursor.execute(sql)
            self.results = self.cursor.fetchall()
            self.populate_blank()
            self.populate_record()
            messagebox.showinfo("DELETE","Records deleted successfully")

        except Exception as e:
            s = "Error while deleting records",str(e)
            messagebox.showerror("delete",s)

    def exit_records(self):
        self.root.destroy()

    def next_record(self):
        if len(self.results) > 0:
            self.current_record += 1
            if self.current_record >= len(self.results):

                self.current_record = 0
            self.populate_record()

    def previous_record(self):
        if len(self.results) > 0:
            self.current_record-= 1
            if self.current_record < 0:
                self.current_record = len(self.results) - 1
            self.populate_record()

    def last_record(self):
        if len(self.results) > 0:
            self.current_record = len(self.results) - 1
        self.populate_record()

a = Employee()