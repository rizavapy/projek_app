import streamlit as st
import numpy as np
import pandas as pd

# ====== CUSTOM BACKGROUND & SIDEBAR ======
st.markdown("""
    <style>
    /* Background halaman utama */
    .stApp {
        background: url('data:image/jpeg;base64,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'):
        background-position: center;
        background-attachment: fixed;
    }

    /* Warna background sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1f77b4 !important;
    }

    /* Warna teks sidebar agar kontras */
    section[data-testid="stSidebar"] .css-1v3fvcr, 
    section[data-testid="stSidebar"] .css-1d391kg,
    section[data-testid="stSidebar"] .st-emotion-cache-1avcm0n,
    section[data-testid="stSidebar"] .st-emotion-cache-1n76uvr {
        color: white !important;
    }

    /* Konten utama transparan */
    .st-emotion-cache-1kyxreq, .st-emotion-cache-10trblm {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

    # Sidebar Navigation
menu = st.sidebar.radio("📂 Navigasi", [
    "Beranda",
    "Dasar Teori",
    "Kalkulator Ketidakpastian",
    "Cara Perhitungan Manual",
    "Faktor Kesalahan",
    "Contoh Soal"
])

# === BERANDA ===
if menu == "Beranda":
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #1f77b4;'>Selamat Datang di <span style='color:#32cd32;'>PhyCalc</span>!</h1>
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
elif menu == "Dasar Teori":
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #1f77b4;'>Konsep <span style='color:#add8e6;'>Perhitungan </span>!</h1>
        <h5 style='font-weight: normal;'>Sebelum menggunakan <i> Phycalc </i> kamu perlu memahami konsep mengenai perhitungan, terutama tentang galat </h5>
    </div> 
    
<p>Proses pembelajaran fisika tidak hanya menekankan penguasaan konsep, tetapi juga keterampilan proses sains yang harus dimiliki siswa, salah satunya adalah kemampuan menaksir ukuran besaran fisika. Kemampuan ini memiliki peranan penting dalam kehidupan, terutama pada besaran-besaran yang kerap digunakan, seperti panjang, massa, dan waktu. Kemampuan ini sangat dibutuhkan dalam berbagai bidang. Namun, belum banyak peneliti yang mengkaji kemampuan ini. Oleh karena itu, diperlukan analisis kemampuan siswa dalam menaksir ukuran besaran fisika. Penelitian ini bertujuan untuk menganalisis kemampuan siswa dalam menaksir ukuran besaran fisika, mengetahui perbedaan kemampuan menaksir ukuran antara siswa laki-laki dan perempuan, mengetahui besaran yang paling mudah dan paling sulit ditaksir, serta mengetahui acuan yang digunakan siswa dalam menaksir ukuran. <strong>(HARTANTI & HARTANTI, 2024)</strong></p>

<li><b>Galat (kesalahan) pengukuran</b><br>
perbedaan antara nilai yang diukur dengan nilai sebenarnya dari suatu besaran.</li><br>
    
<li><b>Galat Sistematis</b><br> 
Galat yang cenderung tetap dan dapat diprediksi, disebabkan oleh kesalahan pada alat ukur atau metode pengukuran. Contohnya, kesalahan kalibrasi atau titik nol pada alat ukur.</li><br>
    
<li><b>Galat Acak</b><br>
Galat yang tidak dapat diprediksi dan bervariasi secara acak, disebabkan oleh faktor-faktor yang tidak terkontrol seperti fluktuasi lingkungan atau kesalahan pengamat.</li><br>   

<li><b>Galat Umum (Kekeliruan)</b><br>
Galat yang disebabkan oleh kesalahan manusia, seperti kesalahan membaca skala atau kesalahan dalam mencatat hasil.</li><br>
    
<li><b>Galat Absolut</b><br>
Selisih antara nilai terukur dengan nilai sebenarnya.</li><br>
    
<li><b>Galat Relatif</b><br>
Galat absolut dibagi dengan nilai sebenarnya, sering dinyatakan dalam persen.</li><br>
    
<li><b>Distribusi Galat</b><br>
Pengukuran berulang dapat menghasilkan distribusi galat yang dapat dianalisis secara statistik untuk mendapatkan informasi tentang keakuratan dan presisi pengukuran.</li><br>
    """, unsafe_allow_html=True)



