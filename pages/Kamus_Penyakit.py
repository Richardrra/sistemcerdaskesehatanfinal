import streamlit as st
import pandas as pd

from auth_helper import login_form, logout_button

st.set_page_config(page_title="Kamus Penyakit", layout="wide")
# Cek login, jika gagal maka stop eksekusi halaman
if not login_form():
    st.stop()
# css
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Poppins:wght@300;400;600&display=swap');

    .stApp { background-color: #f8fafc; font-family: 'Poppins', sans-serif; }
    div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
        background-color: white;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        border: 1px solid #f1f5f9;
    }
    h1, h2, h3 { font-family: 'Comfortaa', cursive !important; color: #1e293b; }
</style>
""", unsafe_allow_html=True)

# KAMUS 
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

# KAMUS TERJEMAHAN GEJALA 
TERJEMAHAN_GEJALA = {
    'chills': 'Menggigil', 'chest tightness': 'Dada Terasa Sesak', 'congestion in chest': 'Dada Terasa Penuh/Sesak',
    'coryza': 'Pilek / Hidung Beringus', 'cough': 'Batuk', 'coughing up sputum': 'Batuk Berdahak',
    'abnormal appearing skin': 'Kulit Tampak Tidak Normal', 'allergic reaction': 'Reaksi Alergi',
    'fever': 'Demam', 'high fever': 'Demam Tinggi', 'mild fever': 'Demam Ringan', 'headache': 'Sakit Kepala',
    'nausea': 'Mual', 'vomiting': 'Muntah', 'fatigue': 'Kelelahan / Badan Lemas', 'sweating': 'Berkeringat Berlebih',
    'breathlessness': 'Sesak Napas', 'shortness of breath': 'Napas Pendek', 'acidity': 'Asam Lambung Naik',
    'indigestion': 'Gangguan Pencernaan', 'muscle pain': 'Nyeri Otot', 'joint pain': 'Nyeri Sendi',
    'skin rash': 'Ruam Kulit', 'itching': 'Gatal-gatal', 'nodal skin eruptions': 'Benjolan pada Kulit',
    'continuous sneezing': 'Bersin Terus-menerus', 'shivering': 'Gemetar', 'stomach pain': 'Sakit Perut',
    'chest pain': 'Nyeri Dada', 'loss of appetite': 'Hilang Nafsu Makan', 'phlegm': 'Berdahak',
    'blood in sputum': 'Batuk Berdarah', 'fast heart rate': 'Detak Jantung Cepat', 'pain behind the eyes': 'Nyeri di Belakang Mata',
    'back pain': 'Nyeri Punggung', 'malaise': 'Kurang Enak Badan (Malaise)', 'red spots over body': 'Bintik Merah di Tubuh',
    'dizziness': 'Pusing / Kleyengan', 'weight loss': 'Berat Badan Turun', 'restlessness': 'Gelisah',
    'fluid retention': 'Penumpukan Cairan Tubuh', 'itchiness of eye': 'Mata Terasa Gatal', 'itching of skin': 'Kulit Terasa Gatal',
    'knee lump or mass': 'Benjolan di Lutut', 'lip swelling': 'Bibir Bengkak', 'nasal congestion': 'Hidung Tersumbat',
    'peripheral edema': 'Pembengkakan Kaki/Tangan (Edema)', 'runny nose': 'Hidung Meler', 'sore throat': 'Sakit Tenggorokan',
    'muscle weakness': 'Otot Terasa Lemah', 'stiff neck': 'Leher Kaku', 'swollen lymph nodes': 'Kelenjar Getah Bening Bengkak',
    'blurred and distorted vision': 'Penglihatan Kabur', 'excessive hunger': 'Sering Merasa Lapar',
    'increased appetite': 'Nafsu Makan Meningkat', 'polyuria': 'Sering Buang Air Kecil', 'lethargy': 'Lesu',
    'irregular sugar level': 'Gula Darah Tidak Teratur', 'diarrhoea': 'Diare', 'diarrhea': 'Diare',
    'constipation': 'Sembelit', 'abdominal pain': 'Nyeri Perut', 'yellowing of eyes': 'Mata Menguning',
    'dark urine': 'Urin Berwarna Gelap', 'yellowish skin': 'Kulit Menguning', 'altered sensorium': 'Penurunan Kesadaran',
    'toxic look (typhos)': 'Tampak Pucat Sakit'
}

def translate_gejala(gejala_raw):
    key = gejala_raw.lower().replace("_", " ").strip()
    return TERJEMAHAN_GEJALA.get(key, gejala_raw.replace("_", " ").title())

@st.cache_data
def get_disease_symptoms(csv_path):
    try:
        df = pd.read_csv(csv_path)
        target_col = 'diseases'
        df[target_col] = df[target_col].str.lower().str.strip()
        
        penyakit_target = list(TERJEMAHAN_PENYAKIT.keys())
        df_filtered = df[df[target_col].isin(penyakit_target)]
        
        if df_filtered.empty:
            top_10 = df[target_col].value_counts().nlargest(10).index
            df_filtered = df[df[target_col].isin(top_10)]
            penyakit_target = top_10.tolist()
        
        cf_dataframe = df_filtered.groupby(target_col).mean()
        
        kamus = {}
        for disease, symptoms_row in cf_dataframe.iterrows():
            gejala = []
            for symptom_name, cf_value in symptoms_row.items():
                if cf_value > 0.0:
                    gejala.append(translate_gejala(symptom_name))
            
            nama_tampil = TERJEMAHAN_PENYAKIT.get(disease, disease.title())
            kamus[nama_tampil] = sorted(list(set(gejala))) 
            
        return kamus
    except Exception as e:
        st.error(f"Error memuat data: {e}")
        return {}

st.title("Kamus Penyakit")
st.write("Informasi daftar penyakit dan gejala terkait dalam Bahasa Indonesia.")

kamus_data = get_disease_symptoms('data.zip')

if kamus_data:
    selected_disease = st.selectbox("Pilih Penyakit:", sorted(list(kamus_data.keys())))
    st.divider()
    
    st.subheader(f"Gejala Umum: {selected_disease}")
    gejala_list = kamus_data[selected_disease]
    
    col1, col2 = st.columns(2)
    for i, g in enumerate(gejala_list):
        if i % 2 == 0:
            with col1: st.markdown(f"-{g}")
        else:
            with col2: st.markdown(f"-{g}")
else:
    st.error("Gagal memuat data dari file data.zip")
