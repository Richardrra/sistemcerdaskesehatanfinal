import streamlit as st
from auth_helper import login_form

st.set_page_config(page_title="Login", page_icon="🔑")

# Panggil fungsi login yang sudah kamu buat
if login_form():
    st.success("Anda sudah berhasil login!")
    st.page_link("app.py", label="Kembali ke Beranda")