# ===== KALKULATOR KETIDAKPASTIAN =====
elif menu == "Kalkulator Ketidakpastian":
    
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #ff8f00;'>Kalkulator <span style='color:#000000;'>Ketidakpastian 📊 </span>!</h1>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #a40000 ;'>Perhitungan cara <span style='color:#00b7eb;'>Manual 📝</span>!</h1>
        <h5 style='font-weight: normal;'>Berhitung dengan <i>manual </i>atau dengan menggunakan <i>kalkulator scientific</i></h5>
    </div>
    """, unsafe_allow_html=True)
    
    #Isi cara secara manual
    st.markdown("""
    <h3 style='font-weight: normal;'>Menggunakan <i>Rumus </i> Secara Mandiri 📝</h3>
    </div>
     """, unsafe_allow_html=True)
    
    with st.expander("1. Hitung Rata-Rata Pengukuran"):
        st.latex(r"\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i")

    with st.expander("2. Hitung Simpangan Baku"):
        st.latex(r"s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}")

    with st.expander("3. Hitung Ketidakpastian Tipe A (uₐ)"):
        st.latex(r"u_a = \frac{s}{\sqrt{n}}")

    with st.expander("4. Hitung Ketidakpastian Tipe B (uᵦ)"):
        st.latex(r"u_b = \frac{\text{resolusi}}{\sqrt{3}}")

    with st.expander("5. Hitung Ketidakpastian Gabungan (u꜀)"):
        st.latex(r"u_c = \sqrt{u_a^2 + u_b^2}")

    with st.expander("6. Tulis Hasil Pengukuran"):
        st.latex(r"x = \bar{x} \pm u_c")
        st.latex(r"\text{Persentase} = \frac{u_c}{\bar{x}} \times 100\%")

        st.success("🎉 Semua langkah sudah dijelaskan. Silakan buka satu per satu untuk belajar mandiri ya!")

  #Isi cara secara kalkulator scientific
    st.markdown("""
    <h3 style='font-weight: normal;'>Melihat cara kerja <i>kalkulator scientific </i> 📝</h3>
    </div>
        """, unsafe_allow_html=True)
    
# --- STEP 1: Input Data dan Hitung Rata-Rata ---
    with st.expander("1️⃣ Hitung Rata-Rata dan Simpangan Baku"):
        data_input = st.text_area("📥 Masukkan data pengukuran (dipisah koma)", "10.1, 10.3, 10.2, 10.4, 10.2")
        if st.button("🔢 Hitung Rata-Rata & Simpangan Baku"):
            try:
                data = np.array([float(i.strip()) for i in data_input.split(",") if i.strip() != ""])
                n = len(data)
                if n < 2:
                    st.error("❌ Minimal 2 data diperlukan.")
                else:
                    rata2 = np.mean(data)
                    std_dev = np.std(data, ddof=1)
                    st.latex(r"\bar{x} = \frac{1}{n} \sum x_i = %.4f" % rata2)
                    st.latex(r"s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}} = %.4f" % std_dev)
                    st.success(f"✔️ Rata-rata: {rata2:.4f} | Simpangan baku: {std_dev:.4f}")
            except:
                st.error("❌ Format data tidak valid.")

    # --- STEP 2: Ketidakpastian Tipe A ---
    with st.expander("2️⃣ Hitung Ketidakpastian Tipe A (uₐ)"):
        std_input = st.number_input("📥 Masukkan simpangan baku (s)", value=0.1, step=0.001)
        n_input = st.number_input("🧮 Masukkan jumlah data (n)", value=5, step=1)
        if st.button("📊 Hitung uₐ"):
            try:
                ua = std_input / np.sqrt(n_input)
                st.latex(r"u_a = \frac{s}{\sqrt{n}} = \frac{%.4f}{\sqrt{%d}} = %.4f" % (std_input, n_input, ua))
                st.success(f"Ketidakpastian Tipe A (uₐ): {ua:.4f}")
            except:
                st.error("❌ Masukkan nilai valid.")

    # --- STEP 3: Ketidakpastian Tipe B ---
    with st.expander("3️⃣ Hitung Ketidakpastian Tipe B (uᵦ)"):
        resolusi = st.number_input("📏 Masukkan resolusi alat ukur", value=0.01, step=0.001)
        if st.button("📐 Hitung uᵦ"):
            ub = resolusi / np.sqrt(3)
            st.latex(r"u_b = \frac{%.4f}{\sqrt{3}} = %.4f" % (resolusi, ub))
            st.success(f"Ketidakpastian Tipe B (uᵦ): {ub:.4f}")

    # --- STEP 4: Ketidakpastian Gabungan ---
    with st.expander("4️⃣ Hitung Ketidakpastian Gabungan (u꜀)"):
        ua_input = st.number_input("🟦 Masukkan uₐ", value=0.01, step=0.001)
        ub_input = st.number_input("🟩 Masukkan uᵦ", value=0.005, step=0.001)
        if st.button("🧮 Hitung u꜀"):
            uc = np.sqrt(ua_input**2 + ub_input**2)
            st.latex(r"u_c = \sqrt{u_a^2 + u_b^2} = %.4f" % uc)
            st.success(f"Ketidakpastian Gabungan (u꜀): {uc:.4f}")

    # --- STEP 5: Tampilkan Hasil Akhir ---
    with st.expander("5️⃣ Hasil Akhir Pengukuran"):
        rata_input = st.number_input("📌 Masukkan nilai rata-rata pengukuran (x̄)", value=10.2, step=0.001)
        uc_input = st.number_input("📎 Masukkan u꜀", value=0.012, step=0.001)
        if st.button("✅ Tampilkan Hasil Akhir"):
            persen = (uc_input / rata_input) * 100
            st.markdown(f"### 📏 Hasil: **{rata_input:.4f} ± {uc_input:.4f}**")
            st.markdown(f"📊 Persentase ketidakpastian: **{persen:.2f}%**")
            if persen < 1:
                st.success("🎯 Akurasi tinggi (ketidakpastian < 1%)")
            elif persen < 5:
                st.info("✔️ Akurasi sedang (1%-5%)")
            else:
                st.warning("⚠️ Akurasi rendah (>5%)")
# ===  FAKTOR KESALAHAN PENGUKURAN   === #
elif menu == "Faktor Kesalahan":  
    
    # Header & Deskripsi Menarik
    st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #4682b4;'>Faktor <span style='color:#ff8c00;'>Kesalahan</span>!</h1>
        <h5 style='font-weight: normal;'>Beberapa <i>Faktor dan Kemungkinan </i>Jika Akurasi Rendah!</h5>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: justify; font-size: 16px;'>
    Dalam kegiatan pengukuran, khususnya dalam eksperimen fisika atau pengamatan ilmiah, hasil pengukuran seringkali tidak sepenuhnya akurat. Perbedaan antara hasil pengukuran dan nilai sebenarnya disebut dengan <b>galat</b> atau <b>kesalahan pengukuran</b>. Galat ini tidak selalu disebabkan oleh ketidaktelitian pengamat, namun juga bisa muncul akibat berbagai faktor yang berkaitan dengan alat ukur, metode yang digunakan, maupun kondisi lingkungan saat pengukuran dilakukan. Memahami penyebab galat sangat penting agar kita dapat meningkatkan ketelitian, mengurangi kesalahan, dan memperoleh hasil yang lebih akurat dalam setiap proses pengukuran.
    </p>
    """, unsafe_allow_html=True)
    
    # Daftar faktor penyebab galat
    st.markdown("""
      <li><b>Kesalahan Kalibrasi Alat</b><br>
      Alat ukur tidak dikalibrasi dengan standar yang benar. <br>
      Contoh: neraca yang tidak disetel ke nol sebelum digunakan.</li><br>
    
      <li><b>Kesalahan Titik Nol (Zero Error)</b><br>
      Alat ukur menunjukkan angka selain nol saat belum digunakan. <br>
      Menyebabkan semua hasil pengukuran menjadi bias.</li><br>
    
      <li><b>Kualitas dan Kondisi Alat Ukur</b><br>
      Alat aus, rusak, atau sudah tidak presisi lagi. <br>
      Termasuk adanya goresan pada skala atau jarum yang tidak akurat.</li><br>
    
      <li><b>Kesalahan Pembacaan Skala (Paralaks)</b><br>
      Sudut pandang tidak tegak lurus terhadap skala alat. <br>
      Mengakibatkan hasil pembacaan tampak lebih atau kurang dari nilai sebenarnya.</li><br>
    
      <li><b>Lingkungan Sekitar</b><br>
      Suhu, kelembaban, dan tekanan dapat mempengaruhi hasil pengukuran. <br>
      Contoh: pita pengukur logam bisa memuai saat suhu tinggi.</li><br>
    
      <li><b>Pengaruh Gaya Luar</b><br>
      Getaran, tekanan jari, atau gangguan fisik lainnya saat alat digunakan.</li><br>
    
      <li><b>Kesalahan Pengamat (Human Error)</b><br>
      Kesalahan mencatat, salah baca, terburu-buru, atau kurang teliti. <br>
      Termasuk kebiasaan menggampangkan pengukuran tanpa kontrol ulang.</li><br>
    
      <li><b>Metode Pengukuran yang Tidak Sesuai</b><br>
      Teknik atau prosedur pengukuran tidak dilakukan dengan benar. <br>
      Contoh: pengukuran panjang benda bengkok dengan penggaris lurus.</li><br>
    
      <li><b>Pemakaian Alat yang Tidak Sesuai Jenis Pengukuran</b><br>
      Menggunakan alat yang tidak cocok untuk objek atau skala pengukuran tertentu.</li>
    </ul>
    """, unsafe_allow_html=True)

