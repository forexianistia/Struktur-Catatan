
import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

FILE = "data.csv"
TARGET = 1000000000  # Target Porsche (2M)

# ========================
# FUNGSI DATA
# ========================
def get_saldo():
    try:
        with open(FILE, "r") as f:
            rows = list(csv.reader(f))
            return int(rows[-1][4])
    except:
        return 0

def tambah_transaksi(deskripsi, masuk, keluar):
    saldo = get_saldo()
    saldo_baru = saldo + masuk - keluar
    tanggal = datetime.now().strftime("%Y-%m-%d")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([tanggal, deskripsi, masuk, keluar, saldo_baru])

    update_ui()

# ========================
# UI
# ========================
root = tk.Tk()
root.title("Jurnal Grow Uang")
root.geometry("400x500")
root.configure(bg="#0f172a")  # dark navy

# ========================
# HEADER (GOAL)
# ========================
label_goal = tk.Label(
    root,
    text="GOAL: PORSCHE 🏎️",
    font=("Helvetica", 16, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
label_goal.pack(pady=10)

# ========================
# SALDO
# ========================
saldo_var = tk.StringVar()

label_saldo = tk.Label(
    root,
    textvariable=saldo_var,
    font=("Helvetica", 24, "bold"),
    fg="white",
    bg="#0f172a"
)
label_saldo.pack(pady=20)

# ========================
# PROGRESS
# ========================
progress_var = tk.StringVar()

label_progress = tk.Label(
    root,
    textvariable=progress_var,
    font=("Helvetica", 12),
    fg="#94a3b8",
    bg="#0f172a"
)
label_progress.pack()

# ========================
# INPUT
# ========================
entry_desc = tk.Entry(root, width=30)
entry_desc.pack(pady=5)

entry_amount = tk.Entry(root, width=30)
entry_amount.pack(pady=5)

# ========================
# BUTTON STYLE
# ========================
btn_style = {
    "width": 20,
    "height": 2,
    "font": ("Helvetica", 10, "bold"),
    "bd": 0
}

def tambah_masuk():
    try:
        jumlah = int(entry_amount.get())
        tambah_transaksi(entry_desc.get(), jumlah, 0)
    except:
        messagebox.showerror("Error", "Input tidak valid")

def tambah_keluar():
    try:
        jumlah = int(entry_amount.get())
        tambah_transaksi(entry_desc.get(), 0, jumlah)
    except:
        messagebox.showerror("Error", "Input tidak valid")

btn_masuk = tk.Button(
    root,
    text="➕ Pemasukan",
    bg="#22c55e",
    fg="white",
    command=tambah_masuk,
    **btn_style
)
btn_masuk.pack(pady=10)

btn_keluar = tk.Button(
    root,
    text="➖ Pengeluaran",
    bg="#ef4444",
    fg="white",
    command=tambah_keluar,
    **btn_style
)
btn_keluar.pack(pady=5)

# ========================
# UPDATE UI
# ========================
def update_ui():
    saldo = get_saldo()
    saldo_var.set(f"Rp {saldo:,}")

    persen = (saldo / TARGET) * 100 if TARGET else 0
    progress_var.set(f"Progress: {persen:.5f}%")

update_ui()

root.mainloop()
