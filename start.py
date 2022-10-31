from tkinter import *
from tkinter import messagebox
import ast
import os.path
from fileinput import filename
#from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import date, datetime
import tkinter as tk
from tkinter import Frame, ttk, messagebox, filedialog
from tkinter import *
from MyQR import myqr
import os
from turtle import Screen
from pyzbar.pyzbar import ZBarSymbol
import xlsxwriter
####################################################################################################

splash_root = Tk()
splash_root.title("Splash Screen!!")
windowWidth = splash_root.winfo_reqwidth()
windowHeight = splash_root.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(splash_root.winfo_screenwidth()/4 - windowWidth/2)
positionDown = int(splash_root.winfo_screenheight()/4 - windowHeight/2)
splash_root.geometry("900x500+{}+{}".format(positionRight, positionDown))
splash_root.overrideredirect(True)
frame = Frame(splash_root, width=900, height=500, bg="white")
frame.place(x=0, y=0)
img = PhotoImage(file='img\splash.png')
Label(splash_root, image=img, bg="white").place(x=0, y=0)
roww = 1

def main_window():
    splash_root.destroy()
    window = Tk()
    window.title("Sign in")
    window.geometry('925x500+200+100')
    # window.iconbitmap('file.ico')
    window.configure(bg='#fff')
    window.resizable(False, False)

    def signinn(e):
        signin()

    def signin():
        username = user.get()
        password = code.get()
        file = open('resources/datasheet.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
        # print(r.keys())
        # print(r.values())

        if username in r.keys() and password == r[username]:
            window.destroy()
            screen = Tk()
            screen.title('Attendance System')
            screen.geometry('1000x500+150+100')

            year = tk.StringVar()
            branch = tk.StringVar()
            batch = tk.StringVar()
            lecture = tk.StringVar()

            title = tk.Label(screen, text="ATTENDANCE SYSTEM", bd=10, relief=tk.GROOVE, font=(
                "Sketch Rockwell", 35), bg="lavender", fg="black")
            title.pack(side=tk.TOP, fill=tk.X)

            frame = Frame(screen, width=600, height=530, bg="white")
            frame.place(x=400, y=78)
            img = PhotoImage(file='img/background.png')
            Label(frame, image=img, bg="white").place(x=0, y=0)

            Manage_Frame = Frame(screen, bg="white")
            Manage_Frame.place(x=0, y=78, width=400, height=530)

            ttk.Label(screen, text="Year", background="white", foreground="black",
                      font=("Times New Roman", 15)).place(x=100, y=150)
            combo_search = ttk.Combobox(screen, textvariable=year, width=10, font=(
                "times new roman", 13), state='readonly')
            combo_search['values'] = ('1', '2', '3', '4')
            combo_search.place(x=250, y=150)

            ttk.Label(screen, text="Branch", background="white", foreground="black",
                      font=("Times New Roman", 15)).place(x=100, y=200)
            combo_search = ttk.Combobox(screen, textvariable=branch, width=10, font=(
                "times new roman", 13), state='readonly')
            combo_search['values'] = ("CSE", "AIML", "CE", "IT", "MECH", "ECM")
            combo_search.place(x=250, y=200)

            ttk.Label(screen, text="Batch", background="white", foreground="black",
                      font=("Times New Roman", 15)).place(x=100, y=250)
            combo_search = ttk.Combobox(screen, textvariable=batch, width=10, font=(
                "times new roman", 13), state='readonly')
            combo_search['values'] = ('A', 'B', 'C', 'D')
            combo_search.place(x=250, y=250)

            ttk.Label(screen, text="Lecture", background="white",
                      foreground="black", font=("Times New Roman", 15)).place(x=100, y=300)
            combo_search = ttk.Combobox(screen, textvariable=lecture, width=10, font=(
                "times new roman", 13), state='readonly')
            combo_search['values'] = ('1', '2', '3', '4', '5', '6', '7')
            combo_search.place(x=250, y=300)

            path = os.getcwd()

            def generate():
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
                    messagebox.showinfo(
                        'QR - Generator', "QR Codes Successfully Generated")
                else:
                    messagebox.showwarning("Warning", "Please select file!!")

            def check():
                if(year.get() and branch.get() and lecture.get() and batch.get()):
                    screen.destroy()
                else:
                    messagebox.showwarning("Warning", "All fields required!!")

            exit_button = tk.Button(screen, width=10, bg="#57a1f8", fg='white', border=0, font=(
                "Times New Roman", 15), text="Submit", command=check)
            exit_button.place(x=50, y=400)

            generate_button = tk.Button(screen, width=10, bg="#57a1f8", fg='white', border=0, font=(
                "Times New Roman", 15), text="Generate QR", command=generate)
            generate_button.place(x=225, y=400)

            button_exit = Button(screen, width=10, bg="#57a1f8", fg='white', border=0, font=(
                "Times New Roman", 15), text="Exit", command=exit)
            button_exit.place(x=400, y=400)

            screen.mainloop()

            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            names = []
            today = date.today()
            d = today.strftime("%b-%d-%Y")

            counter = 0
            filename = (d)

            if (os.path.exists("attendance/"+filename+".xlsx") == False):
                filename = (filename)
            else:
                while (os.path.exists("attendance/"+filename+"("+str(counter+1)+")"+".xlsx") == True):
                    counter += 1
                filename = (filename+"("+str(counter+1)+")")

            # print("\nThe file name is : "+filename)
            p = "attendance/test.txt"
            os.makedirs(os.path.dirname(p), exist_ok=True)
            f = xlsxwriter.Workbook("attendance/"+filename+'.xlsx')
            fob = f.add_worksheet()
            fob.write('A1', 'Name')
            fob.write('B1', 'Class & batch')
            fob.write('C1', 'Year')
            fob.write('D1', 'Lecture')
            fob.write('E1', 'In Time')

            def enterData(z):
                global roww
                if z in names:
                    pass
                else:
                    it = datetime.now()
                    names.append(z)
                    z = (z.decode('utf-8'))
                    intime = it.strftime("%I:%M %p")
                    my_list = [z, branch.get()+'-'+batch.get(), year.get(),lecture.get(), intime]
                    for col_num, data in enumerate(my_list):
                        fob.write(roww, col_num, data)
                    # print(roww)
                    # print(my_list)
                    roww += 1
                return names

            print('Reading...')

            def checkData(data):
                # data=str(data)
                if data in names:
                    print('Already Present')
                else:
                    print('\n'+str(len(names)+1)+' '+'present...')
                    enterData(data)
            ##################################

            # decode(Image.open('pyzbar/tests/qrcode.png'), symbols=[ZBarSymbol.QRCODE])
##################################################
            while True:
                _, frame = cap.read()
                # decodedObjects = pyzbar.decode(frame)
                decodedObjects = pyzbar.decode(
                    frame, symbols=[ZBarSymbol.QRCODE])
                for obj in decodedObjects:
                    checkData(obj.data)
                    time.sleep(1)

                cv2.imshow("Scanner", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print(
                        'Attendance is generated successfully in file named '+filename)
                    cv2.destroyAllWindows()
                    break

            f.close()

        else:
            messagebox.showerror('Invalid', 'invalid username and password')

    def sign():
        screen.destroy()

    ########################################################################################################################
    ########################################################################################################################

    def signup_command():
        window = Toplevel()
        window.title("Sign Up")
        window.geometry('925x500+200+100')
        window.configure(bg='#fff')
        window.resizable(False, False)

        def signupenter(e):
            signup()

        def signup():
            username = user.get()
            password = code.get()
            conform_password = conform_code.get()

            if password == conform_password:
                try:
                    file = open('resources/datasheet.txt', 'r+')
                    d = file.read()
                    r = ast.literal_eval(d)

                    dict2 = {username: password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file = open('resources/datasheet.txt', 'w')
                    w = file.write(str(r))
                    messagebox.showinfo('Signup', 'Successfully sign up')
                except:
                    file = open('resources/datasheet.txt', 'w')
                    pp = str({'Username': 'password'})
                    file.write(pp)
                    file.close()
            else:
                messagebox.showerror('Invalid', 'Both Password should match')

        def sign():
            window.destroy()

        img = PhotoImage(file='img/signup.png')
        Label(window, image=img, bg="white").place(x=0, y=80)

        frame = Frame(window, width=350, height=390, bg="white")
        frame.place(x=480, y=50)

        heading = Label(frame, text="Sign up", fg='#57a1f8', bg="white",
                        font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        ###################################################

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            # name = user.get()
            if user.get() == '':
                user.insert(0, 'Username')

        user = Entry(frame, width=25, fg="black", border=0,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Username')
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        #############################

        def on_enter(e):
            code.delete(0, 'end')

        def on_leave(e):
            #name = user.get()
            if code.get() == '':
                code.insert(0, 'Password')

        code = Entry(frame, width=25, fg="black", border=0,
                     bg='white', font=('Microsoft YaHei UI Light', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Password')
        code.bind('<FocusIn>', on_enter)
        code.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        ###############################################

        def on_enter(e):
            conform_code.delete(0, 'end')

        def on_leave(e):
            #name = user.get()
            if conform_code.get() == '':
                conform_code.insert(0, 'Conform Password')

        conform_code = Entry(frame, width=25, fg="black", border=0,
                             bg='white', font=('Microsoft YaHei UI Light', 11))
        conform_code.place(x=30, y=220)
        conform_code.insert(0, 'Conform Password')
        conform_code.bind('<FocusIn>', on_enter)
        conform_code.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        #####################
        Button(frame, width=39, pady=7, text='Sign up', bg="#57a1f8",
               fg='white', border=0, command=signup).place(x=35, y=300)
        window.bind('<Return>', signupenter)
        label = Label(frame, text="I have an account?", fg='black',
                      bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=90, y=340)

        signin = Button(frame, width=6, text='Sign in', border=0,
                        bg='white', cursor='hand2', fg='#57a1f8', command=sign)
        signin.place(x=200, y=340)

        window.mainloop()

    ########################################################################################################################
    ########################################################################################################################
    img = PhotoImage(file='img/signin.png')
    label = Label(window, image=img, bg="white")
    label.image = img  # keep a reference!
    label.place(x=0, y=85)

    frame = Frame(window, width=350, height=390, bg="white")
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign in", fg='#57a1f8', bg="white",
                    font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)
    ########################################################################################################################

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        # name = user.get()
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg="black", border=0,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ########################################################################################################################

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        #name = user.get()
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg="black", border=0,
                 bg='white', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ########################################################################################################################

    Button(frame, width=39, pady=7, text='Sign in', bg="#57a1f8",
           fg='white', border=0, command=signin).place(x=35, y=204)

    window.bind('<Return>', signinn)

    label = Label(frame, text="Don't have an account?", fg='black',
                  bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75, y=270)

    sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white',
                     cursor='hand2', fg='#57a1f8', command=signup_command)
    sign_up.place(x=215, y=270)


splash_root.after(3000, main_window)

####################################################################################################

mainloop()

################################################END##############################################################
