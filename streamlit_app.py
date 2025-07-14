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
    st.title("🎉 Selamat Datang di UncertaintyCalc!")
    st.write("Slide edukasi pengukuran:")

    slide_index = st.slider("Pilih Slide", 1, 3, 1)
    slide_paths = {
        1: ("https://www.sentrakalibrasiindustri.com/wp-content/uploads/2022/12/ketidakpastian-dalam-pengukuran-tunggal.jpg", "Ilustrasi Ketidakpastian"),
        2: ("https://asset-a.grid.id/crop/0x0:0x0/700x465/photo/2023/08/01/ukuranjpg-20230801094936.jpg", "Diagram Statistik"),
        3: ("https://guruonlinee.com/wp-content/uploads/2022/08/ketidakpastian-pengukuran-fisika-1-e1660916689220.jpg", "Contoh Pengukuran")
    }

    img_path, caption = slide_paths[slide_index]
    st.image(img_path, caption=caption, use_column_width=True)


    st.markdown("""
    Situs web interaktif untuk memahami dan menghitung nilai ketidakpastian dalam pengukuran ilmiah dan teknis.

    📏 **Apa Itu Nilai Ketidakpastian?**  
    Dalam setiap pengukuran, selalu ada kemungkinan kesalahan atau deviasi dari nilai sebenarnya.  
    Nilai ketidakpastian membantu kita mengetahui seberapa akurat hasil pengukuran kita.

    Gunakan menu di sebelah kiri untuk mulai belajar atau menghitung!
    """)

# === DASAR TEORI ===
elif menu == "Dasar Teori":
    st.title("📚 Dasar Teori Ketidakpastian Pengukuran")
    st.markdown("""
    **Jenis Ketidakpastian:**
    - **Tipe A (Statistik):** Berdasarkan hasil pengukuran berulang.
    - **Tipe B (Non-Statistik):** Berdasarkan perkiraan, kalibrasi alat, atau pengalaman.

    **Tujuan:**
    - Mengetahui keandalan hasil pengukuran.
    - Menentukan batas toleransi dari alat atau proses pengukuran.

    **Simbol yang Sering Digunakan:**
    - 𝑥̄: Rata-rata
    - 𝑠: Simpangan baku
    - 𝑢: Ketidakpastian
    """)

# === KALKULATOR TIPE A & B ===
elif menu == "Kalkulator Ketidakpastian":
    st.title("📊 Kalkulator Ketidakpastian (Tipe A & Tipe B)")

    st.header("Tipe A - Berdasarkan Data Pengukuran")
    data_input = st.text_area("Masukkan data pengukuran (pisahkan dengan koma)", "10.1, 10.3, 10.2, 10.4, 10.2")

    if st.button("Hitung Tipe A"):
        try:
            data = np.array([float(x.strip()) for x in data_input.split(",")])
            rata2 = np.mean(data)
            std_dev = np.std(data, ddof=1)
            ua = std_dev / np.sqrt(len(data))
            st.success(f"Rata-rata: {rata2:.4f}")
            st.success(f"Simpangan Baku: {std_dev:.4f}")
            st.success(f"Ketidakpastian Tipe A: {ua:.4f}")
        except:
            st.error("Format input tidak valid. Pastikan hanya angka dipisahkan koma.")

    st.header("Tipe B - Berdasarkan Estimasi")
    resolusi = st.number_input("Masukkan nilai resolusi alat ukur", value=0.01)
    ub = resolusi / np.sqrt(3)
    st.info(f"Ketidakpastian Tipe B: {ub:.4f}")

# === PERHITUNGAN MANUAL ===
elif menu == "Cara Perhitungan Manual":
    st.title("📝 Cara Perhitungan Manual Ketidakpastian")
    st.markdown("""
    **Langkah-langkah Tipe A:**
    1. Catat data pengukuran berulang.
    2. Hitung rata-rata dan simpangan baku.
    3. Ketidakpastian Tipe A = simpangan baku / √jumlah data.

    **Langkah-langkah Tipe B:**
    1. Ambil nilai resolusi alat atau estimasi lainnya.
    2. Ketidakpastian Tipe B = resolusi / √3

    **Gabungan:**
    \[
    u_c = \sqrt{u_A^2 + u_B^2}
    \]
    """)

# === FAKTOR KESALAHAN ===
elif menu == "Faktor Kesalahan":
    st.title("⚠️ Faktor yang Mempengaruhi Ketidakpastian")
    st.markdown("""
    Beberapa faktor yang bisa mempengaruhi besar kecilnya ketidakpastian:
    
    - **Suhu dan Kelembaban:** Perubahan suhu dapat menyebabkan ekspansi/perubahan pada alat ukur.
    - **Resolusi Alat Ukur:** Semakin kecil resolusi, semakin tinggi ketelitian.
    - **Kesalahan Sistematik:** Misalnya alat yang tidak dikalibrasi.
    - **Kesalahan Manusia:** Cara membaca skala, posisi mata, dll.
    """)

# === CONTOH SOAL ===
elif menu == "Contoh Soal dan Pembahasan":
    st.title("🧠 Contoh Soal dan Pembahasan")
    st.markdown("""
    **Soal:**
    Seorang siswa melakukan pengukuran panjang sebanyak 5 kali dengan hasil:  
    10.1 cm, 10.3 cm, 10.2 cm, 10.4 cm, dan 10.2 cm.  
    Tentukan ketidakpastian Tipe A, jika resolusi alat ukur adalah 0.01 cm.

    **Penyelesaian:**
    - Rata-rata = (10.1 + 10.3 + 10.2 + 10.4 + 10.2) / 5 = 10.24
    - Simpangan baku (s) ≈ 0.114
    - Ketidakpastian Tipe A = s / √n = 0.114 / √5 ≈ 0.051
    - Ketidakpastian Tipe B = 0.01 / √3 ≈ 0.0058
    - Ketidakpastian gabungan:
      \[
      u_c = \sqrt{0.051^2 + 0.0058^2} ≈ 0.0513
      \]

    ✅ **Jadi, ketidakpastian gabungan adalah ±0.0513 cm**
    """)
