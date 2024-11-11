import tkinter as tk
#mengimport pustaka tkinter
from tkinter import messagebox
#mengimport pustaka messagebox
from PIL import Image, ImageTk
#mengimport pustaka Pillow untuk memuat dan menampilkan gambar


def hasil_prediksi(): #mendefinisikan hasil_prediksi
    hasil_label.config(text="Hasil Prediksi: Teknologi Informasi") #menampilkan tampilan untuk menampilkan Teknologi Informais

root = tk.Tk() #membuat jendela utama aplikasi
root.title("Aplikasi Prediksi Prodi Pilihan") #Menetapkan judul jendela
root.geometry("600x600") #membuat ukuran untuk jendela

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Broadway", 16, "bold")) #menentukan jenis font pada tulisan aplikasi prediksi prodi pilihan dengan ukurna teks
judul_label.pack(pady=10) #menempatkan  label dengan jarak 10 pixel 

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

for i in range(1, 11): #loop berjalan dari 1 hingga 11 kali
    tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i}:", font=("Broadway", 10)).grid(row=i, column=0, sticky="w", padx=10, pady=5) #menempatkan jarak pada label
    tk.Entry(input_frame, width=10).grid(row=i, column=1, padx=10, pady=5) #menemaptkan jarak pada entry
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Broadway", 12, "bold")) #mengatur teks pada hasil prediksi
prediksi_button.pack(pady=20)


hasil_label = tk.Label(root, text="Hasil Prediksi: ", font=("Broadway", 12)) #membuat label kosong untuk menampilkan hasil
hasil_label.pack(pady=10) #menempatkan label dengan jarak 10 pixel secara vertical

root.mainloop()
#menjalankan aplikasi



