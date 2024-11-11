import tkinter as tk

from tkinter import messagebox

from PIL import Image, ImageTk

def hasil_prediksi():
    hasil_label.config(text="Hasil Prediksi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x600")

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Broadway", 16, "bold"))
judul_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

for i in range(1, 11):
    tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i}:", font=("Broadway", 10)).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    tk.Entry(input_frame, width=10).grid(row=i, column=1, padx=10, pady=5)
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"))
prediksi_button.pack(pady=20)


hasil_label = tk.Label(root, text="Hasil Prediksi: ", font=("Broadway", 12))
hasil_label.pack(pady=10)


root.mainloop()

