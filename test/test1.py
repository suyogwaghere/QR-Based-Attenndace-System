from turtle import window_width
import pandas as pd
from tkinter import filedialog
import os.path
from fileinput import filename
from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import date, datetime
import tkinter as tk
from tkinter import Frame, ttk, messagebox, filedialog
from tkinter import *
import xlsxwriter
from MyQR import myqr
import os
from pyzbar.pyzbar import ZBarSymbol


window = tk.Tk()
window.title('Attendance System')
window.geometry('950x500')
my_font1 = ('times', 12, 'bold')

year = tk.StringVar()
branch = tk.StringVar()
batch = tk.StringVar()
lecture = tk.StringVar()

title = tk.Label(window, text="ATTENDANCE SYSTEM", bd=10, relief=tk.GROOVE, font=(
    "Sketch Rockwell", 35), bg="lavender", fg="black")
title.pack(side=tk.TOP, fill=tk.X)


frame = Frame(window, width=600, height=530, bg="blue")
frame.place(x=400, y=85)
img = PhotoImage(file='background.png')
Label(frame, image=img, bg="white").place(x=0, y=0)

Manage_Frame = Frame(window, bg="grey")
Manage_Frame.place(x=0, y=80, width=400, height=530)

def show():
    # file = filedialog.askopenfilename(filetypes=[("Excel file", ".xlsx")])
    # df = pd.read_excel(file)  # creating DataFrame
    # print(df.to_markdown())
    #######################################
    my_wf = tk.Tk()
    # Toplevel(my_wf)
    my_wf.geometry("690x400")  # Size of the window
    my_wf.title('Attendance')
    my_wf.resizable(False, False)
    my_wf.lift()
    my_wf.configure(bg="white")
    my_wf.call('wm', 'attributes', '.', '-topmost', True)
    my_font1 = ('times', 18, 'bold')
    
    def upload_file():
        file = filedialog.askopenfilename(filetypes=[("Excel file", ".xlsx")])
        df = pd.read_excel(file)
        sg = pd.read_csv(df.to_csv())  # creating DataFrame
        print(df)
        print(sg)
        t1.delete('1.0', END)  # Delete previous data from position 0 till end
        # t1.insert(tk.END, df.head())  # adding data to text widget
        t1.insert('1.0', df)  # adding data to text widget

        # dff = pd.DataFrame(file)
        # cols = list(dff.columns)
        # tree = ttk.Treeview(my_wf)
        # tree.grid()
        # tree["columns"] = cols
        # for i in cols:
        #     tree.column(i, anchor="w")
        #     tree.heading(i, text=i, anchor='w')

        # for index, row in dff.iterrows():
        #     tree.insert("", 0, text=index, values=list(row))








    b1 = tk.Button(my_wf, text='Select Attendance Sheet',
                   width=20, command=upload_file)
    b1.grid(row=1, column=1)
    l1 = tk.Label(my_wf, text='Attendance', bd=10,width=21, relief=tk.GROOVE, font=("Sketch Rockwell", 35))
    l1.grid(row=0, column=1, sticky=S)
    t1 = tk.Text(my_wf, height=10, width=55, bg='white',
                 font=("Calibri", 15))  # added one text box
    t1.grid(row=2, column=1, pady=10,padx=20)
    my_wf.mainloop()
# b1 = tk.Button(frame, text='Upload Excel File', width=20, command=upload_file)
# b1.grid(row=1, column=1)
b1 = tk.Button(Manage_Frame, width=20, bg="#57a1f8", fg='white', border=0,
               font=my_font1, text="Attendance", command=show)
b1.place(x=200, y=370)






ttk.Label(window, text="Year", background="white", foreground="black",
          font=("Times New Roman", 15)).place(x=100, y=150)
