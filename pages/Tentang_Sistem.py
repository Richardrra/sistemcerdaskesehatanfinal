import streamlit as st

st.set_page_config(page_title="Tentang Sistem", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background-color: #f0f4ff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Paksa konten rata kiri, hapus max-width bawaan Streamlit */
    .block-container {
        max-width: 100% !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
        padding-top: 2rem !important;
    }

    [data-testid="stSidebarCollapsedControl"] {
        background-color: #BC84EE !important;
        border-radius: 12px !important;
        padding: 6px !important;
        box-shadow: 0 4px 14px rgba(188,132,238,0.5) !important;
    }
    [data-testid="stSidebarCollapsedControl"] svg {
        fill: white !important;
        color: white !important;
    }

    header[data-testid="stHeader"] { background-color: transparent; }

    /* === PAGE TITLE === */
    .page-title {
        font-family: 'Comfortaa', cursive;
        font-size: 2.2rem;
        font-weight: 700;
        color: #1e1b4b;
        margin-bottom: 6px;
    }
    .page-subtitle {
        color: #6b7280;
        font-size: 14px;
        margin-bottom: 36px;
        font-family: 'Poppins', sans-serif;
    }

    /* === SECTION CARD === */
    .info-card {
        background: white;
        border-radius: 20px;
        padding: 32px 36px;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        border: 1.5px solid #e8e0f7;
        border-left: 5px solid #BC84EE;
    }
    .info-card h3 {
        font-family: 'Comfortaa', cursive;
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e1b4b;
        margin-bottom: 14px;
    }
    .info-card p, .info-card li {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #4b5563;
        line-height: 1.75;
    }
    .info-card ul {
        padding-left: 20px;
        margin: 10px 0;
    }

    /* === CF FORMULA BOX === */
    .formula-box {
        background: linear-gradient(135deg, #ede9fe, #f3e8ff);
        border: 1.5px solid #c4b5fd;
        border-radius: 12px;
        padding: 14px 20px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        color: #5b21b6;
        font-weight: 600;
        margin-top: 14px;
        display: inline-block;
    }

    /* === SKALA TABLE === */
    .skala-grid {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 12px;
    }
    .skala-item {
        background: linear-gradient(135deg, #f3e8ff, #ede9fe);
        border: 1px solid #ddd6fe;
        border-radius: 10px;
        padding: 10px 18px;
        text-align: center;
        flex: 1;
        min-width: 100px;
    }
    .skala-val {
        font-family: 'Comfortaa', cursive;
        font-size: 1.3rem;
        font-weight: 700;
        color: #7c3aed;
    }
    .skala-lbl {
        font-size: 11px;
        color: #6b7280;
        font-family: 'Poppins', sans-serif;
        margin-top: 3px;
    }

    /* === DEV CARD === */
    .dev-row {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 10px;
    }
    .dev-icon {
        width: 42px; height: 42px;
        border-radius: 50%;
        background: linear-gradient(135deg, #7c3aed, #BC84EE);
        display: flex; align-items: center; justify-content: center;
        font-size: 18px;
        flex-shrink: 0;
    }
    .dev-info strong {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #1e1b4b;
    }
    .dev-info span {
        font-size: 13px;
        color: #6b7280;
        display: block;
    }

    /* === BADGE === */
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, #7c3aed, #BC84EE);
        color: white;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 20px;
        font-family: 'Poppins', sans-serif;
        margin-right: 8px;
        margin-bottom: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ──────────────────────────────────────────────────
st.markdown('<div class="page-title">Tentang Sistem & Metodologi</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Informasi lengkap tentang sistem, algoritma, dan pengembang</div>', unsafe_allow_html=True)

# ── LAYOUT 2 KOLOM ──────────────────────────────────────────
left, right = st.columns([3, 2], gap="large")

with left:
    # Profil Sistem
    st.markdown("""
    <div class="info-card">
        <h3>Profil Sistem</h3>
        <p>Aplikasi website cerdas ini dibangun sebagai pemenuhan tugas mata kuliah 
        <strong>Sistem Pakar / Sistem Cerdas</strong>. Antarmuka sistem dibangun sepenuhnya 
        menggunakan <strong>Python</strong> dan pustaka <strong>Streamlit</strong>.</p>
        <br>
        <span class="badge">Python</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Pandas</span>
        <span class="badge">Certainty Factor</span>
    </div>
    """, unsafe_allow_html=True)

    # Metodologi CF
    st.markdown("""
    <div class="info-card">
        <h3>Metodologi: Certainty Factor (CF)</h3>
        <p>Sistem ini menggunakan algoritma <strong>Certainty Factor</strong> untuk menangani 
        ketidakpastian dalam mendiagnosa penyakit.</p>
        <br>
        <p><strong>Terdapat dua parameter utama:</strong></p>
        <ul>
            <li><strong>CF Pakar (Measure of Belief):</strong> Didapatkan dari ekstraksi otomatis 
            dataset berdasarkan frekuensi munculnya nilai 1 pada suatu gejala untuk penyakit tertentu.</li>
            <li><strong>CF Pengguna:</strong> Didapatkan dari input user melalui sistem skala keyakinan.</li>
        </ul>
        <br>
        <p><strong>Rumus Kombinasi</strong> (ketika lebih dari 1 gejala dipilih):</p>
        <div class="formula-box">
            CF_gabungan = CF_lama + CF_gejala_baru × (1 − CF_lama)
        </div>
    </div>
    """, unsafe_allow_html=True)

   
    st.markdown("""
    <div class="info-card">
        <h3>Sumber Dataset</h3>
        <p>Dataset diambil dari Kaggle(Symptoms to Diseases). 
        Untuk mengoptimalkan performa, data awal telah disaring sehingga 
        hanya mencakup 10 jenis penyakit tropis teratas beserta gejala-gejalanya.
        Link dataset : https://www.kaggle.com/datasets/abhishekgodara/symptoms-to-diseases/data</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    
    st.markdown("""
    <div class="info-card">
        <h3>Skala Keyakinan Pengguna</h3>
        <p>Input user menggunakan 5 tingkat keyakinan:</p>
        <div class="skala-grid">
            <div class="skala-item"><div class="skala-val">1.0</div><div class="skala-lbl">Sangat Yakin</div></div>
            <div class="skala-item"><div class="skala-val">0.8</div><div class="skala-lbl">Yakin</div></div>
            <div class="skala-item"><div class="skala-val">0.6</div><div class="skala-lbl">Cukup Yakin</div></div>
            <div class="skala-item"><div class="skala-val">0.4</div><div class="skala-lbl">Sedikit Yakin</div></div>
            <div class="skala-item"><div class="skala-val">0.2</div><div class="skala-lbl">Tidak Yakin</div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div class="info-card">
        <h3>Pengembang</h3>
        <div class="dev-row">
            <div class="dev-icon"></div>
            <div class="dev-info">
                <strong>Richard Ricco A & Tyo Fajar S</strong>
                <span>Mahasiswa Informatika</span>
            </div>
        </div>
        <br>
        <div class="dev-row">
            <div class="dev-icon"></div>
            <div class="dev-info">
                <strong>Platform</strong>
                <span>Streamlit Cloud</span>
            </div>
        </div>
        <br>
        <div class="dev-row">
            <div class="dev-icon"></div>
            <div class="dev-info">
                <strong>Bahasa Pemrograman</strong>
                <span>Python (Pandas, Streamlit)</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Target Penyakit
    st.markdown("""
    <div class="info-card">
        <h3>10 Penyakit Target</h3>
        <p>Sistem dikalibrasi khusus untuk penyakit tropis Indonesia yang paling umum ditemukan.</p>
        <br>
        <span class="badge">Diabetes</span>
        <span class="badge">Hipertensi</span>
        <span class="badge">Malaria</span>
        <span class="badge">Tifus</span>
        <span class="badge">DBD</span>
        <span class="badge">TBC</span>
        <span class="badge">Pneumonia</span>
        <span class="badge">Hepatitis</span>
        <span class="badge">Asma</span>
        <span class="badge">Diare</span>
    </div>
    """, unsafe_allow_html=True)
