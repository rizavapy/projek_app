import streamlit as st
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
        <h5 style='font-weight: normal;'>Situs untuk belajar dan menghitung <i>nilai ketidakpastian</i> dalam pengukuran ilmiah dan teknis 📏🧪</h5>
    </div>
    """, unsafe_allow_html=True)

    # Slide Gambar
    slides = [
        {
            "path": "https://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2023/08/01/ukuranjpg-20230801094936.jpg",
            "caption": "🔍 Nilai Ketidakpastian - Ketelitian adalah segalanya."
        },
        {
            "path": "https://www.kucari.com/wp-content/uploads/2018/09/Alat-Lab.jpg",
            "caption": "🧪 Galat Alat - Alat ukur yang tepat menghasilkan data yang bisa dipercaya."
        },
        {
            "path": "https://i.pinimg.com/736x/dd/59/db/dd59dbb6ae1e3415ac2c20d2406b332c.jpg",
            "caption": "🔁 Pengulangan - Semakin banyak data, semakin baik ketepatannya."
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

    # Deskripsi Isi Halaman
    st.markdown("""
    <hr>
    <div style='font-size:16px; text-align:justify'>
        <p>Halo teman-teman semua! 👋</p>
        <p>Di sini kami akan membantu kalian memahami dan menghitung nilai ketidakpastian secara mudah dan menyenangkan.</p>
        <p>Kalian bisa menjelajahi berbagai fitur melalui menu di sebelah kiri:</p>
        <ul>
            <li>📌 Beranda</li>
            <li>📚 Dasar Teori</li>
            <li>📊 Kalkulator Ketidakpastian</li>
            <li>📝 Cara Perhitungan Manual</li>
            <li>⚠️ Faktor Kesalahan</li>
            <li>🧠 Contoh Soal dan Pembahasan</li>
        </ul>
        <p>Yuk mulai belajar sekarang! 💪</p>
    </div>
    """, unsafe_allow_html=True)

    
    # Daftar Kelompok
    st.markdown("### 👨‍🔬 Pembuat Aplikasi - Kelompok 3")
    st.markdown("""
    **Anggota:**
    1. Aditya Dwika Iannanda         - 2460308
    2. Dhe Adila Zahra Tubarila      - 2460354
    3. Laila Najwa                   - 2460405
    4. Naura Amalia Shaliha          - 2460461
    5. Rizava Apriza                 - 2460503
    """)

    # Footer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>© 2025 POLITEKNIK AKA BOGOR - All rights reserved.</p>", unsafe_allow_html=True)

# ===== DASAR TEORI =====


# ===== KALKULATOR KETIDAKPASTIAN =====
elif menu == "Kalkulator Ketidakpastian":
    st.title("📊 Kalkulator Ketidakpastian Tipe A dan Tipe B")

    st.markdown("""
    Masukkan data pengukuranmu, dan kalkulator ini akan secara otomatis menghitung:
    
    - Ketidakpastian Tipe A (berdasarkan statistik pengukuran berulang)
    - Ketidakpastian Tipe B (berdasarkan resolusi alat)
    - Ketidakpastian Gabungan
    - Hasil akhir dalam format: **x̄ ± u<sub>c</sub>**
    - Persentase ketidakpastian terhadap nilai rata-rata
    """, unsafe_allow_html=True)

    # Input data
    data_input = st.text_area("📥 Masukkan data pengukuran (pisahkan dengan koma)", "10.1, 10.3, 10.2, 10.4, 10.2")
    resolusi = st.number_input("📏 Masukkan nilai resolusi alat ukur", value=0.01, step=0.001)

    if st.button("Hitung Ketidakpastian"):
        try:
            # Olah data
            data = np.array([float(x.strip()) for x in data_input.split(",") if x.strip() != ""])
            n = len(data)

            if n < 2:
                st.error("Minimal masukkan 2 data pengukuran untuk perhitungan Tipe A.")
            else:
                rata2 = np.mean(data)
                std_dev = np.std(data, ddof=1)
                ua = std_dev / np.sqrt(n)  # Ketidakpastian Tipe A
                ub = resolusi / np.sqrt(3)  # Ketidakpastian Tipe B
                uc = np.sqrt(ua**2 + ub**2)  # Ketidakpastian Gabungan
                persen = (uc / rata2) * 100  # Persentase ketidakpastian

                # Hasil
                st.markdown("---")
                st.subheader("📈 Hasil Perhitungan:")
                st.success(f"Rata-rata (x̄): {rata2:.4f}")
                st.success(f"Simpangan baku (s): {std_dev:.4f}")
                st.info(f"Ketidakpastian Tipe A (uₐ): {ua:.4f}")
                st.info(f"Ketidakpastian Tipe B (uᵦ): {ub:.4f}")
                st.warning(f"Ketidakpastian Gabungan (u꜀): {uc:.4f}")
                st.markdown(f"### ✅ Hasil Akhir: **{rata2:.4f} ± {uc:.4f}**")
                st.markdown(f"📌 Persentase ketidakpastian terhadap rata-rata: **{persen:.2f}%**")

                # Interpretasi
                if persen < 1:
                    st.success("🎯 Akurasi tinggi (ketidakpastian < 1%)")
                elif persen < 5:
                    st.info("✔️ Akurasi sedang (ketidakpastian antara 1%-5%)")
                else:
                    st.warning("⚠️ Akurasi rendah (ketidakpastian > 5%). Perlu dicek ulang alat/data.")

        except:
            st.error("❌ Format input tidak valid. Pastikan hanya angka dan dipisahkan koma.")

    # ===== CARA PERHITUNGAN MANUAL =====
elif menu == "Cara Perhitungan Manual":
    st. title("Cara Hitung dengan Rumus dan Kalkulator scientific unch 👉🏻👈🏻🥺")
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #1f77b4;'>Perhitungan dengan cara <span style='color:#FF4B4B;'>Manual</span>!</h1>
        <h5 style='font-weight: normal;'>Berhitung dengan<i>manual</i>atau dengan menggunakan<i>kalkulator scientific</i>/h5>
    </div>
    """, unsafe_allow_html=True)

