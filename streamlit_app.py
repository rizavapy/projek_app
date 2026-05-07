import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
import qrcode
from PIL import Image
import barcode
from barcode.writer import ImageWriter

# ==========================================
# CONFIG & THEME (EARTHY & CALM)
# ==========================================
st.set_page_config(
    page_title="Snack Cecilia | Premium Deli",
    page_icon="🌿",
    layout="wide"
)

# Inisialisasi State untuk Histori (Simulasi Database)
if 'sales_history' not in st.session_state:
    st.session_state.sales_history = []

# CUSTOM CSS - Calm Palette
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

    :root {
        --primary: #6B8E23; /* Sage Green */
        --secondary: #F5F5DC; /* Beige */
        --accent: #BC8F8F; /* Rosy Brown */
        --text: #3E442D;
    }

    .stApp {
        background-color: #FAF9F6;
        color: var(--text);
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 50px;
        color: var(--primary);
        text-align: center;
        margin-bottom: 0px;
    }

    /* Card Styling */
    .product-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        border: 1px solid #E9E9E2;
        transition: transform 0.2s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(107, 142, 35, 0.1);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #F0F2EB;
        border-right: 1px solid #E0E4D9;
    }

    /* Projection Mobile Frame */
    .mobile-frame {
        border: 12px solid #333;
        border-radius: 30px;
        padding: 20px;
        background: white;
        max-width: 300px;
        margin: auto;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA & HELPERS
# ==========================================
products = [
    {"Nama": "Keripik Pisang Madu", "Harga": 18000, "Kategori": "Tradisional", "Stok": 45, "WA": "628123456789", "Loc": "Jakarta"},
    {"Nama": "Sagu Keju Premium", "Harga": 35000, "Kategori": "Kue Kering", "Stok": 12, "WA": "628123456789", "Loc": "Bandung"},
    {"Nama": "Emping Pedas Manis", "Harga": 22000, "Kategori": "Pedas", "Stok": 30, "WA": "628123456789", "Loc": "Jakarta"}
]

def format_idr(val):
    return f"Rp {val:,.0f}".replace(",", ".")

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #6B8E23;'>🌿 Snack Cecilia</h2>", unsafe_allow_html=True)
    menu = st.radio("Menu Utama", ["🏪 Katalog Produk", "🏷️ Generator Smart QR", "📈 Histori Penjualan"])
    
    st.divider()
    st.info("💡 **Tips:** Gunakan QR Generator untuk memasukkan link Google Maps agar pelanggan mudah menemukan toko.")

# ==========================================
# 1. KATALOG PRODUK (REFINED)
# ==========================================
if menu == "🏪 Katalog Produk":
    st.markdown("<h1 class='main-title'>Koleksi Camilan</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>Kualitas premium dengan rasa otentik</p>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='product-card'>
                <span style='background:#F0F2EB; color:#6B8E23; padding:4px 10px; border-radius:20px; font-size:12px;'>{p['Kategori']}</span>
                <h3 style='margin:10px 0;'>{p['Nama']}</h3>
                <h4 style='color:#BC8F8F;'>{format_idr(p['Harga'])}</h4>
                <p style='font-size:13px; color:#777;'>📍 Lokasi: {p['Loc']}</p>
            </div>
            """, unsafe_allow_html=True)
            with st.expander("Lihat Detail & Beli"):
                st.write(f"Stok tersedia: {p['Stok']} pcs")
                qty = st.number_input(f"Jumlah ({p['Nama']})", min_value=1, key=f"qty_{i}")
                if st.button(f"Tambah ke Keranjang", key=f"btn_{i}"):
                    st.session_state.sales_history.append({
                        "Waktu": datetime.now().strftime("%H:%M:%S"),
                        "Produk": p['Nama'],
                        "Total": p['Harga'] * qty
                    })
                    st.success("Berhasil ditambahkan!")

# ==========================================
# 2. SMART QR GENERATOR (RICH DATA)
# ==========================================
elif menu == "🏷️ Generator Smart QR":
    st.markdown("<h2 style='color:#6B8E23;'>Rich Data QR Generator</h2>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown("### ⚙️ Informasi QR")
        with st.container(border=True):
            target_p = st.selectbox("Pilih Produk", [p['Nama'] for p in products])
            p_data = next(item for item in products if item["Nama"] == target_p)
            
            wa_num = st.text_input("WhatsApp Toko", value=p_data['WA'])
            gmaps = st.text_input("Link Google Maps", value="https://maps.google.com/?q=Snack+Cecilia")
            custom_note = st.text_area("Pesan Tambahan", "Snack premium tanpa pengawet.")
            qr_color = st.color_picker("Warna QR (Calm Tone)", "#6B8E23")

    with c2:
        # Generate QR Data String (Structured for scanning)
        qr_content = f"PRODUK: {p_data['Nama']}\nHARGA: {p_data['Harga']}\nWA: https://wa.me/{wa_num}\nLOKASI: {gmaps}\nINFO: {custom_note}"
        
        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(qr_content)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color=qr_color, back_color="white")
        
        buf = BytesIO()
        img_qr.save(buf, format="PNG")
        
        st.markdown("### 📱 Proyeksi Tampilan HP")
        st.markdown(f"""
        <div class='mobile-frame'>
            <div style='text-align:center'>
                <small style='color:#aaa;'>Hasil Scan Muncul Seperti Ini:</small>
                <h4 style='color:{qr_color};'>{p_data['Nama']}</h4>
                <hr>
                <p style='font-size:12px; text-align:left;'>
                    <b>💰 Harga:</b> {format_idr(p_data['Harga'])}<br>
                    <b>📞 Chat:</b> {wa_num}<br>
                    <b>📝 Info:</b> {custom_note}
                </p>
                <div style='background:#f9f9f9; padding:10px; border-radius:10px; font-size:10px; color:blue;'>
                    📍 Klik untuk buka Google Maps
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.image(buf, width=250, caption="Scan untuk info lengkap")
        st.download_button("Simpan QR Code", buf, "smart_qr.png", "image/png")

# ==========================================
# 3. HISTORY & ANALYTICS (SIDEBAR LAINNYA)
# ==========================================
elif menu == "📈 Histori Penjualan":
    st.markdown("<h2 style='color:#6B8E23;'>Histori Sesi Ini</h2>", unsafe_allow_html=True)
    
    if not st.session_state.sales_history:
        st.info("Belum ada transaksi di sesi ini.")
    else:
        df = pd.DataFrame(st.session_state.sales_history)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Total Omzet Sesi", format_idr(df['Total'].sum()))
        with col_b:
            st.metric("Jumlah Transaksi", len(df))
            
        st.dataframe(df, use_container_width=True)
        
        # Inovasi: Chart sederhana
        st.markdown("### Tren Penjualan")
        st.line_chart(df.set_index('Waktu')['Total'])

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("<p style='text-align:center; color:#bbb;'>Snack Cecilia © 2026 - Premium Snack Experience</p>", unsafe_allow_html=True)
