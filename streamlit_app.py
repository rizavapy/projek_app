import streamlit as st
import numpy as np

st.set_page_config(page_title="Chemcalc", layout="wide")

# Sidebar Navigation
menu = st.sidebar.radio("Navigasi", [
    "Beranda",
    "Dasar Teori",
    "Kalkulator Ketidakpastian",
    "Cara Perhitungan Manual",
    "Faktor Kesalahan",
    "Contoh Soal dan Pembahasan"
])

# === BERANDA ===
if menu == "Beranda":
   st.markdown("""
    <div style="text-align:center">
        <h1>🎉 Selamat Datang di <span style='color:#1f77b4;'>UncertaintyCalc</span></h1>
    st.write("Situs web interaktif untuk memahami dan menghitung nilai ketidakpastian dalam pengukuran ilmiah dan teknis.")

    # List gambar
    slides = [
        {"path": "https://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2023/08/01/ukuranjpg-20230801094936.jpg", "caption": "Nilai Ketidakpastian"},
        {"path": "https://1.bp.blogspot.com/-Tb1wYeCR7yM/WYNuEPz-DDI/AAAAAAAAVSc/fvi7otqPr2kfr2Tr_9kR6UO0pAuPQLU_gCLcBGAs/s1600/Peralatan%2BGelas.jpg", "caption": "Galat Alat"},
        {"path": "https://i.pinimg.com/736x/dd/59/db/dd59dbb6ae1e3415ac2c20d2406b332c.jpg", "caption": "Pengulangan"}
    ]

    # Simpan indeks saat ini di session_state
    if "slide_index" not in st.session_state:
        st.session_state.slide_index = 0

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        if st.button("⬅️ Sebelumnya") and st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1

    with col3:
        if st.button("➡️ Selanjutnya") and st.session_state.slide_index < len(slides) - 1:
            st.session_state.slide_index += 1

    # Tampilkan gambar berdasarkan index
    current = slides[st.session_state.slide_index]
    st.image(current["path"], caption=current["caption"], use_container_width=True)

    # Indikator slide
    st.markdown(f"<p style='text-align:center;'>Slide {st.session_state.slide_index + 1} dari {len(slides)}</p>", unsafe_allow_html=True)

    st.markdown("""
    Situs web interaktif untuk memahami dan menghitung nilai ketidakpastian dalam pengukuran ilmiah dan teknis.

    **Apa Itu Nilai Ketidakpastian?**  
    Dalam setiap pengukuran, selalu ada kemungkinan kesalahan atau deviasi dari nilai sebenarnya.  
    Nilai ketidakpastian membantu kita mengetahui seberapa akurat hasil pengukuran kita.

    Gunakan menu di sebelah kiri untuk mulai belajar atau menghitung!
    """)

# === DASAR TEORI ===

# === KALKULATOR TIPE A & B ===

# === PERHITUNGAN MANUAL ===


# === FAKTOR KESALAHAN ===

