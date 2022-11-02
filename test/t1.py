window.destroy()
screen = Tk()
screen.title('Attendance System')
screen.geometry('1000x500+150+100')

year = tk.StringVar()
branch = tk.StringVar()
batch = tk.StringVar()
lecture = tk.StringVar()

title = tk.Label(screen, text="ATTENDANCE SYSTEM", bd=10, relief=tk.GROOVE, font=("Sketch Rockwell", 35), bg="lavender", fg="black")
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
#
ttk.Label(screen, text="Branch", background="white", foreground="black",
          font=("Times New Roman", 15)).place(x=100, y=200)
combo_search = ttk.Combobox(screen, textvariable=branch, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ("CSE", "AIML", "CE", "IT", "MECH", "ECM")
combo_search.place(x=250, y=200)
#
ttk.Label(screen, text="Batch", background="white", foreground="black",
          font=("Times New Roman", 15)).place(x=100, y=250)
combo_search = ttk.Combobox(screen, textvariable=batch, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ('A', 'B', 'C', 'D')
combo_search.place(x=250, y=250)
#
ttk.Label(screen, text="Lecture", background="white",
          foreground="black", font=("Times New Roman", 15)).place(x=100, y=300)
combo_search = ttk.Combobox(screen, textvariable=lecture, width=10, font=(
    "times new roman", 13), state='readonly')
combo_search['values'] = ('1', '2', '3', '4', '5', '6', '7')
combo_search.place(x=250, y=300)
#
path = os.getcwd()
#
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
        #
        p = "qr/test.txt"
        os.makedirs(os.path.dirname(p), exist_ok=True)
        new = path+"\qr"
        #
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
#
def check():
    if(year.get() and branch.get() and lecture.get() and batch.get()):
        screen.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")
#
exit_button = tk.Button(screen, width=10, bg="#57a1f8", fg='white', border=0, font=(
    "Times New Roman", 15), text="Submit", command=check)
exit_button.place(x=50, y=400)
#
generate_button = tk.Button(screen, width=10, bg="#57a1f8", fg='white', border=0, font=(
    "Times New Roman", 15), text="Generate QR", command=generate)
generate_button.place(x=225, y=400)
#
button_exit = Button(screen, width=10, bg="#57a1f8", fg='white', border=0, font=(
    "Times New Roman", 15), text="Exit", command=exit)
button_exit.place(x=400, y=400)
#
screen.mainloop()
#
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
names = []
today = date.today()
d = today.strftime("%b-%d-%Y")
#
counter = 0
filename = (d)
#
if (os.path.exists("attendance/"+filename+".xlsx") == False):
    filename = (filename)
else:
    while (os.path.exists("attendance/"+filename+"("+str(counter+1)+")"+".xlsx") == True):
        counter += 1
    filename = (filename+"("+str(counter+1)+")")
#
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
#
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
#
print('Reading...')
#
def checkData(data):
    # data=str(data)
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+' '+'present...')
        enterData(data)
##################################
#
# decode(Image.open('pyzbar/tests/qrcode.png'), symbols=[ZBarSymbol.QRCODE])
###############################################
while True:
    _, frame = cap.read()
    # decodedObjects = pyzbar.decode(frame)
    decodedObjects = pyzbar.decode(
        frame, symbols=[ZBarSymbol.QRCODE])
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
    #
    cv2.imshow("Scanner", frame)
    #
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(
            'Attendance is generated successfully in file named '+filename)
        cv2.destroyAllWindows()
        break
        #
f.close()
