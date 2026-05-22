import streamlit as st
import pandas as pd
from auth_helper import login_form

# 1. Pastikan fungsi hapus_semua_riwayat di-import dari db_helper
from db_helper import ambil_semua_riwayat, hapus_semua_riwayat

# 2. SET CONFIG (HARUS PALING PERTAMA)
st.set_page_config(page_title="Riwayat Diagnosa", page_icon="🕒", layout="wide")

# 3. CEK LOGIN
if not login_form():
    st.stop()

# 4. KONTEN HALAMAN
st.title("🕒 Riwayat Diagnosa")
st.write("Berikut adalah riwayat diagnosa yang tersimpan secara permanen di database.")

# Mengambil data dari SQLite
df = ambil_semua_riwayat()

if not df.empty:
    # Menampilkan data dari database
    st.dataframe(df, use_container_width=True)
    
    # Tombol Hapus
    if st.button("Hapus Riwayat (Database)", type="primary"):
        hapus_semua_riwayat()           # 1. Eksekusi hapus di database
        st.success("Semua riwayat berhasil dihapus!") # 2. Tampilkan notifikasi
        st.rerun()                      # 3. Refresh halaman agar tabel kosong
else:
    st.info("Belum ada riwayat diagnosa yang tersimpan.")