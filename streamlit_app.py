import streamlit as st
import json
import os
import random
import string
import datetime
import hashlib
import qrcode
import io
import base64
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
 
# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SnackStore – Camilan Nusantara",
    page_icon="🍟",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');
 
:root {
    --cream: #FFF8F0;
    --warm: #F5ECD7;
    --amber: #D4821A;
    --amber-dark: #A85F0A;
    --brown: #3D2B1F;
    --sage: #6B7C5E;
    --blush: #E8C4A0;
    --card-bg: #FFFDF9;
    --shadow: 0 4px 24px rgba(61,43,31,0.10);
    --shadow-hover: 0 12px 40px rgba(61,43,31,0.18);
}
 
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream) !important;
    color: var(--brown);
}
 
/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #3D2B1F 0%, #5C3D28 60%, #7A5235 100%) !important;
    border-right: none;
}
[data-testid="stSidebar"] * { color: #F5ECD7 !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio label { color: #F5ECD7 !important; }
[data-testid="stSidebar"] hr { border-color: rgba(245,236,215,0.2) !important; }
 
/* Hero */
.hero-banner {
    background: linear-gradient(135deg, #3D2B1F 0%, #7A5235 50%, #D4821A 100%);
    border-radius: 20px;
    padding: 48px 40px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    color: white;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: rgba(255,255,255,0.07);
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 30%;
    width: 300px; height: 300px;
    border-radius: 50%;
    background: rgba(255,255,255,0.04);
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 900;
    line-height: 1.1;
    margin: 0 0 10px;
}
.hero-sub {
    font-size: 1.05rem;
    opacity: 0.85;
    margin: 0 0 20px;
}
.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 50px;
    padding: 6px 18px;
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    backdrop-filter: blur(4px);
}
 
/* Product Cards */
.product-card {
    background: var(--card-bg);
    border-radius: 16px;
    border: 1.5px solid var(--blush);
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}
.product-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--amber), var(--blush));
}
.product-card:hover {
    box-shadow: var(--shadow-hover);
    border-color: var(--amber);
    transform: translateY(-2px);
}
.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--brown);
    margin: 0 0 4px;
}
.product-price {
    font-size: 1.3rem;
    font-weight: 600;
    color: var(--amber);
    margin: 4px 0;
}
.product-tag {
    display: inline-block;
    background: var(--warm);
    color: var(--sage);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.78rem;
    font-weight: 500;
    margin: 2px;
}
 
/* Star Rating */
.star-rating { font-size: 1.4rem; cursor: pointer; }
.star-filled { color: #F5A623; }
.star-empty { color: #DDD; }
 
/* Review Card */
.review-card {
    background: var(--warm);
    border-left: 4px solid var(--amber);
    border-radius: 0 12px 12px 0;
    padding: 14px 18px;
    margin: 10px 0;
}
.review-author { font-weight: 600; color: var(--brown); }
.review-text { color: #6B5B50; font-size: 0.95rem; margin-top: 4px; }
 
/* Section Headers */
.section-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--brown);
    margin: 32px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 2px;
    background: linear-gradient(90deg, var(--blush), transparent);
    margin-left: 8px;
}
 
/* Info Row */
.info-row {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px dashed var(--blush);
    font-size: 0.92rem;
}
.info-label { color: var(--sage); font-weight: 500; }
.info-value { color: var(--brown); font-weight: 600; }
 
/* WhatsApp Button */
.wa-btn {
    display: inline-block;
    background: #25D366;
    color: white !important;
    padding: 10px 22px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none;
    margin-top: 12px;
    box-shadow: 0 4px 14px rgba(37,211,102,0.35);
}
.wa-btn:hover { background: #1ebe58; }
 
/* Metrics */
.metric-card {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 20px;
    border: 1.5px solid var(--blush);
    text-align: center;
    box-shadow: var(--shadow);
}
.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--amber);
}
.metric-label { font-size: 0.85rem; color: var(--sage); margin-top: 4px; }
 
/* Seller Panel */
.seller-panel {
    background: linear-gradient(135deg, #3D2B1F, #5C3D28);
    border-radius: 16px;
    padding: 24px;
    color: #F5ECD7;
    margin-bottom: 20px;
}
.seller-panel h3 { font-family: 'Playfair Display', serif; font-size: 1.4rem; margin: 0 0 8px; }
 
/* Alert boxes */
.alert-success {
    background: #E8F5E9;
    border: 1.5px solid #81C784;
    border-radius: 10px;
    padding: 12px 18px;
    color: #2E7D32;
    font-weight: 500;
}
.alert-warning {
    background: #FFF3E0;
    border: 1.5px solid #FFB74D;
    border-radius: 10px;
    padding: 12px 18px;
    color: #E65100;
    font-weight: 500;
}
 
/* Divider */
.fancy-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--blush), transparent);
    margin: 32px 0;
    border: none;
}
 
/* QRIS Card */
.qris-card {
    background: white;
    border: 3px solid var(--amber);
    border-radius: 20px;
    padding: 28px;
    text-align: center;
    box-shadow: var(--shadow-hover);
}
 
