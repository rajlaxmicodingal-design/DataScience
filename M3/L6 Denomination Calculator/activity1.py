from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Dednomination Calculator")
window.geometry("650x400")

upload = Image.open("apple.jpg")
uplaoded = upload.resize((300,300))
image1 = ImageTk.PhotoImage(uplaoded)

lable = Label(window,image=image1,bg="#ADD8E6")
lable.place(x=180,y=20)

lable2 = Label(window,text="Welcome to the Denomination Calculator !")
lable2.place(x=180,y=340)

def msg() :
    x = messagebox.showinfo("Alert","Do you want to calculate the notes ? ")
    if x=="ok" :
        topwin()

button = Button(window,bg="red",fg="white",command=msg,text="Let's get Started !")
button.place(x=260,y=360)

def topwin() :
    top = Toplevel()
    top.configure(bg="lightgrey")
    top.geometry("650x450")
    top.title("Calculator")
    lable3 = Label(top,text="Enter the amount you wish")
    entry= Entry(top)

    lable4 = Label(top,text="₹500")
    lable5 = Label(top,text="₹200")
    lable6 = Label(top,text="₹100")
    lable7 = Label(top,text="₹50")
    lable8 = Label(top,text="₹10")
    lable9 = Label(top,text="₹5")
    lable10 = Label(top,text="₹1")

    entry4 = Entry(top)
    entry5 = Entry(top)
    entry6 = Entry(top)
    entry7 = Entry(top)
    entry8 = Entry(top)
    entry9 = Entry(top)
    entry10 = Entry(top)

    def calculator() :
        global amount
        amount = int(entry.get())
        n500 = amount//500
        amount%= 500
        n200 = amount//200
        amount%= 200
        n100 = amount//100
        amount%= 100
        n50 = amount//50
        amount%= 50
        n10 = amount//10
        amount%= 10
        n5 = amount//5
        amount%= 5
        n1 = amount

        entry4.delete(0,END)
        entry5.delete(0,END)
        entry6.delete(0,END)
        entry7.delete(0,END)
        entry8.delete(0,END)
        entry9.delete(0,END)
        entry10.delete(0,END)

        entry4.insert(END,str(n500))
        entry5.insert(END,str(n200))
        entry6.insert(END,str(n100))
        entry7.insert(END,str(n50))
        entry8.insert(END,str(n10))
        entry9.insert(END,str(n5))
        entry10.insert(END,str(n1))
    buttun = Button(top,command=calculator,text="Calculate",fg="white",bg="blue")

    lable3.place(x=200,y=50)
    lable4.place(x=180,y=200)
    lable5.place(x=180,y=230)
    lable6.place(x=180,y=260)
    lable7.place(x=180,y=290)
    lable8.place(x=180,y=320)
    lable9.place(x=180,y=350)
    lable10.place(x=180,y=380)

    entry.place(x=200,y=80)
    entry4.place(x=270,y=200)
    entry5.place(x=270,y=230)
    entry6.place(x=270,y=260)
    entry7.place(x=270,y=290)
    entry8.place(x=270,y=320)
    entry9.place(x=270,y=350)
    entry10.place(x=270,y=380)

    buttun.place(x=240,y=120)

    top.mainloop()

window.mainloop()