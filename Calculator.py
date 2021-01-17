from tkinter import *

global Number
Number = ""

def clicked(Choose):
    global Number
    if ((Choose >= 0) and (Choose <= 9)):
        Number = Number + str(Choose)
        lbl.configure(text = Number)
    elif (Choose == 15):
        Number = Number + "."
        lbl.configure(text = Number)
    elif (Choose == 10):
        Number = Number + "+"
        lbl.configure(text = Number)
    elif (Choose == 11):
        Number = Number + "-"
        lbl.configure(text = Number)
    elif (Choose == 12):
        Number = Number + "*"
        lbl.configure(text = Number)
    elif (Choose == 13):
        Number = Number + "/"
        lbl.configure(text = Number)
    elif (Choose == 17):
        Number = str(eval(Number))
        lbl.configure(text = Number)
    elif (Choose == 14):
        Number = ""
        lbl.configure(text = Number)
        
window = Tk()

window.title("Simple Calculator")
window.geometry('321x350')

lbl = Label(window, text="", font=("Arial Bold", 20), height="2")
lbl.grid(columnspan = 4, row = 0)

btn7 = Button(window, text="7", width = "10", height = "3", command = lambda:clicked(7))
btn7.grid(column = 0, row = 1)
btn8 = Button(window, text="8", width = "10", height = "3", command = lambda:clicked(8))
btn8.grid(column = 1, row = 1)
btn9 = Button(window, text="9", width = "10", height = "3", command = lambda:clicked(9))
btn9.grid(column = 2, row = 1)
btnCong = Button(window, text="+", width = "10", height = "3", command = lambda:clicked(10))
btnCong.grid(column = 3, row = 1)

btn4 = Button(window, text="4", width = "10", height = "3", command = lambda:clicked(4))
btn4.grid(column = 0, row = 2)
btn5 = Button(window, text="5", width = "10", height = "3", command = lambda:clicked(5))
btn5.grid(column = 1, row = 2)
btn6 = Button(window, text="6", width = "10", height = "3", command = lambda:clicked(6))
btn6.grid(column = 2, row = 2)
btnTru = Button(window, text="-", width = "10", height = "3", command = lambda:clicked(11))
btnTru.grid(column = 3, row = 2)

btn1 = Button(window, text="1", width = "10", height = "3", command = lambda:clicked(1))
btn1.grid(column = 0, row = 3)
btn2 = Button(window, text="2", width = "10", height = "3", command = lambda:clicked(2))
btn2.grid(column = 1, row = 3)
btn3 = Button(window, text="3", width = "10", height = "3", command = lambda:clicked(3))
btn3.grid(column = 2, row = 3)
btnNhan = Button(window, text="*", width = "10", height = "3", command = lambda:clicked(12))
btnNhan.grid(column = 3, row = 3)

btnDau = Button(window, text="C", width = "10", height = "3", command = lambda:clicked(14))
btnDau.grid(column = 0, row = 4)
btn0 = Button(window, text="0", width = "10", height = "3", command = lambda:clicked(0))
btn0.grid(column = 1, row = 4)
btnCham = Button(window, text=".", width = "10", height = "3", command = lambda:clicked(15))
btnCham.grid(column = 2, row = 4)
btnChia = Button(window, text="/", width = "10", height = "3", command = lambda:clicked(13))
btnChia.grid(column = 3, row = 4)

btnBang = Button(window, text="=", width = "45", height = "3", command = lambda:clicked(17))
btnBang.grid(columnspan = 4, row = 5)

window.mainloop()
