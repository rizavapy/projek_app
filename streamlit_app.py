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

<p><strong>Galat (atau kesalahan) pengukuran </stong> adalah perbedaan antara nilai yang diukur dengan nilai sebenarnya dari suatu besaran.</p>
    
<p><strong>Galat Sistematis:</strong> Galat yang cenderung tetap dan dapat diprediksi, disebabkan oleh kesalahan pada alat ukur atau metode pengukuran. Contohnya, kesalahan kalibrasi atau titik nol pada alat ukur.</p>
    
<p><strong>Galat Acak:</strong> Galat yang tidak dapat diprediksi dan bervariasi secara acak, disebabkan oleh faktor-faktor yang tidak terkontrol seperti fluktuasi lingkungan atau kesalahan pengamat.</p>
    
<p><strong>Galat Umum (Kekeliruan):</strong> Galat yang disebabkan oleh kesalahan manusia, seperti kesalahan membaca skala atau kesalahan dalam mencatat hasil.</p>
    
<p><strong>Galat Absolut:</strong> Selisih antara nilai terukur dengan nilai sebenarnya.</p>
    
<p><strong>Galat Relatif:</strong> Galat absolut dibagi dengan nilai sebenarnya, sering dinyatakan dalam persen.</p>
    
<p><strong>Distribusi Galat:</strong> Pengukuran berulang dapat menghasilkan distribusi galat yang dapat dianalisis secara statistik untuk mendapatkan informasi tentang keakuratan dan presisi pengukuran.</p>
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
# Paragraf pendahuluan
    st.markdown("""
    <p style='text-align: justify; font-size: 16px;'>
    Dalam kegiatan pengukuran, khususnya dalam eksperimen fisika atau pengamatan ilmiah, hasil pengukuran seringkali tidak sepenuhnya akurat. Perbedaan antara hasil pengukuran dan nilai sebenarnya disebut dengan <b>galat</b> atau <b>kesalahan pengukuran</b>. Galat ini tidak selalu disebabkan oleh ketidaktelitian pengamat, namun juga bisa muncul akibat berbagai faktor yang berkaitan dengan alat ukur, metode yang digunakan, maupun kondisi lingkungan saat pengukuran dilakukan. Memahami penyebab galat sangat penting agar kita dapat meningkatkan ketelitian, mengurangi kesalahan, dan memperoleh hasil yang lebih akurat dalam setiap proses pengukuran.
    </p>
    """, unsafe_allow_html=True)
    
    # Daftar faktor penyebab galat
    st.markdown("""
    <ul style='font-size: 16px;'>
       with st.expander("Kesalahan Kalibrasi Alat"):
            st.latex("Alat ukur tidak dikalibrasi dengan standar yang benar.
             Contoh: neraca yang tidak disetel ke nol sebelum digunakan.")

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
elif menu == "Contoh Soal dan Pembahasan":
    # Membuat window utama
    root = tk.Tk()
    root.title("Tabel Percobaan")

    # Membuka gambar tabel
    gambar = Image.open("0a8f6ef0-aed5-47d8-a495-355082ea8ebc.png")  # Pastikan file di folder yang sama
    gambar = gambar.resize((400, 300))  # Sesuaikan ukuran jika perlu
    img_tabel = ImageTk.PhotoImage(gambar)

    # Menyimpan referensi gambar agar tidak terhapus dari memori
    label_gambar = tk.Label(root, image=img_tabel)
    label_gambar.image = img_tabel  # INI WAJIB supaya gambar tidak hilang saat ditampilkan
    label_gambar.pack()

    # Jalankan aplikasi
    root.mainloop()