/* Projection Preview */
.phone-frame {
    border: 6px solid #1A1A1A;
    border-radius: 36px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    width: 280px;
    margin: 0 auto;
}
.phone-screen {
    background: var(--cream);
    min-height: 500px;
    padding: 16px;
}
.phone-notch {
    background: #1A1A1A;
    height: 28px;
    border-radius: 0 0 16px 16px;
    width: 100px;
    margin: 0 auto 12px;
}
</style>
""", unsafe_allow_html=True)
 
# ─── Data Storage ───────────────────────────────────────────────────────────────
DATA_FILE = "snackstore_data.json"
SELLER_PASSWORD = "seller123"  # Change this
 
def load_data():
    default = {
        "products": [
            {"id": "p001", "name": "Keripik Tempe", "price": 15000, "weight": "150g",
             "expired": "2025-12-31", "barcode": "123456789012", "whatsapp": "6281234567890",
             "description": "Keripik tempe renyah khas Jawa, bumbu gurih original.", "stock": 50},
            {"id": "p002", "name": "Keripik Talas", "price": 18000, "weight": "130g",
             "expired": "2025-11-30", "barcode": "123456789013", "whatsapp": "6281234567890",
             "description": "Talas pilihan digoreng renyah, cocok untuk camilan keluarga.", "stock": 35},
            {"id": "p003", "name": "Stick Talas", "price": 16000, "weight": "120g",
             "expired": "2025-10-31", "barcode": "123456789014", "whatsapp": "6281234567890",
             "description": "Stick talas tipis renyah dengan taburan bumbu spesial.", "stock": 42},
            {"id": "p004", "name": "Telur Gabus Keju", "price": 22000, "weight": "100g",
             "expired": "2025-09-30", "barcode": "123456789015", "whatsapp": "6281234567890",
             "description": "Telur gabus lembut dengan keju premium, meleleh di mulut.", "stock": 28},
            {"id": "p005", "name": "Keripik Singkong", "price": 12000, "weight": "200g",
             "expired": "2026-01-31", "barcode": "123456789016", "whatsapp": "6281234567890",
             "description": "Singkong segar digoreng crispy, camilan tradisional favorit.", "stock": 60},
            {"id": "p006", "name": "Kacang Bogor", "price": 20000, "weight": "250g",
             "expired": "2025-12-15", "barcode": "123456789017", "whatsapp": "6281234567890",
             "description": "Kacang bogor asli pilihan, diproses higienis tanpa pengawet.", "stock": 45},
            {"id": "p007", "name": "Kacang Bandung", "price": 18000, "weight": "200g",
             "expired": "2025-11-15", "barcode": "123456789018", "whatsapp": "6281234567890",
             "description": "Kacang oven khas Bandung, renyah gurih dengan bumbu spesial.", "stock": 38},
            {"id": "p008", "name": "Kacang Koro", "price": 14000, "weight": "180g",
             "expired": "2025-10-15", "barcode": "123456789019", "whatsapp": "6281234567890",
             "description": "Kacang koro rendah kalori, sumber protein nabati pilihan.", "stock": 25},
            {"id": "p009", "name": "Kue Kering", "price": 35000, "weight": "300g",
             "expired": "2025-08-31", "barcode": "123456789020", "whatsapp": "6281234567890",
             "description": "Aneka kue kering premium, cocok untuk hantaran dan oleh-oleh.", "stock": 20},
        ],
        "reviews": [],
        "sales": [],
        "qris_number": "000201...",  # placeholder
        "expenses": [
            {"date": "2024-01-01", "category": "Bahan Baku", "amount": 500000, "note": "Beli tepung & kacang"},
            {"date": "2024-01-05", "category": "Operasional", "amount": 150000, "note": "Gas & listrik"},
        ]
    }
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                stored = json.load(f)
                for k in default:
                    if k not in stored:
                        stored[k] = default[k]
                return stored
        except:
            pass
    return default
 
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
 
def generate_barcode_image(barcode_num):
    """Generate EAN-13 barcode image"""
    try:
        buf = io.BytesIO()
        barcode_num_12 = str(barcode_num)[:12].zfill(12)
        ean = EAN13(barcode_num_12, writer=ImageWriter())
        ean.write(buf)
        buf.seek(0)
        return buf
    except Exception as e:
        return None
 
def generate_qr_code(data_str, size=200):
    """Generate QR code"""
    qr = qrcode.QRCode(version=1, box_size=4, border=2)
    qr.add_data(data_str)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#3D2B1F", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf
 
def img_to_base64(buf):
    return base64.b64encode(buf.getvalue()).decode()
 
def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")
 
def render_stars(rating, key_suffix=""):
    stars = ""
    for i in range(1, 6):
        stars += "⭐" if i <= rating else "☆"
    return stars
 
# ─── Initialize ────────────────────────────────────────────────────────────────
data = load_data()
 
# ─── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 20px 0 10px; text-align: center;'>
        <div style='font-family: Playfair Display, serif; font-size: 1.5rem; font-weight: 900; color: #F5ECD7;'>🍟 SnackStore</div>
        <div style='font-size: 0.8rem; color: #C4A882; margin-top: 4px;'>Camilan Nusantara</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
 
    page = st.radio(
        "Navigasi",
        ["🏠 Beranda Produk", "🔐 Panel Penjual", "📦 Generator Barcode", "💳 QRIS & Pembayaran", "📊 Laporan & Analitik", "📱 Preview Tampilan"],
        label_visibility="collapsed"
    )
 
    st.markdown("---")
    st.markdown("<div style='font-size:0.78rem; color:#C4A882; text-align:center;'>© 2024 SnackStore</div>", unsafe_allow_html=True)
 
SELLER_PAGES = ["🔐 Panel Penjual", "📦 Generator Barcode", "💳 QRIS & Pembayaran", "📊 Laporan & Analitik"]
 
# ─── Auth Check for Seller Pages ───────────────────────────────────────────────
def seller_auth():
    if "seller_logged_in" not in st.session_state:
        st.session_state.seller_logged_in = False
    if not st.session_state.seller_logged_in:
        st.markdown('<div class="seller-panel"><h3>🔐 Login Penjual</h3><p style="opacity:0.8;font-size:0.9rem;">Halaman ini hanya untuk penjual.</p></div>', unsafe_allow_html=True)
        pwd = st.text_input("Password Penjual", type="password", placeholder="Masukkan password...")
        if st.button("🔓 Login", use_container_width=True):
            if pwd == SELLER_PASSWORD:
                st.session_state.seller_logged_in = True
                st.rerun()
            else:
                st.error("Password salah!")
        return False
    return True
 
# ════════════════════════════════════════════════════════════════════════════════
# PAGE 1 – BERANDA PRODUK
# ════════════════════════════════════════════════════════════════════════════════
if page == "🏠 Beranda Produk":
    # Hero
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">Camilan Nusantara<br>Terbaik & Terpercaya 🌟</div>
        <div class="hero-sub">Produk camilan tradisional berkualitas tinggi, dibuat dengan cinta dari bahan pilihan.</div>
        <span class="hero-badge">🚚 Pengiriman ke seluruh Indonesia</span>
        &nbsp;
        <span class="hero-badge">✅ Tanpa Pengawet Berbahaya</span>
    </div>
    """, unsafe_allow_html=True)
 
    # Search & Filter
    col_s, col_f = st.columns([3, 1])
    with col_s:
        search = st.text_input("🔍 Cari produk...", placeholder="Ketik nama produk...", label_visibility="collapsed")
    with col_f:
        sort_by = st.selectbox("Urutkan", ["Nama A-Z", "Harga Termurah", "Harga Termahal"], label_visibility="collapsed")
 
    products = data["products"]
    if search:
        products = [p for p in products if search.lower() in p["name"].lower()]
    if sort_by == "Harga Termurah":
        products = sorted(products, key=lambda x: x["price"])
    elif sort_by == "Harga Termahal":
        products = sorted(products, key=lambda x: x["price"], reverse=True)
    else:
        products = sorted(products, key=lambda x: x["name"])
 
    st.markdown(f'<div class="section-header">🛒 Produk Kami <span style="font-size:1rem;font-weight:400;color:#6B7C5E;">({len(products)} produk)</span></div>', unsafe_allow_html=True)
 
    # Product Grid
    cols = st.columns(3)
    for idx, prod in enumerate(products):
        with cols[idx % 3]:
            # Calculate avg rating
            prod_reviews = [r for r in data["reviews"] if r.get("product_id") == prod["id"]]
            avg_rating = round(sum(r["rating"] for r in prod_reviews) / len(prod_reviews), 1) if prod_reviews else 0
            star_display = "⭐" * int(avg_rating) + f" {avg_rating}" if avg_rating > 0 else "Belum ada ulasan"
 
            exp_date = datetime.datetime.strptime(prod["expired"], "%Y-%m-%d").date()
            days_left = (exp_date - datetime.date.today()).days
            exp_color = "#E53935" if days_left < 30 else ("#FB8C00" if days_left < 90 else "#43A047")
            exp_label = "⚠️ Segera Exp!" if days_left < 30 else f"Exp: {prod['expired']}"
 
            with st.expander(f"**{prod['name']}** — {format_rupiah(prod['price'])}", expanded=False):
                st.markdown(f"""
                <div style='margin-bottom:12px;'>
                    <div class="product-name">{prod['name']}</div>
                    <div class="product-price">{format_rupiah(prod['price'])}</div>
                    <span class="product-tag">⚖️ {prod['weight']}</span>
                    <span class="product-tag">📦 Stok: {prod.get('stock', '-')}</span>
                    <span class="product-tag" style='color:{exp_color};'>{exp_label}</span>
                </div>
                """, unsafe_allow_html=True)
 
                st.markdown(f"_{prod.get('description', '')}_")
                st.markdown('<div class="fancy-divider" style="margin:12px 0;"></div>', unsafe_allow_html=True)
 
                st.markdown(f"""
                <div class="info-row"><span class="info-label">Barcode</span><span class="info-value">🔢 {prod['barcode']}</span></div>
                <div class="info-row"><span class="info-label">Tanggal Kadaluarsa</span><span class="info-value" style='color:{exp_color};'>{prod['expired']}</span></div>
                <div class="info-row"><span class="info-label">Berat</span><span class="info-value">{prod['weight']}</span></div>
                <div class="info-row"><span class="info-label">Rating</span><span class="info-value">{star_display}</span></div>
                <div class="info-row"><span class="info-label">Jumlah Ulasan</span><span class="info-value">{len(prod_reviews)} ulasan</span></div>
                """, unsafe_allow_html=True)
 
                # Barcode Image
                bc_buf = generate_barcode_image(prod["barcode"])
                if bc_buf:
                    st.image(bc_buf, caption=f"Barcode: {prod['barcode']}", use_container_width=True)
 
                # WhatsApp
                wa_msg = f"Halo, saya tertarik membeli *{prod['name']}* seharga {format_rupiah(prod['price'])}. Apakah masih tersedia?"
                wa_url = f"https://wa.me/{prod['whatsapp']}?text={wa_msg.replace(' ', '%20').replace('*', '%2A')}"
                st.markdown(f'<a href="{wa_url}" target="_blank" class="wa-btn">💬 Pesan via WhatsApp</a>', unsafe_allow_html=True)
 
    # ── Review Section ─────────────────────────────────────────────────────────
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⭐ Ulasan & Penilaian Pelanggan</div>', unsafe_allow_html=True)
 
    col_left, col_right = st.columns([1, 1])
    with col_left:
        st.markdown("#### Tulis Ulasan")
        with st.form("review_form", clear_on_submit=True):
            reviewer_name = st.text_input("Nama Kamu", placeholder="Misal: Budi Santoso")
            product_choice = st.selectbox("Produk yang Dinilai", [p["name"] for p in data["products"]])
            rating = st.select_slider("Rating", options=[1, 2, 3, 4, 5], value=5, format_func=lambda x: "⭐" * x)
            comment = st.text_area("Komentar", placeholder="Ceritakan pengalaman kamu...", height=100)
            submitted = st.form_submit_button("📤 Kirim Ulasan", use_container_width=True)
            if submitted:
                if reviewer_name and comment:
                    prod_obj = next((p for p in data["products"] if p["name"] == product_choice), None)
                    data["reviews"].append({
                        "id": hashlib.md5(f"{reviewer_name}{datetime.datetime.now()}".encode()).hexdigest()[:8],
                        "product_id": prod_obj["id"] if prod_obj else "",
                        "product_name": product_choice,
                        "reviewer": reviewer_name,
                        "rating": rating,
                        "comment": comment,
                        "date": str(datetime.date.today())
                    })
                    save_data(data)
                    st.markdown('<div class="alert-success">✅ Ulasan kamu berhasil dikirim! Terima kasih 😊</div>', unsafe_allow_html=True)
                    st.rerun()
                else:
                    st.warning("Lengkapi nama dan komentar ya!")
 
    with col_right:
        st.markdown("#### Ulasan Terbaru")
        all_reviews = sorted(data["reviews"], key=lambda x: x.get("date", ""), reverse=True)
        if not all_reviews:
            st.info("Belum ada ulasan. Jadilah yang pertama! 🌟")
        for rev in all_reviews[:8]:
            st.markdown(f"""
            <div class="review-card">
                <div class="review-author">{'⭐' * rev['rating']} &nbsp; {rev['reviewer']}</div>
                <div style='font-size:0.78rem; color:#9E8878; margin:2px 0;'>{rev['product_name']} · {rev.get('date','')}</div>
                <div class="review-text">{rev['comment']}</div>
            </div>
            """, unsafe_allow_html=True)
 
