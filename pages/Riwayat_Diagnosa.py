import streamlit as st
import pandas as pd
from auth_helper import login_form

from db_helper import ambil_semua_riwayat, hapus_semua_riwayat

#  SET CONFIG 
st.set_page_config(page_title="Riwayat Diagnosa",layout="wide")

# CEK LOGIN
if not login_form():
    st.stop()

#  KONTEN HALAMAN
st.title("Riwayat Diagnosa")
st.write("Berikut adalah riwayat diagnosa yang tersimpan secara permanen di database.")

# Mengambil data dari SQLite
df = ambil_semua_riwayat()

if not df.empty:
    # Menampilkan data dari database
    st.dataframe(df, use_container_width=True)
    
    # Tombol Hapus
    if st.button("Hapus Riwayat (Database)", type="primary"):
        hapus_semua_riwayat()          
        st.success("Semua riwayat berhasil dihapus!") 
        st.rerun()                      
else:
    st.info("Belum ada riwayat diagnosa yang tersimpan.")