# ===   Contoh Soal dan Pembahasan   === #
elif menu == "Contoh Soal":
    st.header("🧠 Contoh Soal dan Pembahasan")

    # ======= Tabel Pertama =======
    st.subheader("📋 Tabel Data Percobaan 1")

    data1 = {
        "Ulangan": ["1.", "2.", "3.", "4.", "5.", "Rerata"],
        "Nilai X (cm)": [11.3, 11.7, 11.3, 11.5, 11.3, 11.42],
        "Nilai Y (cm)": [5.3, 5.5, 5.3, 5.3, 5.7, 5.4],
    }

    df1 = pd.DataFrame(data1)
    st.table(df1)

    st.markdown("""
    **Keterangan Tabel 1:**
    
    - Data percobaan berulang terhadap dua variabel (X dan Y) dengan Δ ketidakpastian.
    - Nilai rata-rata sudah dihitung pada baris "Rerata".
    """)

    st.markdown("---")

    # ======= Tabel Kedua =======
    st.subheader("📋 Tabel Data Percobaan 2")

    data2 = {
        "Ulangan": ["1.", "2.", "3.", "4.", "5.", "Rerata"],
        "Nilai X (cm)": [3.0, 4.0, 4.3, 4.0, 4.5, 4.0],
        "Nilai Y (cm)": [1.7, 2.0, 2.7, 2.5, 2.0, 2.2]
    }

    df2 = pd.DataFrame(data2)
    st.table(df2)

    st.markdown("""
    **Keterangan Tabel 2:**
    
    - Data percobaan berbeda dengan variabel X dan Y, tanpa Δ ketidakpastian.
    - Nilai rata-rata sudah tersedia di baris "Rerata".
    """)

    st.success("Silakan gunakan tabel ini untuk latihan menghitung ketidakpastian, simpangan baku, atau analisis lainnya.")