combo_search = ttk.Combobox(window, textvariable=year, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ('1', '2', '3', '4')
combo_search.place(x=250, y=150)

ttk.Label(window, text="Branch", background="white", foreground="black",
          font=("Times New Roman", 15)).place(x=100, y=200)
combo_search = ttk.Combobox(window, textvariable=branch, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ("CSE", "AIML", "CE", "IT", "MECH", "ECM")
combo_search.place(x=250, y=200)

ttk.Label(window, text="Batch", background="white", foreground="black",
          font=("Times New Roman", 15)).place(x=100, y=250)
combo_search = ttk.Combobox(window, textvariable=batch, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ('A', 'B', 'C', 'D')
combo_search.place(x=250, y=250)

ttk.Label(window, text="Lecture", background="white",
          foreground="black", font=("Times New Roman", 15)).place(x=100, y=300)
combo_search = ttk.Combobox(window, textvariable=lecture, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ('1', '2', '3', '4', '5', '6', '7')
combo_search.place(x=250, y=300)

path = os.getcwd()


def generate():
    filename = filedialog.askopenfilename(initialdir=path, title="Select a File", filetypes=(
        ("Text files",  "*.txt*"), ("all files", "*.*")))
    print(filename)
    if(filename != ""):
        f = open(filename, 'r')
        lines = f.read().split("\n")
        print(filename)
        print(lines)
        #path=os.getcwd()
        new = path+"\QR"

        for _ in range(0, len(lines)):
            data = lines[_]
            version, level, qr = myqr.run(
                str(data),
                level='H',
                version=1,
                picture="Bg.png",
                colorized=True,
                contrast=1.0,
                brightness=1.0,
                save_name=str(lines[_]+'.png'),
                save_dir=new)
    else:
        messagebox.showwarning("Warning", "Please select file!!")


def check():
    if(year.get() and branch.get() and lecture.get() and batch.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")


exit_button = tk.Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=(
    "Times New Roman", 15), text="Submit", command=check)
exit_button.place(x=50, y=400)

generate_button = tk.Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=(
    "Times New Roman", 15), text="Generate QR", command=generate)
generate_button.place(x=225, y=400)

button_exit = Button(window, width=10, bg="#57a1f8", fg='white', border=0, font=(
    "Times New Roman", 15), text="Exit", command=exit)
button_exit.place(x=400, y=400)


# Manag_Frame=Frame(window,bg="red")
# Manag_Frame.place(x=580,y=80,width=450,height=530)

# canvas = Canvas(Manag_Frame, width = 300, height = 300,background="lavender")
# canvas.pack()
# img = PhotoImage(file="Bg.png")
# canvas.create_image(50,50, anchor=NW, image=img)

window.mainloop()

cap = cv2.VideoCapture(0)
names = []
today = date.today()
d = today.strftime("%b-%d-%Y")

counter = 0
filename = (d)

if (os.path.exists(filename+".xlsx") == False):
    filename = (filename)
else:
    while (os.path.exists(filename+"("+str(counter+1)+")"+".xlsx") == True):
        counter += 1
    filename = (filename+"("+str(counter+1)+")")

print("\nThe file name is : "+filename)
# fob = open(filename+'.xlsx', 'w+')
# fob.write("Name"+'\t')
# fob.write("Class & batch"+'\t')
# fob.write("Year"+'\t')
# fob.write("Lecture"+'\t')
# fob.write("In Time"+'\n')
# filename = "output/suyog.xlsx"
f = xlsxwriter.Workbook(filename+'.xlsx')
fob = f.add_worksheet()
fob.write('A1', 'Name')
fob.write('B1', 'Class & batch')
fob.write('C1', 'Year')
fob.write('D1', 'Lecture')
fob.write('E1', 'In Time')
roww = 1
def enterData(z):
    global roww
    if z in names:
        pass
    else:
        it = datetime.now()
        names.append(z)
        z = (z.decode('utf-8'))
        intime = it.strftime("%I:%M %p")
        my_list = [z, branch.get()+'-'+batch.get(), year.get(), lecture.get(), intime]
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


while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame, symbols=[ZBarSymbol.QRCODE])
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow("Scanner", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

f.close()
print('smart generated imp')
