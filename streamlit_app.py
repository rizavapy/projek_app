# app.py
# ==========================================
# Snack Cecilia - Toko Online Snack
# Streamlit App + Barcode Scanner
# ==========================================

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image
import barcode
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
import os

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Snack Cecilia",
    page_icon="🍟",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.main {
    background-color: #fff8f0;
}

.title {
    text-align:center;
    color:#d35400;
    font-size:50px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#7f8c8d;
    font-size:20px;
}

.card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.price {
    color:green;
    font-size:22px;
    font-weight:bold;
}

.discount {
    color:red;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("<div class='title'>🍿 Snack Cecilia 🍿</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Toko Online Snack Terlengkap dan Termurah</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# DATA PRODUK
# ==========================================

products = [
    {
        "Nama": "Keripik Pisang",
        "Harga": 15000,
        "Diskon": "10%",
        "Tanggal Produksi": "2026-05-01",
        "Expired": "2026-11-01",
        "Bahan": "Pisang, Minyak, Gula",
        "Barcode": "111111"
    },
    {
        "Nama": "CocoCrunch",
        "Harga": 12000,
        "Diskon": "5%",
        "Tanggal Produksi": "2026-04-20",
        "Expired": "2026-10-20",
        "Bahan": "Coklat, Gandum, Gula",
        "Barcode": "222222"
    },
    {
        "Nama": "Keripik Singkong",
        "Harga": 10000,
        "Diskon": "15%",
        "Tanggal Produksi": "2026-05-02",
        "Expired": "2026-09-02",
        "Bahan": "Singkong, Garam, Minyak",
        "Barcode": "333333"
    },
    {
        "Nama": "Macaroni",
        "Harga": 13000,
        "Diskon": "8%",
        "Tanggal Produksi": "2026-05-03",
        "Expired": "2026-10-03",
        "Bahan": "Tepung, Bumbu Pedas",
        "Barcode": "444444"
    },
    {
        "Nama": "Waffer",
        "Harga": 9000,
        "Diskon": "12%",
        "Tanggal Produksi": "2026-05-04",
        "Expired": "2026-12-04",
        "Bahan": "Tepung, Susu, Coklat",
        "Barcode": "555555"
    },
    {
        "Nama": "Astor",
        "Harga": 14000,
        "Diskon": "20%",
        "Tanggal Produksi": "2026-05-05",
        "Expired": "2026-11-05",
        "Bahan": "Coklat, Tepung",
        "Barcode": "666666"
    },
    {
        "Nama": "Kentang Balado",
        "Harga": 16000,
        "Diskon": "10%",
        "Tanggal Produksi": "2026-05-06",
        "Expired": "2026-10-06",
        "Bahan": "Kentang, Cabai",
        "Barcode": "777777"
    },
    {
        "Nama": "Stick Kentang",
        "Harga": 11000,
        "Diskon": "5%",
        "Tanggal Produksi": "2026-05-07",
        "Expired": "2026-09-07",
        "Bahan": "Kentang, Garam",
        "Barcode": "888888"
    },
    {
        "Nama": "Kuping Gajah",
        "Harga": 17000,
        "Diskon": "7%",
        "Tanggal Produksi": "2026-05-08",
        "Expired": "2026-11-08",
        "Bahan": "Tepung, Gula",
        "Barcode": "999999"
    },
    {
        "Nama": "Kue Sagu",
        "Harga": 18000,
        "Diskon": "13%",
        "Tanggal Produksi": "2026-05-09",
        "Expired": "2026-12-09",
        "Bahan": "Sagu, Mentega",
        "Barcode": "101010"
    },
    {
        "Nama": "Roti Kering",
        "Harga": 15000,
        "Diskon": "9%",
        "Tanggal Produksi": "2026-05-10",
        "Expired": "2026-10-10",
        "Bahan": "Roti, Mentega, Gula",
        "Barcode": "121212"
    }
]

# ==========================================
# SEARCH
# ==========================================

search = st.text_input("🔍 Cari Snack")

filtered_products = [
    p for p in products
    if search.lower() in p["Nama"].lower()
]

# ==========================================
# DISPLAY PRODUCTS
# ==========================================

st.subheader("🛒 Daftar Produk")

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(
            "https://cdn-icons-png.flaticon.com/512/2553/2553691.png",
            width=120
        )

        st.subheader(product["Nama"])

        st.markdown(
            f"<div class='price'>Rp {product['Harga']:,}</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='discount'>Diskon {product['Diskon']}</div>",
            unsafe_allow_html=True
        )

        st.write(f"📅 Produksi : {product['Tanggal Produksi']}")
        st.write(f"⏳ Expired : {product['Expired']}")
        st.write(f"🥣 Bahan : {product['Bahan']}")
        st.write(f"📦 Barcode : {product['Barcode']}")

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# BARCODE GENERATOR
# ==========================================

st.write("")
st.write("")
st.subheader("🏷️ Generate Barcode Produk")

barcode_text = st.text_input("Masukkan Kode Barcode")

if st.button("Generate Barcode"):

    if barcode_text != "":

        code128 = barcode.get_barcode_class('code128')

        generated = code128(
            barcode_text,
            writer=ImageWriter()
        )

        filename = generated.save("barcode_produk")

        st.success("Barcode berhasil dibuat!")

        st.image(filename)

# ==========================================
# BARCODE SCANNER
# ==========================================

st.write("")
st.write("")
st.subheader("📷 Scan Barcode Produk")

uploaded_file = st.file_uploader(
    "Upload Gambar Barcode",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    decoded = decode(image)

    if decoded:

        barcode_data = decoded[0].data.decode("utf-8")

        st.success(f"Barcode Terdeteksi: {barcode_data}")

        found = False

        for product in products:

            if product["Barcode"] == barcode_data:

                st.write("## Informasi Produk")
                st.write(f"🍟 Nama : {product['Nama']}")
                st.write(f"💰 Harga : Rp {product['Harga']:,}")
                st.write(f"🔥 Diskon : {product['Diskon']}")
                st.write(f"📅 Produksi : {product['Tanggal Produksi']}")
                st.write(f"⏳ Expired : {product['Expired']}")
                st.write(f"🥣 Bahan : {product['Bahan']}")

                found = True

        if not found:
            st.error("Produk tidak ditemukan")

    else:
        st.error("Barcode tidak terbaca")

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")
st.markdown("---")
st.markdown(
    "<center>© 2026 Snack Cecilia | Toko Snack Online</center>",
    unsafe_allow_html=True
)
