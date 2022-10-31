from tkinter import *

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
img = PhotoImage(file='splash.png')
Label(splash_root, image=img, bg="white").place(x=0, y=0)

def main_window():
    splash_root.destroy()
    root=Tk()
    root.title('Codemy.com - Splash Screens')
    root.iconbitmap('codemy.ico')
    root.geometry("925x500+200+100")
    root = Label(root, text="Splashhhhhh", font=("Times New Roman", 25))
    root.pack(pady=20)
    
splash_root.after(7000, main_window)

mainloop()
