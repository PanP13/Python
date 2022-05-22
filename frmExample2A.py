from textwrap import fill
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import bgcolor
import pyodbc
import re

class HocSinh:

    def __init__(self, root):
        self.window = root
        self.window.title("Quản lý học sinh")
        self.window.geometry("1350x600+0+0")
        self.window.config(bg = "black")

        # Color
        self.color_1 = '#F1EEE9'
        self.color_2 = '#A0BCC2'
        self.color_3 = '#251D3A'
        self.color_4 = 'white'
        self.font_1 = 'black'

        # Variable
        self.MaSoHS = StringVar()
        self.HoTen = StringVar()
        self.Lop = StringVar()
        self.GioiTinh = StringVar()
        self.NgaySinh = StringVar()
        self.DiaChi = StringVar()
        self.DanToc = StringVar()
        self.Email = StringVar()

        # Frame
        self.datafrm = Frame(self.window, bg=self.color_1, width=1000, height=600)
        self.datafrm.pack(side=LEFT, fill=BOTH, expand=1)
        self.datafrm.columnconfigure(0, weight=1)
        self.datafrm.columnconfigure(1, weight=3)

        self.btnfrm = Frame(self.window, bg='#DAE5D0', width=300)
        self.btnfrm.pack(side=RIGHT, fill=BOTH, expand=0)

        # Buttons
        self.Thembtn = Button(self.btnfrm, text='Thêm', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.ThemHS).pack(fill=BOTH, expand=1, pady=5)
        self.Suabtn = Button(self.btnfrm, text='Sửa', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.SuaHS).pack(fill=BOTH, expand=1, pady=5)
        self.Xoabtn = Button(self.btnfrm, text='Xóa', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.XoaHS).pack(fill=BOTH, expand=1, pady=5)
        self.TimKiembtn = Button(self.btnfrm, text='Tìm kiếm', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.TimKiemHS).pack(fill=BOTH, expand=1, pady=5)
        self.HienThibtn = Button(self.btnfrm, text='Hiển thị', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.HienThiDuLieuHS).pack(fill=BOTH, expand=1, pady=5)
        self.Thoatbtn = Button(self.btnfrm, text='Thoát', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.Thoat).pack(fill=BOTH, expand=1, pady=5)

    # Widget
    def showMaSoHS(self):
        self.lblMaSoHS = Label(self.datafrm, text='Mã số', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblMaSoHS.grid(row=0, column=0, pady=5)
        self.txtMaSoHS = Entry(self.datafrm, font=('arial', 15, 'bold'), bg=self.color_4, textvariable=self.MaSoHS)
        self.txtMaSoHS.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    def showMaSoHS2(self):
        self.lblMaSoHS = Label(self.datafrm, text='Nhập mã số học sinh', font=('arial', 30, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblMaSoHS.grid(row=0, columnspan=2, pady=5, sticky='n')
        self.txtMaSoHS = Entry(self.datafrm, font=('arial', 20, 'bold'), bg=self.color_4, textvariable=self.MaSoHS)
        self.txtMaSoHS.grid(row=1, columnspan=2, padx=200, pady=5, sticky='ew')
        self.txtMaSoHS.focus()

    def showHoTen(self):
        self.lblHoTen = Label(self.datafrm, text='Họ tên', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblHoTen.grid(row=1, column=0, pady=5)
        self.txtHoTen = Entry(self.datafrm, font=('arial', 15, 'bold'), bg=self.color_4, textvariable=self.HoTen)
        self.txtHoTen.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

    def showCbxGioiTinh(self):
        self.lblGioiTinh = Label(self.datafrm, text='Giới tính', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblGioiTinh.grid(row=2, column=0, pady=5)
        self.cbxGioiTinh = ttk.Combobox(self.datafrm, font=('arial', 15, 'bold'), state='readonly', textvariable=self.GioiTinh)
        self.cbxGioiTinh['values'] = ('Nam', 'Nữ')
        self.cbxGioiTinh.current(0)
        self.cbxGioiTinh.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

    def showNgaySinh(self):
        self.lblNgaySinh = Label(self.datafrm, text='Ngày sinh', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblNgaySinh.grid(row=3, column=0, pady=5)
        self.txtNgaySinh = Entry(self.datafrm, font=('arial', 15, 'bold'), bg=self.color_4, textvariable=self.NgaySinh)
        self.txtNgaySinh.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

    def showDiaChi(self):
        self.lblDiaChi = Label(self.datafrm, text='Địa chỉ', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblDiaChi.grid(row=4, column=0, pady=5)
        self.txtDiaChi = Entry(self.datafrm, font=('arial', 15, 'bold'), bg=self.color_4, textvariable=self.DiaChi)
        self.txtDiaChi.grid(row=4, column=1, padx=5, pady=5, sticky='ew')

    def showCbxDanToc(self):
        self.lblDanToc = Label(self.datafrm, text='Giới tính', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblDanToc.grid(row=5, column=0, pady=5)
        self.cbxDanToc = ttk.Combobox(self.datafrm, font=('arial', 15, 'bold'), state='readonly', textvariable=self.DanToc)
        self.cbxDanToc['values'] = ('Kinh', 'Hoa', 'Chăm', 'Khmer')
        self.cbxDanToc.current(0)
        self.cbxDanToc.grid(row=5, column=1, padx=5, pady=5, sticky='ew')

    def showEmail(self):
        self.lblEmail = Label(self.datafrm, text='Email', font=('arial', 15, 'bold'), bg=self.color_1, fg=self.font_1)
        self.lblEmail.grid(row=6, column=0, pady=5)
        self.txtEmail = Entry(self.datafrm, font=('arial', 15, 'bold'), bg=self.color_4, textvariable=self.Email)
        self.txtEmail.grid(row=6, column=1, padx=5, pady=5, sticky='ew')

    def ThemHS(self):
        self.ClearScreen()

        self.showMaSoHS()
        self.showHoTen()
        self.showCbxGioiTinh()
        self.showNgaySinh()
        self.showDiaChi()
        self.showCbxDanToc()
        self.showEmail()
        
        self.NhapThembtn = Button(self.datafrm, text='Nhập', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.ThemDuLieuHS).grid(row=7, columnspan=2, padx=5, pady=5, sticky='ew')

    def SuaHS(self):
        self.ClearScreen()

        self.showMaSoHS2()

        self.NhapSuabtn = Button(self.datafrm, text='Nhập', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.LayThongTinHS_Sua).grid(row=3, columnspan=2, padx=500, pady=5, sticky='ew')

    def XoaHS(self):
        self.ClearScreen()

        self.showMaSoHS2()

        self.NhapXoabtn = Button(self.datafrm, text='Nhập', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.XoaDuLieuHS).grid(row=3, columnspan=2, padx=500, pady=5, sticky='ew')

    def TimKiemHS(self):
        self.ClearScreen()

        self.showMaSoHS2()

        self.XacNhanTKbtn = Button(self.datafrm, text='Nhập', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.LayThongTinHS_TK).grid(row=3, columnspan=2, padx=500, pady=5, sticky='ew')


    def ThemDuLieuHS(self):
        # Allows a number between 2000 and 2019
        yearReg = '(200[0-9]|201[0-9])'
        # Allows a number between 01 and 12 
        monthReg = '(0[1-9]|1[0-2])'
        # Allows a number between 01 and 31   
        dayReg = '(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
        # Pattern ngày sinh
        dobReg = dayReg + '-' + monthReg + '-' + yearReg

        if self.MaSoHS.get() == "" or self.HoTen.get() == "" or self.GioiTinh.get() == "" or self.NgaySinh.get() == "" or self.GioiTinh.get() == "" or self.DiaChi.get() == "" or self.DanToc.get() == "" or self.Email.get() == "":
            messagebox.showerror("Lỗi","Dữ liệu không được trống.",parent=self.window)
        elif not re.match('HS\d{4}', self.MaSoHS.get()):
            messagebox.showerror("Lỗi","Mã số học sinh không đúng định dạng.", parent=self.window)
        elif re.match('.*\d+', self.HoTen.get()):
            messagebox.showerror("Lỗi","Họ tên không được có số.", parent=self.window)
        elif not re.match(dobReg, self.NgaySinh.get()):
            messagebox.showerror("Lỗi","Ngày sinh không đúng định dạng.", parent=self.window)    
        else:
            try:
                connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                        'Server=THERICH;'
                        'Database=Python;'
                        'Trusted_Connection=yes;')
                curs = connection.cursor()
                curs.execute("select * from HocSinh where MaHocSinh=?", self.MaSoHS.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The MaHocSinh number is already exists, please try again with another number",parent=self.window)
                else:
                    curs.execute("insert into HocSinh values(?,?,?,?,?,?,?)",
                                            self.MaSoHS.get(),
                                            self.HoTen.get(),
                                            self.GioiTinh.get(),
                                            self.NgaySinh.get(),
                                            self.DiaChi.get(),
                                            self.DanToc.get(),
                                            self.Email.get())
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.Reset()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
    # ==================== Sửa ====================
    def LayThongTinHS_Sua(self):
        if self.MaSoHS.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập mã số học sinh",parent=self.window)
        else:
            try:
                connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                      'Server=THERICH;'
                      'Database=Python;'
                      'Trusted_Connection=yes;')
                curs = connection.cursor()
                curs.execute("select * from HocSinh where MaHocSinh=?", self.MaSoHS.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Lỗi",f"Không tồn tại học sinh mang mã số {self.MaSoHS.get()}",parent=self.window)
                else:
                    self.HienThiDuLieuHS_Sua(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
    def HienThiDuLieuHS_Sua(self, data):
        self.ClearScreen()

        self.showMaSoHS()
        self.showHoTen()
        self.showCbxGioiTinh()
        self.showNgaySinh()
        self.showDiaChi()
        self.showCbxDanToc()
        self.showEmail()
        self.Reset()

        self.txtMaSoHS.insert(0, data[0])
        self.txtHoTen.insert(0, data[1])
        self.cbxGioiTinh.set(data[2])
        self.txtNgaySinh.insert(0, data[3])
        self.txtDiaChi.insert(0, data[4])
        self.cbxDanToc.set(data[5])
        self.txtEmail.insert(0, data[6])

        self.txtMaSoHS.config(state=DISABLED, disabledbackground=self.color_2, disabledforeground=self.color_3)
        self.XacNhan = Button(self.datafrm, text='Xác nhận', font=('arial', 20, 'bold'), bg=self.color_2, fg=self.color_3, cursor='hand2', command=self.SuaDuLieuHS).grid(row=7, columnspan=2, padx=500, pady=5, sticky='ew')

    def SuaDuLieuHS(self):
        # Allows a number between 2000 and 2019
        yearReg = '(200[0-9]|201[0-9])'
        # Allows a number between 01 and 12 
        monthReg = '(0[1-9]|1[0-2])'
        # Allows a number between 01 and 31   
        dayReg = '(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
        # Pattern ngày sinh
        dobReg = dayReg + '-' + monthReg + '-' + yearReg

        if self.MaSoHS.get() == "" or self.HoTen.get() == "" or self.GioiTinh.get() == "" or self.NgaySinh.get() == "" or self.GioiTinh.get() == "" or self.DiaChi.get() == "" or self.DanToc.get() == "" or self.Email.get() == "":
            messagebox.showerror("Lỗi","Dữ liệu không được trống.",parent=self.window)
        elif not re.match('HS\d{4}', self.MaSoHS.get()):
            messagebox.showerror("Lỗi","Mã số học sinh không đúng định dạng.", parent=self.window)
        elif re.match('.*\d+', self.HoTen.get()):
            messagebox.showerror("Lỗi","Họ tên không được có số.", parent=self.window)
        elif not re.match(dobReg, self.NgaySinh.get()):
            messagebox.showerror("Lỗi","Ngày sinh không đúng định dạng.", parent=self.window)    
        else:
            try:
                connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                        'Server=THERICH;'
                        'Database=Python;'
                        'Trusted_Connection=yes;')
                curs = connection.cursor()
                curs.execute("select * from HocSinh where MaHocSinh=?", self.MaSoHS.get())
                row=curs.fetchone()

                if row==None:
                    messagebox.showerror("Lỗi",f"Mã học sinh {self.MaSoHS.get()} không tồn tại.",parent=self.window)
                else:
                    curs.execute("update HocSinh set HoTen=?, GioiTinh=?, NgaySinh=?, DiaChi=?, DanToc=?, Email=? where MaHocSinh=?",
                                    self.HoTen.get(),
                                    self.GioiTinh.get(),
                                    self.NgaySinh.get(),
                                    self.DiaChi.get(),
                                    self.DanToc.get(),
                                    self.Email.get(),
                                    row[0])
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Hoàn thành', "Dữ liệu đã được cập nhật")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
    # ==================== Xóa ====================
    def XoaDuLieuHS(self):
        if self.MaSoHS.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập mã số học sinh",parent=self.window)
        else:
            try:
                connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                      'Server=THERICH;'
                      'Database=Python;'
                      'Trusted_Connection=yes;')
                curs = connection.cursor()
                curs.execute("select * from HocSinh where MaHocSinh=?", self.MaSoHS.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Lỗi",f"Không tồn tại học sinh mang mã số {self.MaSoHS.get()}",parent=self.window)
                else:
                    curs.execute("delete from HocSinh where MaHocSinh=?", self.MaSoHS.get())
                    connection.commit()
                    messagebox.showinfo('Hoàn thành', "Dữ liệu đã bị xóa!")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    # ==================== Tìm kiếm ====================

    def LayThongTinHS_TK(self):
        if self.MaSoHS.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập mã số học sinh",parent=self.window)
        else:
            try:
                connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                      'Server=THERICH;'
                      'Database=Python;'
                      'Trusted_Connection=yes;')
                curs = connection.cursor()
                curs.execute("select * from HocSinh where MaHocSinh=?", self.MaSoHS.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Lỗi",f"Không tồn tại học sinh mang mã số {self.MaSoHS.get()}",parent=self.window)
                else:
                    self.HienThiDuLieuHS_TK(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
    def HienThiDuLieuHS_TK(self, data):
        self.ClearScreen()

        self.showMaSoHS()
        self.showHoTen()
        self.showCbxGioiTinh()
        self.showNgaySinh()
        self.showDiaChi()
        self.showCbxDanToc()
        self.showEmail()
        self.Reset()

        self.txtMaSoHS.insert(0, data[0])
        self.txtHoTen.insert(0, data[1])
        self.cbxGioiTinh.set(data[2])
        self.txtNgaySinh.insert(0, data[3])
        self.txtDiaChi.insert(0, data[4])
        self.cbxDanToc.set(data[5])
        self.txtEmail.insert(0, data[6])

        self.txtMaSoHS.config(state=DISABLED, disabledforeground=self.color_3)
        self.txtHoTen.config(state=DISABLED, disabledforeground=self.color_3)
        self.cbxGioiTinh.config(state=DISABLED)
        self.txtNgaySinh.config(state=DISABLED, disabledforeground=self.color_3)
        self.txtDiaChi.config(state=DISABLED, disabledforeground=self.color_3)
        self.cbxDanToc.config(state=DISABLED)
        self.txtEmail.config(state=DISABLED, disabledforeground=self.color_3)
    
    def HienThiDuLieuHS(self):
        try:
            connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                    'Server=THERICH;'
                    'Database=Python;'
                    'Trusted_Connection=yes;')
            curs = connection.cursor()
            curs.execute("select * from HocSinh")
            row=curs.fetchall()
            
            if row == None:
                messagebox.showerror("Lỗi",f"Không có dữ liệu",parent=self.window)
            else:
                for i in row:
                    print(i)
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def Reset(self):
        self.txtMaSoHS.delete(0, END)
        self.txtHoTen.delete(0, END)
        self.txtNgaySinh.delete(0, END)
        self.cbxGioiTinh.current(0)
        self.txtDiaChi.delete(0, END)
        self.cbxDanToc.current(0)
        self.txtEmail.delete(0, END)

    def ClearScreen(self):
        for widget in self.datafrm.winfo_children():
            widget.destroy()

    def Thoat(self):
        self.window.destroy()

if __name__ == "__main__":
    win = Tk()
    obj = HocSinh(win)
    win.mainloop()