# ════════════════════════════════════════════════════════════════════════════════
# PAGE 2 – PANEL PENJUAL
# ════════════════════════════════════════════════════════════════════════════════
elif page == "🔐 Panel Penjual":
    if not seller_auth():
        st.stop()
 
    st.markdown('<div class="section-header">🔐 Panel Manajemen Penjual</div>', unsafe_allow_html=True)
 
    if st.button("🚪 Logout"):
        st.session_state.seller_logged_in = False
        st.rerun()
 
    # Stats
    total_revenue = sum(s.get("total", 0) for s in data["sales"])
    total_orders = len(data["sales"])
    total_products = len(data["products"])
 
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{format_rupiah(total_revenue)}</div><div class="metric-label">Total Pendapatan</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_orders}</div><div class="metric-label">Total Pesanan</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">{total_products}</div><div class="metric-label">Produk Aktif</div></div>', unsafe_allow_html=True)
    with c4:
        avg_r = round(sum(r["rating"] for r in data["reviews"]) / len(data["reviews"]), 1) if data["reviews"] else 0
        st.markdown(f'<div class="metric-card"><div class="metric-value">{avg_r} ⭐</div><div class="metric-label">Rata-rata Rating</div></div>', unsafe_allow_html=True)
 
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
 
    # Manage Products
    tab1, tab2 = st.tabs(["✏️ Edit Produk", "➕ Tambah Produk Baru"])
    with tab1:
        prod_names = [p["name"] for p in data["products"]]
        selected_prod_name = st.selectbox("Pilih Produk untuk Diedit", prod_names)
        prod_to_edit = next((p for p in data["products"] if p["name"] == selected_prod_name), None)
        if prod_to_edit:
            with st.form("edit_product"):
                cols = st.columns(2)
                with cols[0]:
                    new_name = st.text_input("Nama Produk", value=prod_to_edit["name"])
                    new_price = st.number_input("Harga (Rp)", value=prod_to_edit["price"], step=1000)
                    new_weight = st.text_input("Berat", value=prod_to_edit["weight"])
                    new_stock = st.number_input("Stok", value=prod_to_edit.get("stock", 0), step=1)
                with cols[1]:
                    new_expired = st.text_input("Expired (YYYY-MM-DD)", value=prod_to_edit["expired"])
                    new_barcode = st.text_input("Barcode (12 digit)", value=prod_to_edit["barcode"])
                    new_wa = st.text_input("WhatsApp (62xxx)", value=prod_to_edit["whatsapp"])
                new_desc = st.text_area("Deskripsi", value=prod_to_edit.get("description", ""))
                if st.form_submit_button("💾 Simpan Perubahan", use_container_width=True):
                    prod_to_edit.update({"name": new_name, "price": new_price, "weight": new_weight,
                                         "stock": new_stock, "expired": new_expired, "barcode": new_barcode,
                                         "whatsapp": new_wa, "description": new_desc})
                    save_data(data)
                    st.success("✅ Produk berhasil diperbarui!")
                    st.rerun()
 
    with tab2:
        with st.form("add_product"):
            cols = st.columns(2)
            with cols[0]:
                ap_name = st.text_input("Nama Produk")
                ap_price = st.number_input("Harga (Rp)", value=10000, step=1000)
                ap_weight = st.text_input("Berat", value="100g")
                ap_stock = st.number_input("Stok", value=20, step=1)
            with cols[1]:
                ap_expired = st.text_input("Expired (YYYY-MM-DD)", value=str(datetime.date.today() + datetime.timedelta(days=180)))
                ap_barcode = st.text_input("Barcode (12 digit - isi atau otomatis)")
                ap_wa = st.text_input("WhatsApp (62xxx)", value="6281234567890")
            ap_desc = st.text_area("Deskripsi Produk")
            auto_bc = st.checkbox("🔄 Generate barcode otomatis", value=True)
            if st.form_submit_button("➕ Tambah Produk", use_container_width=True):
                if ap_name:
                    bc_val = ap_barcode[:12].zfill(12) if ap_barcode and not auto_bc else ''.join([str(random.randint(0,9)) for _ in range(12)])
                    new_prod = {
                        "id": f"p{len(data['products'])+1:03d}",
                        "name": ap_name, "price": ap_price, "weight": ap_weight,
                        "stock": ap_stock, "expired": ap_expired, "barcode": bc_val,
                        "whatsapp": ap_wa, "description": ap_desc
                    }
                    data["products"].append(new_prod)
                    save_data(data)
                    st.success(f"✅ Produk '{ap_name}' berhasil ditambahkan dengan barcode: {bc_val}")
                    st.rerun()
                else:
                    st.warning("Nama produk wajib diisi!")
 
