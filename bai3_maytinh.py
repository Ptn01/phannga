import tkinter as tk

giaodien = tk.Tk()
giaodien.title("Calculator")
giaodien.geometry('200x200')

# label = tk.Label(giaodien, text = "CALCULATOR", fg = 'black')
# label.grid(column=2, row=0, columnspan=3)


dulieu = tk.StringVar()
textbox1 = tk.Entry(giaodien, width= 15, font=('arial bold', 10), bd=0, justify="left", textvariable=dulieu)
textbox1.grid(column=1, row=2,columnspan=3, padx = 1, pady = 1)
textbox1.focus()

pc = ""
def bien(num):
    global pc
    pc += str(num)
    dulieu.set(pc)
    
def ketqua():
    try:
        global pc
        total = str(eval(pc))
        dulieu.set(total)
        pc = ""
    except:
        dulieu.set(" error ")
        pc = ""
        
def xoa():
    global pc
    pc = ""
    dulieu.set("")
    
def phantram():
    global pc
    pc = float(int(pc)/100)
    dulieu.set(pc)


button1 = tk.Button(giaodien, text = "+", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien("+"), height=1, width=3)
button1.grid(column=4, row=4, padx = 1, pady = 1)

button2 = tk.Button(giaodien, text = "-", bg='white', fg='black', font=("Tahoma bold", 8),command=lambda: bien("-"), height=1, width=3)
button2.grid(column=4, row=6, padx = 1, pady = 1)

button3 = tk.Button(giaodien, text = "*", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien("*"), height=1, width=3)
button3.grid(column=4, row=8, padx = 1, pady = 1)

button4 = tk.Button(giaodien, text = "/", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien("/"), height=1, width=3)
button4.grid(column=4, row=10, padx = 1, pady = 1)

button5 = tk.Button(giaodien, text = "0", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(0), height=1, width=3)
button5.grid(column=1, row=10, padx = 1, pady = 1)

button6 = tk.Button(giaodien, text = "000", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien("000"), height=1, width=3)
button6.grid(column=2, row=10, padx = 1, pady = 1)

button7 = tk.Button(giaodien, text = ".", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien("."), height=1, width=3)
button7.grid(column=3, row=10, padx = 1, pady = 1)

button8 = tk.Button(giaodien, text = "1", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(1), height=1, width=3)
button8.grid(column=3, row=8, padx = 1, pady = 1)

button9 = tk.Button(giaodien, text = "2", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(2), height=1, width=3)
button9.grid(column=2, row=8, padx = 1, pady = 1)

button10 = tk.Button(giaodien, text = "3", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(3), height=1, width=3)
button10.grid(column=1, row=8, padx = 1, pady = 1)

button11 = tk.Button(giaodien, text = "4", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(4), height=1, width=3)
button11.grid(column=3, row=6, padx = 1, pady = 1)

button12 = tk.Button(giaodien, text = "5", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(5), height=1, width=3)
button12.grid(column=2, row=6, padx = 1, pady = 1)

button13 = tk.Button(giaodien, text = "6", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(6), height=1, width=3)
button13.grid(column=1, row=6, padx = 1, pady = 1)

button14 = tk.Button(giaodien, text = "7", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(7), height=1, width=3)
button14.grid(column=3, row=4, padx = 1, pady = 1)

button15 = tk.Button(giaodien, text = "8", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(8), height=1, width=3)
button15.grid(column=2, row=4, padx = 1, pady = 1)

button16 = tk.Button(giaodien, text = "9", bg='white', fg='black', font=("Tahoma bold", 8), command=lambda: bien(9), height=1, width=3)
button16.grid(column=1, row=4, padx = 1, pady = 1)

button17 = tk.Button(giaodien, text = "C", bg='white', fg='black', font=("Tahoma bold", 8), command= xoa, height=1, width=3)
button17.grid(column=4, row=2, padx = 1, pady = 1)

button18 = tk.Button(giaodien, text = "Result", bg='white', fg='black', font=("Tahoma bold", 8), command= ketqua, height=1, width=15)
button18.grid(column=1, row=12, columnspan=3, padx = 1, pady = 1)

button19 = tk.Button(giaodien, text = "%", bg='white', fg='black', font=("Tahoma bold", 8), command= phantram, height=1, width=3)
button19.grid(column=4, row=12, padx = 1, pady = 1)

giaodien.mainloop()