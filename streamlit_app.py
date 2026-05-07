# ==========================================
# Snack Cecilia - Toko Online Snack
# Streamlit App + Barcode + QRIS Generator
# ==========================================
 
import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
import qrcode
import qrcode.image.svg
import barcode
from barcode.writer import ImageWriter
import os
 
# ==========================================
# CONFIG
# ==========================================
 
st.set_page_config(
    page_title="Snack Cecilia 🍿",
    page_icon="🍟",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
# ==========================================
# CUSTOM CSS
# ==========================================
 
st.markdown("""
<style>
 
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Nunito:wght@400;600;700;800&display=swap');
 
/* ---- GLOBAL ---- */
html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}
 
.stApp {
    background: linear-gradient(135deg, #fff8f2 0%, #ffe8d6 50%, #ffd6b8 100%);
    min-height: 100vh;
}
 
/* ---- HEADER ---- */
.hero-title {
    font-family: 'Pacifico', cursive;
    text-align: center;
    font-size: 64px;
    background: linear-gradient(135deg, #ff6b35, #f7c59f, #ff6b35);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shine 3s linear infinite;
    margin-bottom: 0;
    line-height: 1.2;
    text-shadow: none;
    filter: drop-shadow(2px 4px 6px rgba(255,107,53,0.25));
}
 
@keyframes shine {
    to { background-position: 200% center; }
}
 
.hero-subtitle {
    text-align: center;
    color: #b5613a;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 35px;
    margin-top: 8px;
}
 
.hero-divider {
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #ff6b35, #ffa07a);
    border-radius: 99px;
    margin: 0 auto 30px auto;
}
 
/* ---- SEARCH BAR ---- */
div[data-testid="stTextInput"] > div > div > input {
    border-radius: 50px !important;
    border: 2px solid #ffb085 !important;
    background: white !important;
    padding: 12px 20px !important;
    font-size: 16px !important;
    box-shadow: 0 4px 15px rgba(255,107,53,0.15) !important;
    font-family: 'Nunito', sans-serif !important;
}
 
div[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #ff6b35 !important;
    box-shadow: 0 4px 20px rgba(255,107,53,0.3) !important;
}
 
/* ---- PRODUCT CARDS ---- */
.product-card {
    background: white;
    padding: 22px 18px;
    border-radius: 24px;
    box-shadow: 0 8px 30px rgba(255, 107, 53, 0.12);
    margin-bottom: 24px;
    border: 1.5px solid rgba(255, 180, 130, 0.3);
    transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    position: relative;
    overflow: hidden;
}
 
.product-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, #ff6b35, #ffa07a, #ff6b35);
    background-size: 200% auto;
    animation: shine 3s linear infinite;
}
 
.product-card:hover {
    transform: translateY(-8px) scale(1.01);
    box-shadow: 0 20px 50px rgba(255, 107, 53, 0.22);
    border-color: rgba(255, 107, 53, 0.4);
}
 
.product-name {
    font-family: 'Nunito', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #2d2013;
    margin: 10px 0 4px 0;
}
 
.product-price {
    color: #ff6b35;
    font-size: 22px;
    font-weight: 800;
}
 
.product-original-price {
    color: #aaa;
    font-size: 14px;
    text-decoration: line-through;
    margin-left: 6px;
    font-weight: 600;
}
 
.discount-badge {
    display: inline-block;
    background: linear-gradient(135deg, #ff6b35, #ff4500);
    color: white;
    font-size: 12px;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}
 
.info-row {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: #666;
    margin: 4px 0;
    font-weight: 600;
}
 
.barcode-tag {
    display: inline-block;
    background: #f0f0f0;
    color: #555;
    font-size: 12px;
    font-family: 'Courier New', monospace;
    padding: 3px 10px;
    border-radius: 8px;
    margin-top: 6px;
    font-weight: 700;
    letter-spacing: 1px;
}
 
/* ---- SECTION HEADER ---- */
.section-header {
    font-family: 'Nunito', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #2d2013;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
 
/* ---- SIDEBAR ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ff6b35 0%, #e8421a 100%);
}
 
[data-testid="stSidebar"] .stRadio label {
    color: white !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}
 
[data-testid="stSidebar"] .stRadio > div {
    gap: 8px;
}
 
[data-testid="stSidebar"] * {
    color: white !important;
}
 
[data-testid="stSidebar"] .stRadio > div > div:hover {
    background: rgba(255,255,255,0.15);
    border-radius: 12px;
}
 
/* ---- BUTTONS ---- */
.stButton > button {
    background: linear-gradient(135deg, #ff6b35, #ff4500) !important;
    color: white !important;
    border-radius: 50px !important;
    border: none !important;
    padding: 12px 32px !important;
    font-size: 16px !important;
    font-weight: 800 !important;
    font-family: 'Nunito', sans-serif !important;
    letter-spacing: 0.5px;
    box-shadow: 0 6px 20px rgba(255,107,53,0.35) !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}
 
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 30px rgba(255,107,53,0.5) !important;
}
 
/* ---- INPUT FIELDS ---- */
div[data-testid="stTextInput"] label,
div[data-testid="stNumberInput"] label {
    font-weight: 700 !important;
    color: #2d2013 !important;
    font-size: 14px !important;
}
 
/* ---- GENERATOR SECTION ---- */
.gen-card {
    background: white;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 40px rgba(255,107,53,0.1);
    border: 1.5px solid rgba(255,180,130,0.25);
    margin-bottom: 24px;
}
 
.gen-title {
    font-family: 'Pacifico', cursive;
    font-size: 36px;
    background: linear-gradient(135deg, #ff6b35, #e8421a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
}
 
.gen-desc {
    color: #888;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 24px;
}
 
.result-box {
    background: linear-gradient(135deg, #fff8f2, #ffe8d6);
    border-radius: 20px;
    padding: 24px;
    border: 2px solid rgba(255,107,53,0.2);
    text-align: center;
    margin-top: 20px;
}
 
.result-label {
    font-weight: 800;
    color: #ff6b35;
    font-size: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
}
 
/* ---- STATS STRIP ---- */
.stats-strip {
    display: flex;
    gap: 16px;
    margin-bottom: 30px;
    flex-wrap: wrap;
}
 
.stat-chip {
    background: white;
    border-radius: 50px;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-weight: 700;
    font-size: 14px;
    color: #2d2013;
    box-shadow: 0 4px 15px rgba(0,0,0,0.07);
    border: 1.5px solid rgba(255,180,130,0.3);
}
 
/* ---- EMPTY STATE ---- */
.empty-state {
    text-align: center;
    padding: 60px 20px;
    color: #bbb;
}
 
/* ---- SUCCESS ALERT ---- */
div[data-testid="stSuccess"] {
    border-radius: 14px !important;
    font-weight: 700 !important;
}
 
/* ---- SELECTBOX ---- */
div[data-testid="stSelectbox"] > div {
    border-radius: 12px !important;
    border: 2px solid #ffb085 !important;
}
 
/* ---- NUMBER INPUT ---- */
div[data-testid="stNumberInput"] > div > div > input {
    border-radius: 12px !important;
    border: 2px solid #ffb085 !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 700 !important;
}
 
/* ---- COLOR PICKER ---- */
div[data-testid="stColorPicker"] label {
    font-weight: 700 !important;
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
        "Diskon": 10,
        "Tanggal Produksi": "2026-05-01",
        "Expired": "2026-11-01",
        "Bahan": "Pisang, Minyak, Gula",
        "Barcode": "111111",
        "Kategori": "Keripik"
    },
    {
        "Nama": "CocoCrunch",
        "Harga": 12000,
        "Diskon": 5,
        "Tanggal Produksi": "2026-04-20",
        "Expired": "2026-10-20",
        "Bahan": "Coklat, Gandum, Gula",
        "Barcode": "222222",
        "Kategori": "Coklat"
    },
    {
        "Nama": "Keripik Singkong",
        "Harga": 10000,
        "Diskon": 15,
        "Tanggal Produksi": "2026-05-02",
        "Expired": "2026-09-02",
        "Bahan": "Singkong, Garam, Minyak",
        "Barcode": "333333",
        "Kategori": "Keripik"
    },
    {
        "Nama": "Macaroni",
        "Harga": 13000,
        "Diskon": 8,
        "Tanggal Produksi": "2026-05-03",
        "Expired": "2026-10-03",
        "Bahan": "Tepung, Bumbu Pedas",
        "Barcode": "444444",
        "Kategori": "Pedas"
    },
    {
        "Nama": "Waffer",
        "Harga": 9000,
        "Diskon": 12,
        "Tanggal Produksi": "2026-05-04",
        "Expired": "2026-12-04",
        "Bahan": "Tepung, Susu, Coklat",
        "Barcode": "555555",
        "Kategori": "Coklat"
    },
    {
        "Nama": "Astor",
        "Harga": 14000,
        "Diskon": 20,
        "Tanggal Produksi": "2026-05-05",
        "Expired": "2026-11-05",
        "Bahan": "Coklat, Tepung",
        "Barcode": "666666",
        "Kategori": "Coklat"
    },
    {
        "Nama": "Kentang Balado",
        "Harga": 16000,
        "Diskon": 10,
        "Tanggal Produksi": "2026-05-06",
        "Expired": "2026-10-06",
        "Bahan": "Kentang, Cabai",
        "Barcode": "777777",
        "Kategori": "Pedas"
    },
    {
        "Nama": "Stick Kentang",
        "Harga": 11000,
        "Diskon": 5,
        "Tanggal Produksi": "2026-05-07",
        "Expired": "2026-09-07",
        "Bahan": "Kentang, Garam",
        "Barcode": "888888",
        "Kategori": "Keripik"
    },
    {
        "Nama": "Kuping Gajah",
        "Harga": 17000,
        "Diskon": 7,
        "Tanggal Produksi": "2026-05-08",
        "Expired": "2026-11-08",
        "Bahan": "Tepung, Gula",
        "Barcode": "999999",
        "Kategori": "Manis"
    },
    {
        "Nama": "Kue Sagu",
        "Harga": 18000,
        "Diskon": 13,
        "Tanggal Produksi": "2026-05-09",
        "Expired": "2026-12-09",
        "Bahan": "Sagu, Mentega",
        "Barcode": "101010",
        "Kategori": "Manis"
    },
    {
        "Nama": "Roti Kering",
        "Harga": 15000,
        "Diskon": 9,
        "Tanggal Produksi": "2026-05-10",
        "Expired": "2026-10-10",
        "Bahan": "Roti, Mentega, Gula",
        "Barcode": "121212",
        "Kategori": "Manis"
    }
]
 
# ==========================================
# HELPER FUNCTIONS
# ==========================================
 
def hitung_harga_diskon(harga, diskon_persen):
    return int(harga - (harga * diskon_persen / 100))
 
def cek_status_expired(expired_str):
    try:
        exp_date = datetime.strptime(expired_str, "%Y-%m-%d")
        hari_sisa = (exp_date - datetime.now()).days
        if hari_sisa < 0:
            return "⚠️ Expired", "#dc3545"
        elif hari_sisa <= 30:
            return f"⚡ {hari_sisa} hari lagi", "#ff8c00"
        else:
            return f"✅ {hari_sisa} hari lagi", "#28a745"
    except:
        return expired_str, "#666"
 
def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")
 
# ==========================================
# SIDEBAR MENU
# ==========================================
 
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px 0;'>
        <div style='font-family: Pacifico, cursive; font-size: 28px; color: white;
                    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));'>
            🍿 Snack Cecilia
        </div>
        <div style='font-size: 12px; color: rgba(255,255,255,0.8); margin-top: 4px;
                    font-weight: 600; letter-spacing: 1px;'>
            TOKO SNACK ONLINE
        </div>
    </div>
    <hr style='border-color: rgba(255,255,255,0.3); margin: 10px 0 20px 0;'>
    """, unsafe_allow_html=True)
 
    menu = st.radio(
        "📌 Navigasi",
        [
            "🏪 Beranda",
            "🏷️ Generator Barcode",
            "💳 Generator QRIS"
        ],
        label_visibility="collapsed"
    )
 
    st.markdown("""
    <hr style='border-color: rgba(255,255,255,0.3); margin: 20px 0;'>
    <div style='font-size: 12px; color: rgba(255,255,255,0.7); text-align:center;
                font-weight: 600; padding-bottom: 10px;'>
        © 2026 Snack Cecilia<br>Semua hak dilindungi
    </div>
    """, unsafe_allow_html=True)
 
# ==========================================
# HOME / BERANDA
# ==========================================
 
if menu == "🏪 Beranda":
 
    # Header
    st.markdown("""
        <div class='hero-title'>🍿 Snack Cecilia</div>
        <div class='hero-subtitle'>✨ Camilan Terlengkap & Paling Yummy ✨</div>
        <div class='hero-divider'></div>
    """, unsafe_allow_html=True)
 
    # Stats strip
    total_produk = len(products)
    avg_diskon = sum(p["Diskon"] for p in products) // total_produk
    produk_diskon_besar = sum(1 for p in products if p["Diskon"] >= 10)
 
    st.markdown(f"""
    <div class='stats-strip'>
        <div class='stat-chip'>🛍️ {total_produk} Produk Tersedia</div>
        <div class='stat-chip'>🔥 Diskon Rata-rata {avg_diskon}%</div>
        <div class='stat-chip'>⚡ {produk_diskon_besar} Produk Diskon Besar</div>
        <div class='stat-chip'>🚚 Gratis Ongkir Min. 50rb</div>
    </div>
    """, unsafe_allow_html=True)
 
    # Filter baris
    col_search, col_filter = st.columns([3, 1])
 
    with col_search:
        search = st.text_input(
            "Cari Snack",
            placeholder="🔍  Ketik nama snack favorit kamu...",
            label_visibility="collapsed"
        )
 
    with col_filter:
        kategori_list = ["Semua"] + sorted(set(p["Kategori"] for p in products))
        kategori_filter = st.selectbox(
            "Kategori",
            kategori_list,
            label_visibility="collapsed"
        )
 
    # Filter produk
    filtered_products = [
        p for p in products
        if search.lower() in p["Nama"].lower()
        and (kategori_filter == "Semua" or p["Kategori"] == kategori_filter)
    ]
 
    st.markdown(
        f"<div class='section-header'>🛒 Daftar Produk "
        f"<span style='font-size:16px; color:#999; font-weight:600;'>"
        f"({len(filtered_products)} item)</span></div>",
        unsafe_allow_html=True
    )
 
    if not filtered_products:
        st.markdown("""
        <div class='empty-state'>
            <div style='font-size:60px;'>😕</div>
            <div style='font-size:20px; font-weight:700; color:#aaa;'>
                Produk tidak ditemukan
            </div>
            <div style='color:#ccc; font-size:14px; margin-top:8px;'>
                Coba kata kunci atau kategori yang berbeda
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        cols = st.columns(3)
 
        EMOJI_MAP = {
            "Keripik": "🥔",
            "Coklat": "🍫",
            "Pedas": "🌶️",
            "Manis": "🍬"
        }
 
        for index, product in enumerate(filtered_products):
            with cols[index % 3]:
                harga_asli = product["Harga"]
                diskon = product["Diskon"]
                harga_diskon = hitung_harga_diskon(harga_asli, diskon)
                status_exp, warna_exp = cek_status_expired(product["Expired"])
                emoji = EMOJI_MAP.get(product["Kategori"], "🍿")
 
                st.markdown(f"""
                <div class='product-card'>
                    <div style='text-align:center; font-size:64px; 
                                margin-bottom:6px; line-height:1;'>
                        {emoji}
                    </div>
                    <div style='text-align:center;'>
                        <span class='discount-badge'>🔥 DISKON {diskon}%</span>
                    </div>
                    <div class='product-name' style='text-align:center;'>
                        {product["Nama"]}
                    </div>
                    <div style='text-align:center; margin: 6px 0 10px 0;'>
                        <span class='product-price'>{format_rupiah(harga_diskon)}</span>
                        <span class='product-original-price'>{format_rupiah(harga_asli)}</span>
                    </div>
                    <hr style='border:none; border-top:1px solid #f0e8e0; margin:10px 0;'>
                    <div class='info-row'>📅 Produksi: {product["Tanggal Produksi"]}</div>
                    <div class='info-row' style='color:{warna_exp};'>
                        ⏳ Expired: {status_exp}
                    </div>
                    <div class='info-row'>🥣 {product["Bahan"]}</div>
                    <div style='margin-top:8px; text-align:center;'>
                        <span class='barcode-tag'>📦 {product["Barcode"]}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
 
# ==========================================
# BARCODE GENERATOR
# ==========================================
 
elif menu == "🏷️ Generator Barcode":
 
    st.markdown("""
    <div class='gen-title'>🏷️ Generator Barcode</div>
    <div class='gen-desc'>
        Buat barcode profesional untuk produk snack kamu dalam hitungan detik!
    </div>
    """, unsafe_allow_html=True)
 
    col_form, col_result = st.columns([1, 1], gap="large")
 
    with col_form:
        st.markdown("<div class='gen-card'>", unsafe_allow_html=True)
 
        st.markdown("**⚙️ Konfigurasi Barcode**")
        st.markdown("<br>", unsafe_allow_html=True)
 
        # Pilih produk dari database atau manual
        mode_barcode = st.radio(
            "Mode Input",
            ["📦 Pilih dari Produk", "✏️ Input Manual"],
            horizontal=True
        )
 
        if mode_barcode == "📦 Pilih dari Produk":
            nama_list = [p["Nama"] for p in products]
            pilihan_produk = st.selectbox("Pilih Produk", nama_list)
            produk_terpilih = next(
                (p for p in products if p["Nama"] == pilihan_produk), None
            )
            nama_barcode = produk_terpilih["Nama"]
            kode_barcode = produk_terpilih["Barcode"]
 
            st.info(
                f"📦 Kode: **{kode_barcode}** | "
                f"💰 Harga: **{format_rupiah(produk_terpilih['Harga'])}**"
            )
        else:
            nama_barcode = st.text_input(
                "Nama Produk",
                placeholder="Contoh: Keripik Tempe",
                key="nama_barcode_manual"
            )
            kode_barcode = st.text_input(
                "Kode Barcode",
                placeholder="Contoh: 123456",
                key="kode_barcode_manual"
            )
 
        st.markdown("<br>", unsafe_allow_html=True)
 
        tipe_barcode = st.selectbox(
            "Format Barcode",
            ["code128", "ean13", "ean8", "upca"],
            format_func=lambda x: {
                "code128": "Code 128 (Umum)",
                "ean13": "EAN-13 (Retail)",
                "ean8": "EAN-8 (Mini)",
                "upca": "UPC-A (Amerika)"
            }.get(x, x)
        )
 
        generate_btn = st.button("🎯 Generate Barcode", use_container_width=True)
 
        st.markdown("</div>", unsafe_allow_html=True)
 
    with col_result:
        if generate_btn:
            if not kode_barcode or not nama_barcode:
                st.warning("⚠️ Isi nama dan kode barcode terlebih dahulu!")
            else:
                try:
                    barcode_class = barcode.get_barcode_class(tipe_barcode)
 
                    # Sesuaikan panjang kode jika perlu
                    if tipe_barcode == "ean13" and len(kode_barcode) < 12:
                        kode_barcode = kode_barcode.zfill(12)
                    elif tipe_barcode == "ean8" and len(kode_barcode) < 7:
                        kode_barcode = kode_barcode.zfill(7)
                    elif tipe_barcode == "upca" and len(kode_barcode) < 11:
                        kode_barcode = kode_barcode.zfill(11)
 
                    options = {
                        "module_height": 15.0,
                        "text_distance": 5.0,
                        "font_size": 10,
                        "quiet_zone": 6.5,
                        "write_text": True,
                    }
 
                    generated = barcode_class(
                        kode_barcode,
                        writer=ImageWriter()
                    )
 
                    safe_name = nama_barcode.replace(" ", "_")
                    filename = f"/tmp/{safe_name}_barcode"
                    saved = generated.save(filename, options=options)
 
                    st.markdown(f"""
                    <div class='result-box'>
                        <div class='result-label'>✅ Barcode Berhasil Dibuat!</div>
                        <div style='font-size:22px; font-weight:800; 
                                    color:#2d2013; margin-bottom:4px;'>
                            {nama_barcode}
                        </div>
                        <div style='font-family: monospace; font-size:14px; 
                                    color:#888; margin-bottom:16px;'>
                            {tipe_barcode.upper()} · {kode_barcode}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
 
                    st.image(saved, use_container_width=True)
 
                    with open(saved, "rb") as f:
                        st.download_button(
                            label=f"⬇️ Download {nama_barcode}_barcode.png",
                            data=f,
                            file_name=f"{safe_name}_barcode.png",
                            mime="image/png",
                            use_container_width=True
                        )
 
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info(
                        "💡 Tips: Untuk EAN-13 gunakan 12 angka, "
                        "EAN-8 gunakan 7 angka, UPC-A gunakan 11 angka."
                    )
        else:
            st.markdown("""
            <div class='result-box' style='min-height: 320px; 
                display:flex; flex-direction:column; 
                align-items:center; justify-content:center;'>
                <div style='font-size:72px; margin-bottom:16px;'>🏷️</div>
                <div style='font-size:18px; font-weight:700; color:#aaa;'>
                    Barcode akan tampil di sini
                </div>
                <div style='font-size:13px; color:#ccc; margin-top:8px;'>
                    Isi form dan klik Generate
                </div>
            </div>
            """, unsafe_allow_html=True)
 
# ==========================================
# QRIS GENERATOR
# ==========================================
 
elif menu == "💳 Generator QRIS":
 
    st.markdown("""
    <div class='gen-title'>💳 Generator QRIS</div>
    <div class='gen-desc'>
        Buat QR Code pembayaran digital untuk produk snack kamu secara instan!
    </div>
    """, unsafe_allow_html=True)
 
    col_form, col_result = st.columns([1, 1], gap="large")
 
    with col_form:
        st.markdown("<div class='gen-card'>", unsafe_allow_html=True)
        st.markdown("**⚙️ Konfigurasi QRIS**")
        st.markdown("<br>", unsafe_allow_html=True)
 
        # Mode input
        mode_qris = st.radio(
            "Mode Input",
            ["📦 Pilih dari Produk", "✏️ Input Manual"],
            horizontal=True,
            key="mode_qris"
        )
 
        if mode_qris == "📦 Pilih dari Produk":
            nama_list_qris = [p["Nama"] for p in products]
            pilihan_qris = st.selectbox(
                "Pilih Produk",
                nama_list_qris,
                key="pilih_produk_qris"
            )
            produk_qris = next(
                (p for p in products if p["Nama"] == pilihan_qris), None
            )
            nama_produk = produk_qris["Nama"]
            harga_produk = hitung_harga_diskon(
                produk_qris["Harga"], produk_qris["Diskon"]
            )
            kode_produk = produk_qris["Barcode"]
 
            st.info(
                f"💰 Harga setelah diskon: "
                f"**{format_rupiah(harga_produk)}** "
                f"(hemat {produk_qris['Diskon']}%)"
            )
        else:
            nama_produk = st.text_input(
                "Nama Produk",
                placeholder="Contoh: Paket Snack 3 Pcs",
                key="nama_qris_manual"
            )
            harga_produk = st.number_input(
                "Harga Produk (Rp)",
                min_value=0,
                step=500,
                value=10000
            )
            kode_produk = st.text_input(
                "Kode Produk",
                placeholder="Contoh: SC-001",
                key="kode_qris_manual"
            )
 
        st.markdown("<br>", unsafe_allow_html=True)
 
        # Opsi tampilan
        jumlah = st.number_input(
            "Jumlah Beli",
            min_value=1,
            max_value=100,
            value=1
        )
 
        nama_toko = st.text_input(
            "Nama Toko / Nama Penerima",
            value="Snack Cecilia",
            placeholder="Nama pemilik rekening"
        )
 
        catatan = st.text_area(
            "Catatan (opsional)",
            placeholder="Contoh: Terima kasih sudah berbelanja!",
            height=80
        )
 
        warna_qr = st.color_picker(
            "🎨 Warna QR Code",
            "#ff6b35"
        )
 
        generate_qris_btn = st.button(
            "🎯 Generate QRIS",
            use_container_width=True
        )
 
        st.markdown("</div>", unsafe_allow_html=True)
 
    with col_result:
        if generate_qris_btn:
            if not nama_produk or not kode_produk:
                st.warning("⚠️ Isi nama dan kode produk terlebih dahulu!")
            else:
                total_bayar = harga_produk * jumlah
 
                # Build QR data string
                data_qr = (
                    f"SNACK CECILIA\n"
                    f"================================\n"
                    f"Toko     : {nama_toko}\n"
                    f"Produk   : {nama_produk}\n"
                    f"Kode     : {kode_produk}\n"
                    f"Qty      : {jumlah} pcs\n"
                    f"Harga    : {format_rupiah(harga_produk)}\n"
                    f"TOTAL    : {format_rupiah(total_bayar)}\n"
                    f"================================\n"
                )
 
                if catatan:
                    data_qr += f"Catatan  : {catatan}\n"
 
                data_qr += f"Waktu    : {datetime.now().strftime('%d/%m/%Y %H:%M')}"
 
                # Generate QR
                qr = qrcode.QRCode(
                    version=2,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=4
                )
                qr.add_data(data_qr)
                qr.make(fit=True)
 
                # Konversi warna hex ke RGB
                def hex_to_rgb(hex_color):
                    hex_color = hex_color.lstrip("#")
                    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
 
                fill_rgb = hex_to_rgb(warna_qr)
 
                img_qr = qr.make_image(
                    fill_color=fill_rgb,
                    back_color="white"
                )
 
                buffer = BytesIO()
                img_qr.save(buffer, format="PNG")
                buffer.seek(0)
 
                # Summary info
                st.markdown(f"""
                <div class='result-box'>
                    <div class='result-label'>✅ QRIS Berhasil Dibuat!</div>
                    <div style='font-size:22px; font-weight:800; 
                                color:#2d2013; margin-bottom:4px;'>
                        {nama_produk}
                    </div>
                    <div style='display:flex; justify-content:center; 
                                gap:16px; flex-wrap:wrap; margin-bottom:12px;'>
                        <div style='background:#fff0e6; border-radius:12px; 
                                    padding:8px 16px;'>
                            <div style='font-size:11px; color:#888; font-weight:700;'>
                                HARGA SATUAN
                            </div>
                            <div style='font-size:16px; font-weight:800; 
                                        color:#ff6b35;'>
                                {format_rupiah(harga_produk)}
                            </div>
                        </div>
                        <div style='background:#fff0e6; border-radius:12px; 
                                    padding:8px 16px;'>
                            <div style='font-size:11px; color:#888; font-weight:700;'>
                                QTY
                            </div>
                            <div style='font-size:16px; font-weight:800; color:#ff6b35;'>
                                {jumlah} pcs
                            </div>
                        </div>
                        <div style='background:linear-gradient(135deg,#ff6b35,#ff4500); 
                                    border-radius:12px; padding:8px 16px;'>
                            <div style='font-size:11px; color:rgba(255,255,255,0.8); 
                                        font-weight:700;'>
                                TOTAL BAYAR
                            </div>
                            <div style='font-size:16px; font-weight:800; color:white;'>
                                {format_rupiah(total_bayar)}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
 
                # Tampilkan QR Code
                st.image(buffer, use_container_width=True)
 
                # Reset buffer untuk download
                buffer.seek(0)
                safe_nama = nama_produk.replace(" ", "_")
                st.download_button(
                    label=f"⬇️ Download QRIS {nama_produk}.png",
                    data=buffer,
                    file_name=f"QRIS_{safe_nama}.png",
                    mime="image/png",
                    use_container_width=True
                )
 
                # Info scan
                st.markdown("""
                <div style='background:#f8f9fa; border-radius:14px; 
                            padding:14px; margin-top:12px; text-align:center;'>
                    <div style='font-size:13px; color:#888; font-weight:600;'>
                        📱 Scan QR Code ini dengan aplikasi dompet digital
                        <br>(GoPay, OVO, Dana, ShopeePay, dll)
                    </div>
                </div>
                """, unsafe_allow_html=True)
 
        else:
            st.markdown("""
            <div class='result-box' style='min-height: 420px; 
                display:flex; flex-direction:column; 
                align-items:center; justify-content:center;'>
                <div style='font-size:72px; margin-bottom:16px;'>💳</div>
                <div style='font-size:18px; font-weight:700; color:#aaa;'>
                    QRIS akan tampil di sini
                </div>
                <div style='font-size:13px; color:#ccc; margin-top:8px;'>
                    Isi form dan klik Generate
                </div>
            </div>
            """, unsafe_allow_html=True)
 
