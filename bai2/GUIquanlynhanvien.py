import connect
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
giaodien = tk.Tk()
giaodien.title("Quản lý nhân viên")
giaodien.geometry('600x450')

label = tk.Label(giaodien, text = "CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN", fg = 'black', bg= 'white')
label.grid(column=3, row=0)

label0 = tk.Label(giaodien, font=("Arial", 10))
label0.grid(column=1, row=1)

label1 = tk.Label(giaodien, text = "Id", fg= "black", font=("Arial", 10))
label1.grid(column=0, row=2)

label2 = tk.Label(giaodien, text = "Name", fg= "black", font=("Arial", 10))
label2.grid(column=0, row=3)

label3 = tk.Label(giaodien, text = "Age", fg= "black", font=("Arial", 10))
label3.grid(column=0, row=4)

label4 = tk.Label(giaodien, text = "Country", fg= "black", font=("Arial", 10))
label4.grid(column=0, row=5)

label5 = tk.Label(giaodien, text = "Sex", fg= "black", font=("Arial", 10))
label5.grid(column=0, row=6)

label6 = tk.Label(giaodien, text = "Chức vụ", fg = 'black', font=("Arial", 10))
label6.grid(column=0, row=7)

label7 = tk.Label(giaodien, text = "Chấm công", fg= "black", font=("Arial", 10))
label7.grid(column=0, row=8)

label8 = tk.Label(giaodien, fg = 'black', font=("Time New Roman", 8))
label8.grid(column=3, row=15)

label9 = tk.Label(giaodien, fg = 'black', font=("Time New Roman", 8))
label9.grid(column=3, row=11)

Id = tk.IntVar()
textbox1 = tk.Entry(giaodien, width=30, textvariable= Id)
textbox1.grid(column=3, row=2)
textbox1.focus()

Name = tk.StringVar()
textbox2 = tk.Entry(giaodien, width=30, textvariable= Name)
textbox2.grid(column=3, row=3)
textbox2.focus()

Age = tk.IntVar()
textbox3 = tk.Entry(giaodien, width=30, textvariable= Age)
textbox3.grid(column=3, row=4)
textbox3.focus()

Country = tk.StringVar()
textbox4 = tk.Entry(giaodien, width=30, textvariable= Country)
textbox4.grid(column=3, row=5)
textbox4.focus()

Sex = tk.StringVar()
combobox5 = Combobox(giaodien)
combobox5['values'] = ('Male', 'Female', 'Unknown')
combobox5.grid(column=3,row=6)

Chucvu = tk.StringVar()
textbox6 = tk.Entry(giaodien, width=30, textvariable= Chucvu)
textbox6.grid(column=3, row=7)
textbox6.focus()

Chamcong = tk.IntVar()
textbox7 = tk.Entry(giaodien, width=30, textvariable= Chamcong)
textbox7.grid(column=3, row=8)
textbox7.focus()

scrolled = ScrolledText(giaodien,width=50,height = 10)
scrolled.grid(column=3,row=12)

#   Bước 2: Xây dựng chức năng
connection = connect.getConnection()
dulieu = connection.cursor()

def kiemtraketnoi():
    if (connection.is_connected):
        label8.config(text = "Kết nối thành công!!!")
    else:
        label8.config(text = "Kết nối không thành công")
        
button = tk.Button(giaodien, text = "Kiểm tra kết nối", bg='White', fg='black', font=("Arial Bold", 8), command= kiemtraketnoi)
button.grid(column=3, row=14)

def hienthi():
    dulieu.execute("SELECT * FROM quan_ly_nhan_vien.nhanvien")
    ketqua = dulieu.fetchall() 
    scrolled.configure(state="normal")
    scrolled.delete("1.0", tk.END)
    for i in ketqua:
        ketqua = str(i) + ","
        scrolled.configure(state = "normal")
        scrolled.insert(tk.INSERT, ketqua + "\n")
        scrolled.configure(state = "disable")
    return ketqua

button2 = tk.Button(giaodien, text = "Hiển thị nhân viên", bg='white', fg='black', font=("Arial Bold", 8), command= hienthi)
button2.grid(column=3, row=9)


def them():
    dulieu.execute("INSERT INTO Quan_ly_nhan_vien.`Nhanvien`(id,`Name`, Age, Country, Sex, Chucvu, Chamcong) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
        Id.get(),
        Name.get(),
        Age.get(),
        Country.get(),
        Sex.get(),
        Chucvu.get(),
        Chamcong.get()
    ))
    connection.commit()
    label9.config(text = "Đã thêm")
    textbox1.delete("0", tk.END)
    textbox2.delete("0", tk.END)
    textbox3.delete("0", tk.END)
    textbox4.delete("0", tk.END)
    combobox5.delete("0", tk.END)
    textbox6.delete("0", tk.END)
    textbox7.delete("0", tk.END)

button1 = tk.Button(giaodien, text = "Thêm nhân viên", bg='white', fg='black', font=("Arial Bold", 8), command= them)
button1.grid(column=1, row=9)
    
        
def sua():
    dulieu.execute("UPDATE Quan_ly_nhan_vien.Nhanvien SET Age = %s WHERE id = %s", (
        Age.get(),
        Id.get()
    ))
    connection.commit()
    label9.config(text = "Đã sửa")
    textbox1.delete("0", tk.END)
    textbox3.delete("0", tk.END)

button4 = tk.Button(giaodien, text = "Sửa nhân viên", bg='white', fg='black', font=("Arial Bold", 8), command= sua)
button4.grid(column=3, row=10)    
    
    
def xoa():
    Id_get = Id.get()
    sql = "DELETE FROM Quan_ly_nhan_vien.Nhanvien WHERE id = %s"
    dulieu.execute(sql, (Id_get, ))
    connection.commit()
    label9.config(text = "Đã xóa")
    textbox1.delete("0", tk.END)
    
button3 = tk.Button(giaodien, text = "Xóa nhân viên", bg='white', fg='black', font=("Arial Bold", 8), command= xoa)
button3.grid(column=1, row=10)

giaodien.mainloop()
