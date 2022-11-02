from cProfile import label
from cgitb import text
from itertools import tee
import sqlite3 as sq  # For tables and database
from tkinter import *  # GUI package
from tkinter import Frame, ttk, messagebox, filedialog
import datetime
import time
from datetime import date, datetime
import os
import os.path
from turtle import bgcolor
from MyQR import myqr
from pyzbar.pyzbar import ZBarSymbol
import cv2
import pyzbar.pyzbar as pyzbar
from tkcalendar import DateEntry

#################################################################################################################
#
window = Tk()
window.title("Attendance")
window.geometry('700x500+0+0')
# header = Label(window, text="Attendance System", font=("arial", 30, "bold"), fg="steelblue").pack()
window.config(bg="white")
#
con = sq.connect('database.db')  # dB browser for sqlite needed
c = con.cursor()  # SQLite command, to connect to db so 'execute' method can be called
#
#################################################################################################################
#
year = StringVar()
branch = StringVar()
batch = StringVar()
lecture = StringVar()
subject = StringVar()
title = Label(window, text="ATTENDANCE SYSTEM", bd=10, relief=GROOVE, font=("Sketch Rockwell", 35), bg="lavender", fg="black")
title.pack(side=TOP, fill=X)
#
ttk.Label(window, text="Year", background="white", foreground="black",font=("Times New Roman", 15)).place(x=100, y=150)
combo_search = ttk.Combobox(window, textvariable=year, width=10, font=("times new roman", 13), state='readonly')
combo_search['values'] = ('1', '2', '3', '4')
combo_search.place(x=250, y=150)
#
ttk.Label(window, text="Branch", background="white", foreground="black",font=("Times New Roman", 15)).place(x=100, y=200)
combo_search = ttk.Combobox(window, textvariable=branch, width=10, font=("times new roman", 13), state='readonly')
combo_search['values'] = ("CSE", "AIML", "CE", "IT", "MECH", "ECM")
combo_search.place(x=250, y=200)
#
ttk.Label(window, text="Batch", background="white", foreground="black",font=("Times New Roman", 15)).place(x=100, y=250)
combo_search = ttk.Combobox(window, textvariable=batch, width=10, font=("times new roman", 13), state='readonly')
combo_search['values'] = ('A', 'B', 'C', 'D')
combo_search.place(x=250, y=250)
#
ttk.Label(window, text="Lecture", background="white",foreground="black", font=("Times New Roman", 15)).place(x=100, y=300)
combo_search = ttk.Combobox(window, textvariable=lecture, width=10, font=("times new roman", 13), state='readonly')
combo_search['values'] = ('1', '2', '3', '4', '5', '6', '7')
combo_search.place(x=250, y=300)
#
ttk.Label(window, text="Subject", background="white",foreground="black", font=("Times New Roman", 15)).place(x=100, y=330)
# subjectT = Entry(window, textvariable=subject, background="white", font=("Times New Roman", 12))
# subjectT.place(x=250, y=330)
#
# print('list table start')
sql_query = ('''SELECT name FROM sqlite_master WHERE type='table';''')
c.execute(sql_query)
tableslist =[]
for row in c.fetchall():
    for itm in row:
        # tableslist = add(itm)
        tableslist.append(itm)
    # print(c.fetchall())
clicked = StringVar()
#
def selsub(e):
    subject.set(myCombo.get())
