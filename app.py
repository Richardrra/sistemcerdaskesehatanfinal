import streamlit as st
import base64
import os

st.set_page_config(
    page_title="HealthTech CF",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background-color: #f0f4ff;
        font-family: 'Poppins', sans-serif;
    }

    /* === SIDEBAR TOGGLE === */
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

    /* === LOGO === */
    .logo-text {
        color: #7c3aed;
        font-weight: 700;
        font-family: 'Comfortaa', cursive;
        font-size: 17px;
        letter-spacing: 0.5px;
        padding: 8px 0;
    }

    /* === NAV BUTTONS === */
    a[data-testid="stPageLink-NavLink"] {
        background: linear-gradient(135deg, #7c3aed, #BC84EE) !important;
        color: white !important;
        border-radius: 30px !important;
        padding: 8px 20px !important;
        font-weight: 600 !important;
        font-size: 13px !important;
        text-decoration: none !important;
        display: inline-block !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 14px rgba(124,58,237,0.3) !important;
        border: none !important;
        white-space: nowrap !important;
    }
    a[data-testid="stPageLink-NavLink"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 20px rgba(124,58,237,0.45) !important;
    }

    /* === HERO BANNER === */
    .hero-banner {
        background: linear-gradient(135deg, #7c3aed 0%, #BC84EE 60%, #c4b5fd 100%);
        border-radius: 28px;
        padding: 60px 55px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: white;
        margin-bottom: 45px;
        box-shadow: 0 25px 50px rgba(124,58,237,0.25);
        position: relative;
        overflow: hidden;
    }
    .hero-banner::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 250px; height: 250px;
        border-radius: 50%;
        background: rgba(255,255,255,0.08);
    }
    .hero-banner::after {
        content: '';
        position: absolute;
        bottom: -80px; left: 30%;
        width: 200px; height: 200px;
        border-radius: 50%;
        background: rgba(255,255,255,0.05);
    }
    .hero-text h1 {
        font-family: 'Comfortaa', cursive;
        font-size: 3.2rem;
        font-weight: 700;
        margin-bottom: 18px;
        line-height: 1.15;
        color: white;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        border: 1px solid rgba(255,255,255,0.35);
        color: white;
        font-size: 12px;
        font-weight: 600;
        padding: 5px 14px;
        border-radius: 20px;
        margin-bottom: 18px;
        backdrop-filter: blur(6px);
        letter-spacing: 0.5px;
    }
    .hero-text p {
        font-size: 1.05rem;
        opacity: 0.92;
        font-weight: 300;
        line-height: 1.7;
    }
    .hero-img {
        max-width: 260px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.25);
    }

    /* === STATS BAR === */
    .stats-bar {
        display: flex;
        gap: 20px;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }
    .stat-item {
        background: white;
        border-radius: 18px;
        padding: 20px 28px;
        flex: 1;
        min-width: 140px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.04);
        border: 1.5px solid #e8e0f7;
        text-align: center;
        transition: transform 0.2s ease;
    }
    .stat-item:hover { transform: translateY(-4px); }
    .stat-num {
        font-size: 2rem;
        font-weight: 700;
        color: #7c3aed;
        font-family: 'Comfortaa', cursive;
        line-height: 1;
        margin-bottom: 5px;
    }
    .stat-label {
        font-size: 12px;
        color: #9ca3af;
        font-weight: 500;
        font-family: 'Poppins', sans-serif;
    }

    /* === CLICKABLE CARD WRAPPER === */
    /* Container kolom yang berisi card + page_link */
    .card-col-wrapper {
        position: relative;
    }

    /* Sembunyikan teks default page_link, jadikan full-area overlay */
    .card-col-wrapper a[data-testid="stPageLink-NavLink"] {
        position: absolute !important;
        inset: 0 !important;
        background: transparent !important;
        box-shadow: none !important;
        border-radius: 22px !important;
        padding: 0 !important;
        font-size: 0 !important;      /* sembunyikan teks label */
        color: transparent !important;
        z-index: 10 !important;
        display: block !important;
        width: 100% !important;
        height: 100% !important;
    }
    .card-col-wrapper a[data-testid="stPageLink-NavLink"]:hover ~ .service-card,
    .card-col-wrapper:hover .service-card {
        transform: translateY(-7px);
        box-shadow: 0 20px 45px rgba(124,58,237,0.15);
        border-color: #a78bfa;
    }

    /* === SERVICE CARD === */
    .service-card {
        background: white;
        border-radius: 22px;
        padding: 30px 28px 26px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border: 1.5px solid #e8e0f7;
        border-top: 5px solid transparent;
        background-clip: padding-box;
        transition: all 0.3s cubic-bezier(0.25,0.8,0.25,1);
        position: relative;
        cursor: pointer;
    }
    .service-card::before {
        content: '';
        position: absolute;
        top: -1.5px; left: -1.5px; right: -1.5px;
        height: 6px;
        background: linear-gradient(90deg, #7c3aed, #BC84EE);
        border-radius: 22px 22px 0 0;
    }
    /* Panah kecil pojok kanan bawah sebagai hint klikable */
    .service-card .card-arrow {
        position: absolute;
        bottom: 20px; right: 22px;
        width: 30px; height: 30px;
        background: linear-gradient(135deg, #ede9fe, #ddd6fe);
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 13px;
        transition: all 0.25s ease;
        color: #7c3aed;
    }
    .service-card:hover .card-arrow {
        background: linear-gradient(135deg, #7c3aed, #BC84EE);
        color: white;
        transform: translate(2px, -2px);
    }

    .card-number {
        font-size: 11px;
        font-weight: 700;
        color: #BC84EE;
        letter-spacing: 1.5px;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 10px;
        text-transform: uppercase;
    }
    .card-title {
        color: #1e1b4b;
        font-weight: 700;
        font-size: 18px;
        margin-bottom: 10px;
        font-family: 'Comfortaa', cursive;
        line-height: 1.3;
    }
    .card-desc {
        color: #6b7280;
        font-size: 13px;
        margin-bottom: 30px;
        line-height: 1.65;
        font-family: 'Poppins', sans-serif;
    }
    .card-status {
        display: inline-block;
        background: linear-gradient(135deg, #f3e8ff, #ede9fe);
        color: #7c3aed;
        font-size: 12px;
        font-weight: 600;
        padding: 6px 14px;
        border-radius: 20px;
        font-family: 'Poppins', sans-serif;
        border: 1px solid #ddd6fe;
        margin-bottom: 30px;
    }

    /* === SECTION TITLE === */
    .section-title {
        color: #1e1b4b;
        font-weight: 700;
        font-family: 'Comfortaa', cursive;
        font-size: 1.6rem;
        margin-bottom: 4px;
    }
    .section-sub {
        color: #6b7280;
        font-size: 14px;
        margin-bottom: 28px;
    }

    hr { border: none; border-top: 1.5px solid #e8e0f7; margin: 30px 0; }

    /* Hapus padding default container streamlit agar posisi absolut presisi */
    div[data-testid="stColumn"] > div {
        position: relative;
    }
</style>
""", unsafe_allow_html=True)


def clickable_card(col, number, title, desc, page, status_badge=None):
    with col:
        st.markdown(f"""
        <div class="service-card">
            <div class="card-number">{number}</div>
            <div class="card-title">{title}</div>
            <div class="card-desc">{desc}</div>
            {"<div class='card-status'>✓ Terkonfigurasi Aktif</div>" if status_badge else ""}
            
        </div>
        """, unsafe_allow_html=True)
        
        st.page_link(page, label=title)


nav_col1, nav_col2 = st.columns([1, 2])
with nav_col1:
    st.markdown('<div class="logo-text">Deteksi Penyakit Berbasis Certainty Factor</div>', unsafe_allow_html=True)
with nav_col2:
    cols = st.columns(5)
    with cols[0]: st.page_link("pages/Diagnosa.py", label="Diagnosa")
    with cols[1]: st.page_link("pages/Kamus_Penyakit.py", label="Kamus")
    with cols[2]: st.page_link("pages/Analisis_Dataset.py", label="Analisis")
    with cols[3]: st.page_link("pages/Riwayat_Diagnosa.py", label="Riwayat")
    
    with cols[4]:
        # Logika: Jika sudah login, tampilkan tombol Logout. Jika belum, tampilkan Login.
        if st.session_state.get('logged_in', False):
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()
        else:
            st.page_link("pages/Login.py", label="Login")


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f: data = f.read()
    return base64.b64encode(data).decode()

image_path = "assets/logosistempakar.png"
if os.path.exists(image_path):
    img_b64 = get_base64_of_bin_file(image_path)
    img_tag  = f'<img class="hero-img" src="data:image/png;base64,{img_b64}" alt="LOGO">'
else:
    img_tag = '<div style="font-size:110px;text-align:center;line-height:1;">🩺</div>'

st.markdown(f"""
<div class="hero-banner">
    <div class="hero-text">
        <div class="hero-badge">✦ Berbasis Certainty Factor Algorithm</div>
        <h1>Diagnosa<br>Lebih Cerdas.</h1>
        <p>Sistem pakar medis untuk menganalisis gejala penyakit tropis<br>
        Indonesia dengan akurasi tinggi dan visualisasi profesional.</p>
    </div>
    <div style="position:relative;z-index:1;">{img_tag}</div>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="stats-bar">
    <div class="stat-item"><div class="stat-num">10</div><div class="stat-label">Penyakit Target</div></div>
    <div class="stat-item"><div class="stat-num">CF</div><div class="stat-label">Algoritma Utama</div></div>
    <div class="stat-item"><div class="stat-num">50+</div><div class="stat-label">Gejala Terdaftar</div></div>
    <div class="stat-item"><div class="stat-num">5</div><div class="stat-label">Modul Sistem</div></div>
</div>
""", unsafe_allow_html=True)


st.markdown("<div class='section-title'>Layanan Sistem</div>", unsafe_allow_html=True)
st.markdown("<div class='section-sub'>Klik card untuk membuka modul</div>", unsafe_allow_html=True)

row1 = st.columns(3)
clickable_card(row1[0], "Modul 01", "Mulai Diagnosa",
    "Deteksi penyakit berdasarkan perhitungan Certainty Factor dari gejala yang Anda rasakan.",
    "pages/Diagnosa.py")
clickable_card(row1[1], "Modul 02", "Basis Pengetahuan",
    "Eksplorasi kamus medis dan daftar gejala lengkap dari 10 penyakit tropis target.",
    "pages/Kamus_Penyakit.py")
clickable_card(row1[2], "Modul 03", "Analisis Dataset",
    "Visualisasi dan transparansi data latih yang digunakan oleh sistem.",
    "pages/Analisis_Dataset.py")

st.write("")

row2 = st.columns(3)
clickable_card(row2[0], "Modul 04", "Riwayat Pasien",
    "Rekam medis hasil diagnosa sementara selama sesi aplikasi ini berjalan aktif.",
    "pages/Riwayat_Diagnosa.py")
clickable_card(row2[1], "Modul 05", "Metodologi CF",
    "Pelajari cara algoritma Certainty Factor bekerja dan profil tim pengembang sistem.",
    "pages/Tentang_Sistem.py")
clickable_card(row2[2], "Modul 06", "Tentang Sistem",
    "Sistem dikalibrasi khusus untuk 10 penyakit tropis Indonesia yang paling umum.",
    "pages/Tentang_Sistem.py",
    status_badge=True)

if 'history' not in st.session_state:
    st.session_state['history'] = []