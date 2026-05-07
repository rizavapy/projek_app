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

.stApp {
    background: linear-gradient(to bottom, #fff7f0, #ffe4cc);
}

.title {
    text-align:center;
    color:#ff6600;
    font-size:55px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#6c757d;
    font-size:20px;
    margin-bottom:30px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 25px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
}

.price {
    color:#28a745;
    font-size:24px;
    font-weight:bold;
}

.discount {
    color:#dc3545;
    font-size:18px;
    font-weight:bold;
}

.sidebar .sidebar-content {
    background-color:#fff0e6;
}

[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #ff9966, #ff5e62);
    color: white;
}

[data-testid="stSidebar"] * {
    color: white;
}

.stButton>button {
    background-color:#ff6600;
    color:white;
    border-radius:10px;
    border:none;
    padding:10px 20px;
    font-weight:bold;
}

.stButton>button:hover {
    background-color:#ff8533;
}

</style>
""", unsafe_allow_html=True)

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
# SIDEBAR
# ==========================================

st.sidebar.title("🍿 Snack Cecilia")

st.sidebar.markdown("## 🏷️ Generate Barcode")

barcode_text = st.sidebar.text_input(
    "Masukkan Kode Barcode"
)

if st.sidebar.button("Generate Barcode"):

    if barcode_text != "":

        code128 = barcode.get_barcode_class('code128')

        generated = code128(
            barcode_text,
            writer=ImageWriter()
        )

        filename = generated.save("barcode_produk")

        st.sidebar.success("Barcode berhasil dibuat!")

        st.sidebar.image(filename)

st.sidebar.markdown("---")

st.sidebar.info(
    "Gunakan barcode untuk mengecek "
    "informasi produk Snack Cecilia."
)

# ==========================================
# CEK PRODUK DARI BARCODE
# ==========================================

st.write("")
st.write("")
st.subheader("🔍 Cek Informasi Produk")

barcode_input = st.text_input("Masukkan Kode Barcode Produk")

if barcode_input:

    found = False

    for product in products:

        if product["Barcode"] == barcode_input:

            st.success("Produk Ditemukan!")

            st.write(f"🍟 Nama : {product['Nama']}")
            st.write(f"💰 Harga : Rp {product['Harga']:,}")
            st.write(f"🔥 Diskon : {product['Diskon']}")
            st.write(f"📅 Produksi : {product['Tanggal Produksi']}")
            st.write(f"⏳ Expired : {product['Expired']}")
            st.write(f"🥣 Bahan : {product['Bahan']}")

            found = True

    if not found:
        st.error("Produk tidak ditemukan")

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
