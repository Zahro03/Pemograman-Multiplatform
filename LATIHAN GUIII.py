import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
top.title("Pemograman Kelas B")
top.geometry("400x400")
top.resizable(False,False)

inputframe=tk.Frame(top)
inputframe.pack(padx=10,pady=10,fill="x",expand=True)

#Bikin tabel untuk Judul
var = tk.Label(inputframe,text="Aplikasi Predksi Prodi Pilihan")
var.pack()

#Bikin input 1
input=tk.Label(inputframe,text="Masukan Nama Depan: ")
input.pack(fill="x",expand=True)
e1=tk.Entry(inputframe)
e1.pack(padx=10,pady=10 ,fill= "x",expand=True)

#Bikin input 2
input2=tk.Label(inputframe,text="Masukan Nama Depan: ")
input2.pack(fill="x",expand=True)
e2=tk.Entry(inputframe)
e2.pack(padx=10,pady=10,fill="x",expand=True)

#Bikin Button
def onClickBut():
    Nama_Depan=e1.get()
    Nama_Belakang=e2.get()
    print("Nama Kamu Adalah:" + Nama_Depan+" " +Nama_Belakang)
    messagebox.showinfo("Keterangan","Nama Kamu Adalah:" +Nama_Depan+" " +Nama_Belakang)

tombol=tk.Button(inputframe,text="Submit",command=onClickBut)
tombol.pack(padx=10,pady=5,fill="x",expand=True)

top.mainloop()  