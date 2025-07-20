import streamlit as st
import numpy as np
import pandas as pd

# ====== CUSTOM BACKGROUND & SIDEBAR ======
st.markdown("""
    <style>
    /* Background halaman utama */
    .stApp {
        background: url('data:image/jpeg;base64,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');
        background-size: cover;
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
