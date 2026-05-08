🍟 SnackStore – Aplikasi Manajemen Camilan Nusantara
Aplikasi Streamlit lengkap untuk manajemen toko camilan dengan fitur pembeli dan penjual.
✨ Fitur Utama
🏠 Beranda (Untuk Pembeli)

Katalog 9 produk camilan dengan informasi lengkap
Kartu produk yang bisa dibuka (expand): nama, harga, berat, expired, barcode, WhatsApp
Tombol pesan langsung via WhatsApp
Sistem rating bintang (1-5) dan komentar pembeli
Pencarian dan sorting produk

🔐 Panel Penjual (Sidebar 2) — Password Protected

Dashboard statistik real-time
Edit dan tambah produk baru
Manajemen stok

📦 Generator Barcode (Sidebar 3)

Generate barcode EAN-13 otomatis (12 digit)
Input manual barcode
Cetak barcode produk existing
Download gambar barcode PNG

💳 QRIS & Pembayaran (Sidebar 4)

Generate QR Code QRIS toko
Catat transaksi penjualan manual
History transaksi terbaru

📊 Laporan & Analitik (Sidebar 5)

Laporan Laba Rugi otomatis (P&L)
Grafik penjualan per produk
Tren penjualan harian
Manajemen pengeluaran
Export CSV

📱 Preview Tampilan (Sidebar 6)

Proyeksi tampilan HP pembeli (frame iPhone)
Proyeksi tampilan HP penjual
Penjelasan fitur di setiap sisi

🚀 Cara Menjalankan
Local
bashpip install -r requirements.txt
streamlit run app.py
Streamlit Cloud (GitHub)

Fork repo ini
Buka share.streamlit.io
Connect ke GitHub repo
Set app.py sebagai main file
Deploy!

🔐 Kredensial Default

Password Penjual: seller123
Ganti di baris SELLER_PASSWORD = "seller123" di app.py

📁 Struktur File
├── app.py                  # Aplikasi utama
├── requirements.txt        # Dependencies
├── snackstore_data.json    # Database (auto-generated)
└── README.md
🛠 Teknologi

Streamlit — Framework UI
python-barcode — Generate EAN-13 barcode
qrcode — Generate QRIS QR Code
Pandas + Matplotlib — Analitik & visualisasi data
Pillow — Pemrosesan gambar

📦 Produk yang Tersedia

Keripik Tempe
Keripik Talas
Stick Talas
Telur Gabus Keju
Keripik Singkong
Kacang Bogor
Kacang Bandung
Kacang Koro
Kue Kering
Dll

Dibuat dengan ❤️ untuk UMKM Indonesia
