""", unsafe_allow_html=True)import streamlit as st
import numpy as np

st.set_page_config(page_title="UncertaintyCalc", layout="wide")

# Sidebar Navigation
menu = st.sidebar.radio("📂 Navigasi", [
    "Beranda",
    "Dasar Teori",
    "Kalkulator Ketidakpastian",
    "Cara Perhitungan Manual",
    "Faktor Kesalahan",
    "Contoh Soal dan Pembahasan"
])

# === BERANDA ===
if menu == "Beranda":
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #1f77b4;'>Selamat Datang di <span style='color:#FF4B4B;'>PhyCalc</span>!</h1>
        <h5 style='font-weight: normal;'>Situs untuk belajar dan menghitung <i>nilai ketidakpastian</i> dalam pengukuran ilmiah dan teknis</h3>
    </div>
    """, unsafe_allow_html=True)

    # Slide Gambar
    slides = [
        {
            "path": "https://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2023/08/01/ukuranjpg-20230801094936.jpg",
            "caption": "Nilai Ketidakpastian - Ketelitian adalah segalanya."
        },
        {
            "path": "https://www.kucari.com/wp-content/uploads/2018/09/Alat-Lab.jpg",
            "caption": "Galat Alat - Alat ukur yang tepat menghasilkan data yang bisa dipercaya."
        },
        {
            "path": "https://i.pinimg.com/736x/dd/59/db/dd59dbb6ae1e3415ac2c20d2406b332c.jpg",
            "caption": "Pengulangan - Semakin banyak data, semakin baik ketepatannya."
        }
    ]

    if "slide_index" not in st.session_state:
        st.session_state.slide_index = 0

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.button("⬅️ Sebelumnya", 
                  on_click=lambda: st.session_state.update(slide_index=st.session_state.slide_index - 1),
                  disabled=st.session_state.slide_index == 0)

    with col3:
        st.button("➡️ Selanjutnya", 
                  on_click=lambda: st.session_state.update(slide_index=st.session_state.slide_index + 1),
                  disabled=st.session_state.slide_index == len(slides) - 1)

    current = slides[st.session_state.slide_index]
    st.image(current["path"], caption=current["caption"], use_container_width=True)

    st.markdown(f"<p style='text-align:center; color:gray;'>Slide {st.session_state.slide_index + 1} dari {len(slides)}</p>", unsafe_allow_html=True)

    #isi
    st.markdown("""
 Halo teman-teman semua! disini kami akan membantu kalian memahami dan menghitung nilai ketidakpastian.
Di website ini akan ada beberapa opsi yang bisa kalian buka, yaitu:
    1. Beranda
    2. Dasar Teori
    3. Kalkulator Ketidakpastian
    4. Cara Perhitungan Manual
    5. Faktor Kesalahan
    6. Contoh Soal dan Pembahasan

Ayo mulai belajar sekarang!
""")

    st.header("Pembuat")
    st.markdown("""
Kelompok 3
    Anggota:
            1. 
            2. 
            3. 
            4. 
            5.

    # Footer ringan
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>POLITEKNIK AKA BOGOR - 2025</p>", unsafe_allow_html=True)
