import sqlite3
from datetime import datetime
import pandas as pd
# Inisialisasi Database
def init_db():
    conn = sqlite3.connect('diagnosa_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS riwayat 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  waktu TEXT, penyakit TEXT, persentase TEXT, gejala TEXT)''')
    conn.commit()
    conn.close()

# Fungsi Simpan Data
def simpan_ke_db(penyakit, persentase, gejala):
    conn = sqlite3.connect('diagnosa_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO riwayat (waktu, penyakit, persentase, gejala) VALUES (?, ?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), penyakit, persentase, gejala))
    conn.commit()
    conn.close()

# Fungsi Ambil Data
def ambil_semua_riwayat():
    conn = sqlite3.connect('diagnosa_database.db')
    df = pd.read_sql_query("SELECT * FROM riwayat", conn)
    conn.close()
    return df
# Tambahkan ini di db_helper.py
def hapus_semua_riwayat():
    conn = sqlite3.connect('diagnosa_database.db')
    c = conn.cursor()
    # Menghapus semua baris di tabel riwayat
    c.execute("DELETE FROM riwayat")
    # Mengembalikan ID agar jika ada data baru, dimulai dari 1 lagi
    c.execute("DELETE FROM sqlite_sequence WHERE name='riwayat'")
    conn.commit()
    conn.close()