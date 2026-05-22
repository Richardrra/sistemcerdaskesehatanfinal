import streamlit as st

def login_form():

    st.markdown("""
    <style>
        .login-card {
            background-color: white;
            padding: 40px;
            border-radius: 24px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            border: 1px solid #f1f5f9;
            text-align: center;
        }
        .login-title {
            font-family: 'Comfortaa', cursive;
            color: #1e293b;
            font-size: 28px;
            margin-bottom: 10px;
        }
        .login-desc {
            color: #64748b;
            font-family: 'Poppins', sans-serif;
            margin-bottom: 30px;
        }
        /* Styling tombol login agar warna senada */
        div.stButton > button {
            background-color: #BC84EE !important;
            color: white !important;
            border-radius: 30px !important;
            width: 100%;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("<h3 class='login-title'>Login Sistem</h3>", unsafe_allow_html=True)
            st.markdown("<p class='login-desc'>Login untuk menggunakan sistem cerdas kesehatan.</p>", unsafe_allow_html=True)
            
            with st.form("login_form"):
                user = st.text_input("Username")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Masuk Sekarang")
                
                if submit:
                    if user == "admin" and password == "admin123":
                        st.session_state.logged_in = True
                        st.rerun()
                    else:
                        st.error("Username atau Password salah!")
            st.markdown("</div>", unsafe_allow_html=True)
        
        return False
    return True

def logout_button():
    """Tombol logout di sidebar"""
    if st.sidebar.button("Keluar dari Sistem"):
        st.session_state.logged_in = False
        st.rerun()