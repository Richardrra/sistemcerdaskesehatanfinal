import streamlit as st
import pandas as pd
from datetime import datetime
from auth_helper import login_form
from db_helper import init_db, simpan_ke_db


st.set_page_config(page_title="Diagnosa", layout="wide")

init_db()

if not login_form():
    st.stop()

#  DATA & KAMUS
TERJEMAHAN_PENYAKIT = {
    'dengue': 'Demam Berdarah (Dengue)', 'typhoid': 'Tipes (Typhoid)', 'tuberculosis': 'TBC (Tuberculosis)',
    'common cold': 'Flu Biasa (Common Cold)', 'pneumonia': 'Paru-paru Basah (Pneumonia)', 'gerd': 'Asam Lambung (GERD)',
    'allergy': 'Alergi (Allergy)', 'fungal infection': 'Infeksi Jamur (Fungal Infection)', 'malaria': 'Malaria',
    'hypertension': 'Darah Tinggi (Hypertension)', 'asthma': 'Asma (Asthma)', 'diabetes': 'Diabetes (Kencing Manis)'
}

TERJEMAHAN_GEJALA = {
    'chills': 'Menggigil', 'chest tightness': 'Dada Terasa Sesak', 'cough': 'Batuk', 'fever': 'Demam',
    'headache': 'Sakit Kepala', 'nausea': 'Mual', 'vomiting': 'Muntah', 'fatigue': 'Kelelahan',
    'sweating': 'Berkeringat', 'breathlessness': 'Sesak Napas', 'muscle pain': 'Nyeri Otot', 
    'joint pain': 'Nyeri Sendi', 'skin rash': 'Ruam Kulit', 'itching': 'Gatal-gatal',
    'stomach pain': 'Sakit Perut', 'chest pain': 'Nyeri Dada', 'loss of appetite': 'Hilang Nafsu Makan',
    'dizziness': 'Pusing', 'weight loss': 'Berat Badan Turun', 'sore throat': 'Sakit Tenggorokan'
}

def format_nama_gejala(gejala_raw):
    key = gejala_raw.lower().replace("_", " ").strip()
    return f"{TERJEMAHAN_GEJALA.get(key, gejala_raw.replace('_', ' ').title())} ({gejala_raw.replace('_', ' ').title()})"

@st.cache_data
def load_rules_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    if 'disease' in df.columns: df.rename(columns={'disease': 'diseases'}, inplace=True)
    df['diseases'] = df['diseases'].str.lower().str.strip()
    cf_dataframe = df[df['diseases'].isin(TERJEMAHAN_PENYAKIT.keys())].groupby('diseases').mean()
    rules = {d: {s: round(v, 2) for s, v in row.items() if v > 0} for d, row in cf_dataframe.iterrows()}
    return rules, list(TERJEMAHAN_PENYAKIT.keys())

rules, available_diseases = load_rules_from_csv('data.zip')
all_symptoms = sorted(list(set().union(*rules.values())))

# 5. UI
st.title(" Diagnosa Penyakit")
selected_symptoms_raw = st.multiselect("1. Pilih gejala:", options=all_symptoms, format_func=format_nama_gejala)

cf_user_options = {
    "Tidak" : 0.0,
    "Tidak Yakin" : 0.2,
    "Sedikit Yakin" : 0.4,
    "Cukup Yakin" : 0.6,
    "Yakin" : 0.8,
    "Sangat Yakin" : 1.0
}

user_inputs = {}
if selected_symptoms_raw:
    st.markdown("---")
    st.subheader("2. Seberapa yakin Anda dengan gejala tersebut?")
    
    for symptom in selected_symptoms_raw:
        # Menggunakan selectbox dengan teks seperti aslinya
        choice = st.selectbox(
            f"Tingkat keyakinan untuk {format_nama_gejala(symptom)}:", 
            options=list(cf_user_options.keys()), 
            index=3, # Default otomatis ke "Cukup Yakin"
            key=symptom
        )
        
        # Simpan nilai angkanya (float) ke dalam user_inputs
        if cf_user_options[choice] > 0: 
            user_inputs[symptom] = cf_user_options[choice]

# 6. ANALISIS
if st.button("Analisis Penyakit", type="primary", key="btn_analisis"):
    if not user_inputs:
        st.warning("Pilih gejala terlebih dahulu!")
    else:
        results = {}
        for disease, d_symptoms in rules.items():
            cf_gabungan = 0.0
            for s, cf_user in user_inputs.items():
                if s in d_symptoms:
                    cf_gejala = cf_user * d_symptoms[s]
                    cf_gabungan = cf_gabungan + cf_gejala * (1 - cf_gabungan) if cf_gabungan != 0 else cf_gejala
            if cf_gabungan > 0: results[disease] = cf_gabungan * 100

        if results:
            sorted_res = sorted(results.items(), key=lambda x: x[1], reverse=True)
            top_d, top_cf = sorted_res[0]
            nama_indo = TERJEMAHAN_PENYAKIT.get(top_d, top_d.title())
            gejala_str = ", ".join([format_nama_gejala(s) for s in user_inputs.keys()])
            
            st.success(f"**Kemungkinan Terbesar:** {nama_indo} ({top_cf:.2f}%)")
            
            # SIMPAN KE DATABASE
            simpan_ke_db(nama_indo, f"{top_cf:.2f}%", gejala_str)
            st.info("Hasil diagnosa telah disimpan ke riwayat.")
            
            st.dataframe(pd.DataFrame(sorted_res, columns=["Penyakit", "Persentase (%)"]))
        else:
            st.info("Gejala tidak cocok dengan data.")
