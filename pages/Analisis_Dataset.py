import streamlit as st
import pandas as pd
import numpy as np
from auth_helper import login_form, logout_button
st.set_page_config(page_title="Analisis Dataset", layout="wide")
# Cek login, jika gagal maka stop eksekusi halaman
if not login_form():
    st.stop()


# css
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Poppins:wght@300;400;600&display=swap');

    .stApp {
        background-color: #f8fafc;
        font-family: 'Poppins', sans-serif;
    }
    
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        background-color: white;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        border: 1px solid #f1f5f9;
    }
    
    h1, h2, h3 {
        font-family: 'Comfortaa', cursive !important;
        color: #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# KAMUS TERJEMAHAN PENYAKIT (Samakan dengan file Diagnosa)
TERJEMAHAN_PENYAKIT = {
    'dengue': 'Demam Berdarah (Dengue)',
    'typhoid': 'Tipes (Typhoid)',
    'tuberculosis': 'TBC (Tuberculosis)',
    'common cold': 'Flu Biasa (Common Cold)',
    'pneumonia': 'Paru-paru Basah (Pneumonia)',
    'gerd': 'Asam Lambung (GERD)',
    'allergy': 'Alergi (Allergy)',
    'fungal infection': 'Infeksi Jamur (Fungal Infection)',
    'malaria': 'Malaria',
    'hypertension': 'Darah Tinggi (Hypertension)',
    'asthma': 'Asma (Asthma)',
    'diabetes': 'Diabetes (Kencing Manis)'
}

st.title(" Analisis Dataset Kaggle")
st.write("Menampilkan statistik dari dataset yang telah difilter untuk target penyakit aplikasi.")

try:
    df = pd.read_csv('data.zip')
    target_col = 'diseases' 
    
    # Standardisasi format teks
    df[target_col] = df[target_col].str.lower().str.strip()
    penyakit_indonesia = list(TERJEMAHAN_PENYAKIT.keys())

    # filter penyakit target
    df_filtered = df[df[target_col].isin(penyakit_indonesia)]
    
    # Jika kosong, jalankan fallback 10 terbanyak
    if df_filtered.empty:
        st.warning("⚠️ Menggunakan mode fallback: Penyakit target tidak ditemukan, menampilkan 10 penyakit terbanyak.")
        top_10 = df[target_col].value_counts().nlargest(10).index
        df_filtered = df[df[target_col].isin(top_10)]

   
    st.subheader("1. Cuplikan Data Latih (Raw Data)")
    st.write("Berikut adalah 10 baris data yang diambil secara **acak** dari dataset:")
    # Jika data kurang dari 10, tampilkan semua. Jika lebih, ambil acak 10 baris.
    if len(df_filtered) > 10:
        st.dataframe(df_filtered.sample(10)) 
    else:
        st.dataframe(df_filtered)

    # --- INFORMASI DATASET ---
    st.subheader("2. Informasi Dataset Terfilter")
    col1, col2 = st.columns(2)
    col1.metric("Total Data Kasus (Baris)", f"{df_filtered.shape[0]:,}")
    col2.metric("Total Fitur Gejala (Kolom)", f"{df_filtered.shape[1] - 1:,}")

    # --- GRAFIK DISTRIBUSI ---
    st.subheader("3. Distribusi Frekuensi Penyakit")
    distribusi = df_filtered[target_col].value_counts()
    
    # Ubah index grafik menjadi bahasa Indonesia menggunakan kamus
    distribusi.index = distribusi.index.map(lambda x: TERJEMAHAN_PENYAKIT.get(x, x.title()))
    
    st.bar_chart(distribusi)
    
    # === ALAT BANTU DEVELOPER ===
    st.divider()
    with st.expander(" Alat Bantu Developer: Lihat Semua Daftar Penyakit Asli"):
        semua_penyakit = df['diseases'].unique()
        st.dataframe(pd.DataFrame(semua_penyakit, columns=["Nama Asli di Dataset (Bahasa Inggris)"]))

except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat data: {e}")