# ════════════════════════════════════════════════════════════════════════════════
# PAGE 3 – GENERATOR BARCODE
# ════════════════════════════════════════════════════════════════════════════════
elif page == "📦 Generator Barcode":
    if not seller_auth():
        st.stop()
 
    st.markdown('<div class="section-header">📦 Generator Barcode Produk</div>', unsafe_allow_html=True)
    st.markdown("Buat barcode EAN-13 (12 digit + 1 digit cek otomatis) untuk produk baru atau yang sudah ada.")
 
    tab_auto, tab_manual, tab_existing = st.tabs(["🤖 Otomatis", "✍️ Manual", "📋 Produk Existing"])
 
    with tab_auto:
        st.markdown("#### Generate Barcode Otomatis")
        col1, col2 = st.columns(2)
        with col1:
            prefix = st.text_input("Prefix (opsional, maks 6 digit)", value="899", max_chars=6)
            prod_name_auto = st.text_input("Nama Produk (untuk label)")
        with col2:
            qty = st.number_input("Jumlah barcode yang digenerate", min_value=1, max_value=20, value=1)
 
        if st.button("🎲 Generate Sekarang", use_container_width=True):
            generated = []
            for i in range(int(qty)):
                rand_part = ''.join([str(random.randint(0,9)) for _ in range(12 - len(prefix))])
                bc_12 = (prefix + rand_part)[:12]
                generated.append(bc_12)
 
            for bc in generated:
                col_bc, col_img = st.columns([1, 2])
                with col_bc:
                    st.markdown(f"""
                    <div class='metric-card' style='text-align:left; padding:16px;'>
                        <div style='font-size:0.85rem; color:#6B7C5E;'>Barcode Generated</div>
                        <div style='font-family: monospace; font-size:1.4rem; font-weight:700; color:#D4821A; letter-spacing:2px;'>{bc}</div>
                        <div style='font-size:0.8rem; color:#9E8878; margin-top:4px;'>{prod_name_auto or "Produk Baru"}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with col_img:
                    buf = generate_barcode_image(bc)
                    if buf:
                        st.image(buf, caption=f"EAN-13: {bc}", use_container_width=True)
 
    with tab_manual:
        st.markdown("#### Input Barcode Manual")
        with st.form("manual_barcode"):
            manual_bc = st.text_input("Nomor Barcode (tepat 12 digit)", max_chars=12, placeholder="Contoh: 899300012345")
            manual_prod = st.text_input("Nama Produk")
            manual_price = st.number_input("Harga (Rp)", value=15000, step=1000)
            manual_weight = st.text_input("Berat", value="150g")
            manual_expired = st.text_input("Expired (YYYY-MM-DD)", value="2025-12-31")
            manual_wa = st.text_input("WhatsApp (62xxx)", value="6281234567890")
            manual_desc = st.text_area("Deskripsi")
            save_new = st.checkbox("💾 Simpan ke database produk")
 
            if st.form_submit_button("🔢 Generate Barcode", use_container_width=True):
                if len(manual_bc) == 12 and manual_bc.isdigit():
                    buf = generate_barcode_image(manual_bc)
                    if buf:
                        st.image(buf, caption=f"EAN-13: {manual_bc}", width=400)
                        st.download_button("⬇️ Download Barcode", data=buf.getvalue(), file_name=f"barcode_{manual_bc}.png", mime="image/png")
                    if save_new and manual_prod:
                        new_p = {
                            "id": f"p{len(data['products'])+1:03d}",
                            "name": manual_prod, "price": manual_price, "weight": manual_weight,
                            "stock": 0, "expired": manual_expired, "barcode": manual_bc,
                            "whatsapp": manual_wa, "description": manual_desc
                        }
                        data["products"].append(new_p)
                        save_data(data)
                        st.success(f"✅ Produk '{manual_prod}' disimpan!")
                else:
                    st.error("❌ Barcode harus tepat 12 digit angka!")
 
    with tab_existing:
        st.markdown("#### Cetak Barcode Produk yang Ada")
        for prod in data["products"]:
            with st.expander(f"🏷️ {prod['name']} — {prod['barcode']}"):
                col_i, col_d = st.columns([2, 1])
                with col_i:
                    buf = generate_barcode_image(prod["barcode"])
                    if buf:
                        st.image(buf, use_container_width=True)
                        dl_buf = generate_barcode_image(prod["barcode"])
                        st.download_button(f"⬇️ Download", data=dl_buf.getvalue(), file_name=f"barcode_{prod['name']}.png", mime="image/png", key=f"dl_{prod['id']}")
                with col_d:
                    st.markdown(f"""
                    <div class="info-row"><span class="info-label">Produk</span><span class="info-value">{prod['name']}</span></div>
                    <div class="info-row"><span class="info-label">Barcode</span><span class="info-value">{prod['barcode']}</span></div>
                    <div class="info-row"><span class="info-label">Harga</span><span class="info-value">{format_rupiah(prod['price'])}</span></div>
                    <div class="info-row"><span class="info-label">Expired</span><span class="info-value">{prod['expired']}</span></div>
                    """, unsafe_allow_html=True)
 
# ════════════════════════════════════════════════════════════════════════════════
# PAGE 4 – QRIS & PEMBAYARAN
# ════════════════════════════════════════════════════════════════════════════════
elif page == "💳 QRIS & Pembayaran":
    if not seller_auth():
        st.stop()
 
    st.markdown('<div class="section-header">💳 QRIS & Manajemen Pembayaran</div>', unsafe_allow_html=True)
 
    tab_qris, tab_order = st.tabs(["🔲 Generate QRIS", "📝 Catat Penjualan Manual"])
 
    with tab_qris:
        col_form, col_preview = st.columns([1, 1])
        with col_form:
            st.markdown("#### Pengaturan QRIS Toko")
            merchant_name = st.text_input("Nama Merchant", value="SnackStore Nusantara")
            merchant_id = st.text_input("Merchant ID / No. QRIS", value="ID1234567890", help="Dari penyedia QRIS Anda")
            merchant_city = st.text_input("Kota", value="Jakarta")
            amount_fixed = st.checkbox("Jumlah Tetap?")
            if amount_fixed:
                qris_amount = st.number_input("Jumlah Pembayaran (Rp)", value=50000, step=1000)
            else:
                qris_amount = 0
 
            gen_qris = st.button("🔲 Generate QRIS Sekarang", use_container_width=True)
 
        with col_preview:
            if gen_qris:
                qris_data = f"Merchant: {merchant_name} | ID: {merchant_id} | Kota: {merchant_city}"
                if qris_amount > 0:
                    qris_data += f" | Amount: {qris_amount}"
 
                buf = generate_qr_code(qris_data)
                st.markdown(f"""
                <div class="qris-card">
                    <div style='font-family: Playfair Display, serif; font-size: 1.2rem; font-weight: 700; color: #3D2B1F; margin-bottom: 12px;'>
                        🏪 {merchant_name}
                    </div>
                """, unsafe_allow_html=True)
                st.image(buf, caption="QRIS — Scan untuk Bayar", width=220)
                st.markdown(f"""
                    <div style='background:#FFF3E0; border-radius:8px; padding:10px; margin-top:12px;'>
                        <div style='font-size:0.85rem; color:#7A5235;'>ID: {merchant_id}</div>
                        <div style='font-size:0.85rem; color:#7A5235;'>Kota: {merchant_city}</div>
                        {"<div style='font-size:1rem; font-weight:700; color:#D4821A;'>Rp " + f"{qris_amount:,.0f}".replace(',','.') + "</div>" if qris_amount > 0 else ""}
                    </div>
                </div>
                """, unsafe_allow_html=True)
 
                dl_buf = generate_qr_code(qris_data)
                st.download_button("⬇️ Download QRIS PNG", data=dl_buf.getvalue(), file_name="qris_snackstore.png", mime="image/png")
 
    with tab_order:
        st.markdown("#### Catat Transaksi Penjualan")
        with st.form("add_sale"):
            cols = st.columns(3)
            with cols[0]:
                buyer_name = st.text_input("Nama Pembeli", placeholder="Opsional")
                sale_date = st.date_input("Tanggal Transaksi", value=datetime.date.today())
            with cols[1]:
                sale_product = st.selectbox("Produk", [p["name"] for p in data["products"]])
                qty_sold = st.number_input("Jumlah (pcs)", min_value=1, value=1)
            with cols[2]:
                payment_method = st.selectbox("Metode Bayar", ["QRIS", "Transfer Bank", "Tunai", "COD"])
                discount = st.number_input("Diskon (Rp)", value=0, step=1000)
 
            notes = st.text_area("Catatan", height=60)
            if st.form_submit_button("💾 Simpan Transaksi", use_container_width=True):
                prod_obj = next((p for p in data["products"] if p["name"] == sale_product), None)
                if prod_obj:
                    subtotal = prod_obj["price"] * qty_sold - discount
                    sale_record = {
                        "id": hashlib.md5(f"{buyer_name}{datetime.datetime.now()}".encode()).hexdigest()[:8],
                        "date": str(sale_date),
                        "product": sale_product,
                        "product_id": prod_obj["id"],
                        "qty": qty_sold,
                        "unit_price": prod_obj["price"],
                        "discount": discount,
                        "total": subtotal,
                        "payment": payment_method,
                        "buyer": buyer_name,
                        "notes": notes
                    }
                    data["sales"].append(sale_record)
                    # Update stock
                    prod_obj["stock"] = max(0, prod_obj.get("stock", 0) - qty_sold)
                    save_data(data)
                    st.markdown(f'<div class="alert-success">✅ Transaksi berhasil dicatat! Total: {format_rupiah(subtotal)}</div>', unsafe_allow_html=True)
                    st.rerun()
 
        # Recent transactions
        st.markdown("#### Transaksi Terbaru")
        recent_sales = sorted(data["sales"], key=lambda x: x.get("date", ""), reverse=True)[:10]
        if recent_sales:
            df = pd.DataFrame(recent_sales)[["date", "product", "qty", "total", "payment", "buyer"]]
            df.columns = ["Tanggal", "Produk", "Qty", "Total", "Pembayaran", "Pembeli"]
            df["Total"] = df["Total"].apply(format_rupiah)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Belum ada transaksi dicatat.")
 
# ════════════════════════════════════════════════════════════════════════════════
# PAGE 5 – LAPORAN & ANALITIK
# ════════════════════════════════════════════════════════════════════════════════
elif page == "📊 Laporan & Analitik":
    if not seller_auth():
        st.stop()
 
    st.markdown('<div class="section-header">📊 Laporan & Analitik Bisnis</div>', unsafe_allow_html=True)
 
    # Period filter
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        start_date = st.date_input("Dari Tanggal", value=datetime.date.today() - datetime.timedelta(days=30))
    with col_p2:
        end_date = st.date_input("Sampai Tanggal", value=datetime.date.today())
 
    sales = [s for s in data["sales"] if start_date.strftime("%Y-%m-%d") <= s.get("date","") <= end_date.strftime("%Y-%m-%d")]
    expenses = [e for e in data["expenses"] if start_date.strftime("%Y-%m-%d") <= e.get("date","") <= end_date.strftime("%Y-%m-%d")]
 
    total_revenue = sum(s.get("total", 0) for s in sales)
    total_expense = sum(e.get("amount", 0) for e in expenses)
    gross_profit = total_revenue - total_expense
    profit_margin = (gross_profit / total_revenue * 100) if total_revenue > 0 else 0
 
    # P&L Summary
    st.markdown("### 📋 Laporan Laba Rugi (P&L)")
    cols = st.columns(4)
    metrics = [
        ("💰 Pendapatan", total_revenue, "#43A047"),
        ("📉 Pengeluaran", total_expense, "#E53935"),
        ("📈 Laba Bersih", gross_profit, "#1E88E5" if gross_profit >= 0 else "#E53935"),
        ("📊 Margin", f"{profit_margin:.1f}%", "#FB8C00"),
    ]
    for col, (label, val, color) in zip(cols, metrics):
        with col:
            display = format_rupiah(val) if isinstance(val, (int, float)) else val
            st.markdown(f'<div class="metric-card"><div class="metric-value" style="color:{color};">{display}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)
 
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)
 
    col_chart1, col_chart2 = st.columns(2)
 
    with col_chart1:
        st.markdown("#### 📊 Penjualan per Produk")
        if sales:
            product_sales = {}
            for s in sales:
                product_sales[s["product"]] = product_sales.get(s["product"], 0) + s["total"]
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.patch.set_facecolor('#FFF8F0')
            ax.set_facecolor('#FFF8F0')
            products_sorted = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
            names = [p[0].replace("Keripik ", "Krpk ").replace("Kacang ", "Kcg ") for p, _ in products_sorted]
            values = [v for _, v in products_sorted]
            colors = ['#D4821A', '#A85F0A', '#E8A44A', '#6B7C5E', '#3D2B1F', '#C4A882', '#7A5235', '#F5ECD7', '#9E8878']
            bars = ax.barh(names, values, color=colors[:len(names)])
            ax.set_xlabel("Total Penjualan (Rp)", fontsize=9)
            ax.tick_params(axis='both', labelsize=8)
            for bar, val in zip(bars, values):
                ax.text(bar.get_width() + max(values)*0.01, bar.get_y() + bar.get_height()/2,
                        f'Rp{val//1000}K', va='center', fontsize=7, color='#3D2B1F')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close()
        else:
            st.info("Belum ada data penjualan di periode ini.")
 
    with col_chart2:
        st.markdown("#### 📅 Tren Penjualan Harian")
        if sales:
            daily = {}
            for s in sales:
                d = s.get("date", "")
                daily[d] = daily.get(d, 0) + s["total"]
            dates = sorted(daily.keys())
            values = [daily[d] for d in dates]
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            fig2.patch.set_facecolor('#FFF8F0')
            ax2.set_facecolor('#FFF8F0')
            ax2.plot(range(len(dates)), values, color='#D4821A', linewidth=2.5, marker='o', markersize=5)
            ax2.fill_between(range(len(dates)), values, alpha=0.15, color='#D4821A')
            ax2.set_xticks(range(len(dates)))
            ax2.set_xticklabels([d[5:] for d in dates], rotation=45, fontsize=7)
            ax2.tick_params(axis='y', labelsize=8)
            ax2.set_ylabel("Pendapatan (Rp)", fontsize=9)
            plt.tight_layout()
            st.pyplot(fig2)
            plt.close()
        else:
            st.info("Belum ada data tren penjualan.")
 
    # Add Expense
    st.markdown("### 💸 Tambah Pengeluaran")
    with st.form("add_expense"):
        ce1, ce2, ce3 = st.columns(3)
        with ce1:
            exp_date = st.date_input("Tanggal", value=datetime.date.today())
            exp_cat = st.selectbox("Kategori", ["Bahan Baku", "Operasional", "Kemasan", "Gaji", "Pemasaran", "Lainnya"])
        with ce2:
            exp_amount = st.number_input("Jumlah (Rp)", value=50000, step=5000)
            exp_note = st.text_input("Keterangan")
        with ce3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("➕ Tambah Pengeluaran", use_container_width=True):
                data["expenses"].append({"date": str(exp_date), "category": exp_cat, "amount": exp_amount, "note": exp_note})
                save_data(data)
                st.success("✅ Pengeluaran ditambahkan!")
                st.rerun()
 
    # History Table
    st.markdown("### 📜 History Semua Transaksi")
    if data["sales"]:
        df_all = pd.DataFrame(data["sales"])[["date", "product", "qty", "unit_price", "discount", "total", "payment", "buyer"]]
        df_all.columns = ["Tanggal", "Produk", "Qty", "Harga Satuan", "Diskon", "Total", "Pembayaran", "Pembeli"]
        for col in ["Harga Satuan", "Diskon", "Total"]:
            df_all[col] = df_all[col].apply(format_rupiah)
        st.dataframe(df_all, use_container_width=True, hide_index=True)
 
        # Download
        df_download = pd.DataFrame(data["sales"])
        csv = df_download.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download CSV", data=csv, file_name="laporan_penjualan.csv", mime="text/csv")
    else:
        st.info("Belum ada transaksi yang tercatat.")
 
# ════════════════════════════════════════════════════════════════════════════════
# PAGE 6 – PREVIEW TAMPILAN
# ════════════════════════════════════════════════════════════════════════════════
elif page == "📱 Preview Tampilan":
    st.markdown('<div class="section-header">📱 Preview Tampilan di Berbagai Perangkat</div>', unsafe_allow_html=True)
    st.markdown("Proyeksi tampilan yang akan dilihat pembeli dan penjual di layar HP.")
 
    tab_buyer, tab_seller = st.tabs(["👥 Tampilan Pembeli", "🏪 Tampilan Penjual"])
 
    with tab_buyer:
        st.markdown("#### Tampilan HP Pembeli")
        sample_prod = data["products"][0] if data["products"] else {}
        prod_reviews = [r for r in data["reviews"] if r.get("product_id") == sample_prod.get("id")]
        avg_r = round(sum(r["rating"] for r in prod_reviews) / len(prod_reviews), 1) if prod_reviews else 0
 
        col_phone, col_desc = st.columns([1, 1])
        with col_phone:
            st.markdown(f"""
            <div style="display:flex; justify-content:center; padding: 20px;">
              <div style="border: 6px solid #1A1A1A; border-radius: 36px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.3); width: 280px;">
                <div style="background: #1A1A1A; height: 28px; display:flex; align-items:center; justify-content:center;">
                  <div style="background:#333; width:80px; height:12px; border-radius:6px;"></div>
                </div>
                <div style="background: #FFF8F0; min-height: 560px; overflow:hidden;">
                  <!-- Header -->
                  <div style="background: linear-gradient(135deg, #3D2B1F, #D4821A); padding: 16px 14px; color:white;">
                    <div style="font-size:0.75rem; opacity:0.8;">🍟 SnackStore</div>
                    <div style="font-size:1rem; font-weight:700; margin:4px 0;">Camilan Nusantara</div>
                    <input style="width:92%; padding:6px 10px; border-radius:20px; border:none; font-size:0.75rem; margin-top:6px;" placeholder="🔍 Cari produk..."/>
                  </div>
                  <!-- Product Cards -->
                  <div style="padding: 12px 10px;">
                    <div style="font-size:0.7rem; font-weight:600; color:#6B7C5E; margin-bottom:8px;">PRODUK UNGGULAN</div>
                    <div style="background:white; border-radius:12px; padding:12px; border:1.5px solid #E8C4A0; margin-bottom:10px; box-shadow:0 2px 8px rgba(61,43,31,0.08);">
                      <div style="font-size:0.9rem; font-weight:700; color:#3D2B1F;">{sample_prod.get('name','Keripik Tempe')}</div>
                      <div style="font-size:1rem; font-weight:700; color:#D4821A; margin:3px 0;">Rp {sample_prod.get('price',15000):,}".replace(',','.')</div>
                      <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:4px;">
                        <span style="background:#F5ECD7; color:#6B7C5E; border-radius:4px; padding:2px 7px; font-size:0.65rem;">⚖️ {sample_prod.get('weight','150g')}</span>
                        <span style="background:#F5ECD7; color:#6B7C5E; border-radius:4px; padding:2px 7px; font-size:0.65rem;">⭐ {avg_r if avg_r > 0 else '4.8'}</span>
                      </div>
                      <div style="background:#25D366; color:white; border-radius:20px; text-align:center; padding:6px; margin-top:8px; font-size:0.72rem; font-weight:600;">💬 Pesan WhatsApp</div>
                    </div>
                    <div style="background:white; border-radius:12px; padding:12px; border:1.5px solid #E8C4A0; margin-bottom:10px; box-shadow:0 2px 8px rgba(61,43,31,0.08);">
                      <div style="font-size:0.9rem; font-weight:700; color:#3D2B1F;">Keripik Talas</div>
                      <div style="font-size:1rem; font-weight:700; color:#D4821A; margin:3px 0;">Rp 18.000</div>
                      <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:4px;">
                        <span style="background:#F5ECD7; color:#6B7C5E; border-radius:4px; padding:2px 7px; font-size:0.65rem;">⚖️ 130g</span>
                        <span style="background:#F5ECD7; color:#6B7C5E; border-radius:4px; padding:2px 7px; font-size:0.65rem;">⭐ 4.7</span>
                      </div>
                    </div>
                    <div style="font-size:0.7rem; font-weight:600; color:#6B7C5E; margin: 10px 0 6px;">ULASAN TERBARU</div>
                    <div style="background:#F5ECD7; border-left:3px solid #D4821A; border-radius:0 8px 8px 0; padding:8px; font-size:0.7rem;">
                      <div style="font-weight:600;">⭐⭐⭐⭐⭐ Siti Rahayu</div>
                      <div style="color:#6B5B50; margin-top:3px;">Enak banget! Renyah & gurih 😋</div>
                    </div>
                  </div>
                </div>
                <div style="background: #1A1A1A; height: 20px;"></div>
              </div>
            </div>
            """, unsafe_allow_html=True)
 
        with col_desc:
            st.markdown("""
            #### Apa yang Dilihat Pembeli?
 
            **🏠 Halaman Utama**
            - Banner toko yang menarik dan profesional
            - Kotak pencarian produk yang mudah digunakan
            - Kartu produk yang rapi dengan harga & rating
            - Tombol pesan via WhatsApp langsung
 
            **📦 Detail Produk (Klik Kartu)**
            - Nama, harga, berat, tanggal kadaluarsa
            - Gambar barcode produk
            - Rating & ulasan dari pembeli lain
            - Tombol WhatsApp untuk pemesanan cepat
 
            **⭐ Fitur Ulasan**
            - Pilih produk & beri rating bintang (1-5)
            - Tulis komentar pengalaman
            - Lihat ulasan pembeli lain di bawah beranda
 
            **💡 Keunggulan UX Pembeli**
            - Tampilan mobile-friendly & responsif
            - Filter dan sort produk
            - Informasi kadaluarsa dengan warna peringatan
            - Akses mudah ke WhatsApp penjual
            """)
 
    with tab_seller:
        st.markdown("#### Tampilan HP Penjual")
        col_phone2, col_desc2 = st.columns([1, 1])
 
        with col_phone2:
            total_rev = sum(s.get("total",0) for s in data["sales"])
            st.markdown(f"""
            <div style="display:flex; justify-content:center; padding: 20px;">
              <div style="border: 6px solid #1A1A1A; border-radius: 36px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.3); width: 280px;">
                <div style="background: #1A1A1A; height: 28px; display:flex; align-items:center; justify-content:center;">
                  <div style="background:#333; width:80px; height:12px; border-radius:6px;"></div>
                </div>
                <div style="background: #FFF8F0; min-height: 560px; overflow:hidden;">
                  <div style="background: linear-gradient(135deg, #3D2B1F, #5C3D28); padding: 16px 14px; color:#F5ECD7;">
                    <div style="font-size:0.72rem; opacity:0.7;">🔐 PANEL PENJUAL</div>
                    <div style="font-size:1rem; font-weight:700; margin:4px 0;">Dashboard Toko</div>
                  </div>
                  <div style="padding: 12px 10px;">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-bottom:12px;">
                      <div style="background:white; border-radius:10px; padding:10px; text-align:center; border:1.5px solid #E8C4A0;">
                        <div style="font-size:0.95rem; font-weight:700; color:#D4821A;">Rp{total_rev//1000}K</div>
                        <div style="font-size:0.65rem; color:#6B7C5E; margin-top:2px;">Pendapatan</div>
                      </div>
                      <div style="background:white; border-radius:10px; padding:10px; text-align:center; border:1.5px solid #E8C4A0;">
                        <div style="font-size:0.95rem; font-weight:700; color:#D4821A;">{len(data['sales'])}</div>
                        <div style="font-size:0.65rem; color:#6B7C5E; margin-top:2px;">Pesanan</div>
                      </div>
                    </div>
                    <div style="font-size:0.7rem; font-weight:600; color:#6B7C5E; margin-bottom:6px;">MENU PENJUAL</div>
                    {"".join([f'''<div style="background:white; border-radius:10px; padding:10px 12px; margin-bottom:6px; border:1.5px solid #E8C4A0; display:flex; align-items:center; gap:8px;">
                      <span style="font-size:1rem;">{icon}</span>
                      <span style="font-size:0.8rem; font-weight:600; color:#3D2B1F;">{label}</span>
                    </div>''' for icon, label in [("✏️","Edit Produk"),("📦","Generator Barcode"),("💳","QRIS & Bayar"),("📊","Laporan Laba Rugi")]])}
                    <div style="background: linear-gradient(135deg, #D4821A, #A85F0A); border-radius:10px; padding:10px 12px; margin-top:8px; color:white; font-size:0.78rem; font-weight:600; text-align:center;">
                      🔲 Generate QRIS Toko
                    </div>
                  </div>
                </div>
                <div style="background: #1A1A1A; height: 20px;"></div>
              </div>
            </div>
            """, unsafe_allow_html=True)
 
        with col_desc2:
            st.markdown("""
            #### Apa yang Dilihat Penjual?
 
            **🔐 Login Aman**
            - Halaman seller dilindungi password
            - Hanya penjual yang bisa akses fitur manajemen
 
            **📊 Dashboard Realtime**
            - Total pendapatan, pesanan, rating toko
            - Grafik penjualan harian & per produk
            - Laporan Laba Rugi otomatis (P&L)
 
            **📦 Manajemen Produk**
            - Edit harga, stok, expired kapan saja
            - Tambah produk baru dengan mudah
            - Generate & cetak barcode EAN-13
 
            **💳 QRIS & Pembayaran**
            - Buat QRIS toko sendiri
            - Catat setiap transaksi masuk
            - History lengkap semua penjualan
 
            **📈 Analitik Bisnis**
            - Laporan bisa difilter per periode
            - Export CSV untuk laporan eksternal
            - Pantau produk terlaris & margin profit
            """)
 