#
myCombo = ttk.Combobox(window, values=tableslist,textvariable=subject, background="white", font=("Times New Roman", 12))
myCombo.bind("<<Comboboxselected>>",selsub)
myCombo.place(x=250, y=330)
#
# Add Calendar
cal = DateEntry(window,selectmode='day',date_pattern='dd/mm/y')
cal.place(x=250, y=360)
#
#############################Tree#View###############################################################################
treev = ttk.Treeview(window, selectmode ='browse')
treev.pack(side='right' ,padx=20,pady=80,anchor=NE)
#
# Constructing vertical scrollbar with treeview
verscrlbar = ttk.Scrollbar(window,orient ="vertical",command = treev.yview)
verscrlbar.pack(side ='right', fill ='x')
#
# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)
#
# Defining number of columns
treev["columns"] = ("1", "2")
#
# Defining heading
treev['show'] = 'headings'
#
# Assigning the width and anchor to  the
# respective columns
treev.column("1", width = 80, anchor ='c')
treev.column("2", width = 100, anchor ='c')
#
# Assigning the heading names to the
# respective columns
treev.heading("1", text ="Roll No")
treev.heading("2", text ="In Time")
# treev.heading("3", text ="Age")
#
#get func to isolate the text entered in the entry boxes and submit to database
def submitData():
    if(year.get() and branch.get() and lecture.get() and batch.get() and subject.get() and batch.get() and cal.get_date()):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        names = []
        today = date.today()
        d = today.strftime("%b-%d-%Y")
        filename = (d)
        def enterData(z):
            if z in names:
                pass
            else:
                it = datetime.now()
                names.append(z)
                #z=''.join(str(z))
                z = (z.decode('utf-8'))
                intime = it.strftime("%I:%M %p")
                # datep = it.strftime("%Y-%m-%d")
                datep = cal.get_date().strftime("%Y-%m-%d")
                # print("You have submitted a record")
                # print(subject.get())
                c.execute('CREATE TABLE IF NOT EXISTS ' + subject.get() +' (roll_no TEXT, in_time TEXT, branch TEXT, batch TEXT, year INTEGER, lecture INTEGER, subject TEXT, date NUMERIC)')  # SQL syntax
                # print("Table "+subject.get()+" Created")
                c.execute('INSERT INTO ' + subject.get() + ' (roll_no , in_time , branch , batch , year , lecture , subject , date ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(z, intime, branch.get(), batch.get(), year.get(), lecture.get(), subject.get(), datep))  # Insert record into database.
                con.commit()
                print("You have Inserted a record")
                # fob.write(z+'\t'+branch.get()+'-'+batch.get() +
                #         '\t'+year.get()+'\t'+lecture.get()+'\t'+intime+'\n')
            return names
            #####################################################################
        print('Reading...')
        def checkData(data):
            # data=str(data)
            if data in names:
                print('Already Present')
            else:
                rl = (data.decode('utf-8'))
                # print('\n'+str(len(names)+1)+' '+'present...')
                print('\nRoll no '+(rl)+' Present...')
                enterData(data)
        #########################################################################
        while True:
            _, frame = cap.read()
            # decodedObjects = pyzbar.decode(frame)
            decodedObjects = pyzbar.decode(frame,symbols=[ZBarSymbol.QRCODE])
            for obj in decodedObjects:
                checkData(obj.data)
                time.sleep(1)
            cv2.imshow("Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('Attendance is generated successfully in file named '+filename)
                cv2.destroyAllWindows()
                break
    else:
        messagebox.showwarning("Warning", "All fields required!!")
######  This block is use to generate qr codes 
def generateQR():
    path = os.getcwd()
    filename = filedialog.askopenfilename(initialdir=path+"\resources", title="Select a File", filetypes=(
        ("Text files",  "*.txt*"), ("all files", "*.*")))
    # print(filename)
    if(filename != ""):
        f = open(filename, 'r')
        lines = f.read().split("\n")
        # print(filename)
        print(lines)
        #path=os.getcwd()
        
        p = "qr/test.txt"
        os.makedirs(os.path.dirname(p), exist_ok=True)
        new = path+"\qr"
    
        for _ in range(0, len(lines)):
            data = lines[_]
            qr = myqr.run(
                str(data),
                # level='H',
                # version=10,
                # picture="img/logo.png",
                # colorized=True,
                save_name=str(lines[_]+'.png'),
                save_dir=new)
        messagebox.showinfo('QR - Generator', "QR Codes Successfully Generated")
    else:
        messagebox.showwarning("Warning", "Please select file!!")
######  This block is use to fetch data from database 
def record():
    if(subject.get() and cal.get_date()):
        print()
        dt = cal.get_date().strftime("%Y-%m-%d")
        dd = str(dt)
        # c.execute('''SELECT * FROM ''' + subject.get())
        # c.execute('''SELECT * FROM '''+ subject.get()+''' WHERE date = '''+dt)
        c.execute("""SELECT * FROM """+subject.get()+""" WHERE date = '"""+ dd +"""' """)
        #
        data = c.fetchall()  # Gets the data from the table
        for i in treev.get_children():
            treev.delete(i)
        for row in data:
            # print(row)
            # Lb.insert(1, row)
            treev.insert("", 'end', text ="L1",values =(row[0], row[1]))  # Inserts record row by row in Tree View
            year.set(row[4])
            branch.set(row[2])
            batch.set(row[3])
            lecture.set(row[5])
            subject.set(row[6])
        L6 = Label(window, bg="white", text='Date: '+row[7] + ' ',font=("arial", 12)).place(x=500, y=80)
        L7 = Label(window, bg="white", text='Subject: '+subject.get() + '     ',font=("arial", 12)).place(x=500, y=100)
        con.commit()
    else:
        messagebox.showwarning("Warning", "Please select subject and date!!")
# def get():
#     # print("You have submitted a record")
#     pass
# def testquery():
#     # print('list table start')
#     sql_query = ('''SELECT name FROM sqlite_master WHERE type='table';''')
#     c.execute(sql_query)
#     tableslist =[]
#     for row in c.fetchall():
#         for itm in row:
#             # tableslist = add(itm)
#             tableslist.append(itm)
#         # print(c.fetchall())
#     # print(tableslist)
#     # print('list table end')
##################################################
submit_button = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=("Times New Roman", 15), text="Submit", command=submitData)
submit_button.place(x=50, y=400)

generate_button = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=("Times New Roman", 15), text="Generate QR" ,command=generateQR)
generate_button.place(x=225, y=400)

exit_button = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=("Times New Roman", 15), text="Exit", command=exit)
exit_button.place(x=400, y=400)
##########################################
# insert_button = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=("Times New Roman", 15), text="Insert", command=get )
# insert_button.place(x=50, y=450)

# testquery_button = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=("Times New Roman", 15), text="Q Fire" , command=testquery)
# testquery_button.place(x=225, y=450)

opendb_exit = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=("Times New Roman", 15), text="Open DB", command=record)
opendb_exit.place(x=400, y=450)
############################################
window.mainloop()  # mainloop() -> make sure that window stays open