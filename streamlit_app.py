import { useState, useRef, useEffect } from "react";

const PRODUCTS = [
  {
    id: "CS001",
    name: "Keripik Singkong",
    brand: "Cecilia Snack",
    weight: "250g",
    price: 12000,
    priceOri: 15000,
    emoji: "ðŸ¥”",
    bg: "linear-gradient(135deg,#FFF3E0,#FFE0B2)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-22",
    expired: "12 bulan",
    ingredients: "Singkong, Minyak Nabati, Garam, Bumbu",
    desc: "Keripik singkong renyah dengan bumbu gurih khas Jawa.",
    barcode: "8993012200140",
    wa: "6281234567890",
  },
  {
    id: "CS002",
    name: "Keripik Pisang",
    brand: "Cecilia Snack",
    weight: "200g",
    price: 10000,
    priceOri: 13000,
    emoji: "ðŸŒ",
    bg: "linear-gradient(135deg,#FFFDE7,#FFF9C4)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-23",
    expired: "10 bulan",
    ingredients: "Pisang, Minyak Nabati, Gula, Garam",
    desc: "Keripik pisang manis legit, dibuat dari pisang pilihan.",
    barcode: "8993012200157",
    wa: "6281234567890",
  },
  {
    id: "CS003",
    name: "Kue Bawang",
    brand: "Cecilia Snack",
    weight: "150g",
    price: 8000,
    priceOri: 10000,
    emoji: "ðŸ§…",
    bg: "linear-gradient(135deg,#F3E5F5,#EDE7F6)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-24",
    expired: "8 bulan",
    ingredients: "Tepung Terigu, Bawang Putih, Telur, Minyak, Garam",
    desc: "Kue bawang gurih dan renyah, cocok untuk cemilan keluarga.",
    barcode: "8993012200164",
    wa: "6281234567890",
  },
  {
    id: "CS004",
    name: "Rempeyek Kacang",
    brand: "Cecilia Snack",
    weight: "180g",
    price: 11000,
    priceOri: 14000,
    emoji: "ðŸ¥œ",
    bg: "linear-gradient(135deg,#E8F5E9,#C8E6C9)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-25",
    expired: "9 bulan",
    ingredients: "Tepung Beras, Kacang Tanah, Santan, Bumbu Rempah",
    desc: "Rempeyek kacang tanah renyah dengan aroma rempah yang khas.",
    barcode: "8993012200171",
    wa: "6281234567890",
  },
];

// ---- Mini QR Matrix Generator (visual only, functional via URL) ----
function generateQRMatrix(size = 21) {
  // Deterministic pseudorandom for visual QR-like pattern
  const matrix = Array.from({ length: size }, () => Array(size).fill(0));
  // Finder patterns
  const finder = (r, c) => {
    for (let i = 0; i < 7; i++) for (let j = 0; j < 7; j++) {
      const v = (i === 0 || i === 6 || j === 0 || j === 6) ? 1 : (i >= 2 && i <= 4 && j >= 2 && j <= 4) ? 1 : 0;
      if (r + i < size && c + j < size) matrix[r + i][c + j] = v;
    }
  };
  finder(0, 0); finder(0, size - 7); finder(size - 7, 0);
  // Fill rest with pattern
  for (let i = 0; i < size; i++) for (let j = 0; j < size; j++) {
    if (matrix[i][j] === 0) matrix[i][j] = ((i * 3 + j * 7 + i * j) % 5 < 2) ? 1 : 0;
  }
  return matrix;
}

const QR_MATRIX = generateQRMatrix(21);

function QRCode({ url, size = 120, product }) {
  // Use Google Charts API for real scannable QR
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encodeURIComponent(url)}&color=3E2000&bgcolor=FFFDF8`;
  return (
    <div style={{ textAlign: "center" }}>
      <img
        src={qrUrl}
        alt="QR Code"
        width={size}
        height={size}
        style={{ borderRadius: 8, border: "2px solid #3E2000", display: "block", margin: "0 auto" }}
        onError={(e) => {
          // Fallback visual QR
          e.target.style.display = "none";
        }}
      />
    </div>
  );
}

function Barcode({ code, width = 200, height = 60 }) {
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FFFDF8";
    ctx.fillRect(0, 0, width, height);

    // EAN-13 like visual barcode
    const digits = code.slice(0, 13).padEnd(13, "0");
    const bars = [];
    // Encode digits to bars (simplified visual)
    const enc = [
      [3,2,1,1],[2,2,2,1],[2,1,2,2],[1,4,1,1],[1,1,3,2],
      [1,2,3,1],[1,1,1,4],[1,3,1,2],[1,2,1,3],[3,1,1,2]
    ];
    bars.push(1,0,1); // start
    for (let i = 1; i < 7; i++) {
      const d = parseInt(digits[i]);
      enc[d].forEach((w, idx) => {
        for (let k = 0; k < w; k++) bars.push(idx % 2 === 0 ? 1 : 0);
      });
    }
    bars.push(0,1,0,1,0); // middle
    for (let i = 7; i < 13; i++) {
      const d = parseInt(digits[i]);
      enc[d].forEach((w, idx) => {
        for (let k = 0; k < w; k++) bars.push(idx % 2 === 0 ? 0 : 1);
      });
    }
    bars.push(1,0,1); // end

    const barW = (width - 20) / bars.length;
    bars.forEach((b, i) => {
      if (b) {
        ctx.fillStyle = "#3E2000";
        ctx.fillRect(10 + i * barW, 5, Math.max(barW - 0.3, 0.7), height - 18);
      }
    });

    // Digit text
    ctx.fillStyle = "#3E2000";
    ctx.font = `bold ${Math.floor(height * 0.18)}px 'Courier New', monospace`;
    ctx.textAlign = "center";
    const spacing = (width - 20) / 13;
    for (let i = 0; i < 13; i++) {
      ctx.fillText(digits[i], 10 + (i + 0.5) * spacing, height - 2);
    }
  }, [code, width, height]);

  return <canvas ref={canvasRef} width={width} height={height} style={{ display: "block", margin: "0 auto" }} />;
}

function ProductPage({ product, onBack }) {
  const waMsg = encodeURIComponent(`Halo Cecilia Snack! Saya ingin memesan *${product.name}* (${product.weight}) â€” Rp ${product.price.toLocaleString("id-ID")}`);
  const waUrl = `https://wa.me/${product.wa}?text=${waMsg}`;
  const productUrl = `https://ceciliasnack.id/produk/${product.id.toLowerCase()}`;

  return (
    <div style={{
      minHeight: "100vh",
      background: "#FFF8EE",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "0 0 40px",
      fontFamily: "'DM Sans', sans-serif",
    }}>
      {/* Header */}
      <div style={{
        width: "100%",
        background: "linear-gradient(135deg,#3E2000,#E8650A)",
        color: "white",
        padding: "20px 24px 16px",
        display: "flex",
        alignItems: "center",
        gap: 12,
      }}>
        <button onClick={onBack} style={{
          background: "rgba(255,255,255,0.2)", border: "none", color: "white",
          borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontSize: 14, fontWeight: 700,
        }}>â† Kembali</button>
        <div>
          <div style={{ fontSize: 18, fontWeight: 900, fontFamily: "Georgia, serif" }}>Cecilia Snack</div>
          <div style={{ fontSize: 11, opacity: 0.8 }}>Halaman Produk Digital</div>
        </div>
      </div>

      {/* Product Image Area */}
      <div style={{
        width: "100%", maxWidth: 420,
        background: product.bg,
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: 96, padding: "32px 0",
      }}>
        {product.emoji}
      </div>
{/* Info */}
      <div style={{ width: "100%", maxWidth: 420, padding: "0 20px" }}>
        {/* Badges */}
        <div style={{ display: "flex", gap: 8, marginTop: 16, marginBottom: 12 }}>
          {product.halal && (
            <span style={{ background: "#1A5C2A", color: "white", fontSize: 11, fontWeight: 700, padding: "4px 10px", borderRadius: 4 }}>âœ“ HALAL</span>
          )}
          <span style={{ background: "#3E2000", color: "white", fontSize: 11, fontWeight: 700, padding: "4px 10px", borderRadius: 4 }}>PIRT</span>
          <span style={{ background: "#E8650A", color: "white", fontSize: 11, fontWeight: 700, padding: "4px 10px", borderRadius: 4 }}>UMKM</span>
        </div>

        <h1 style={{ fontFamily: "Georgia, serif", fontSize: 28, fontWeight: 900, color: "#3E2000", margin: "0 0 4px" }}>{product.name}</h1>
        <div style={{ color: "#E8650A", fontSize: 12, fontWeight: 700, letterSpacing: 2, marginBottom: 8 }}>{product.brand} â€¢ {product.weight}</div>
        <p style={{ color: "#7A5C3A", fontSize: 14, lineHeight: 1.7, marginBottom: 16 }}>{product.desc}</p>

        {/* Price */}
        <div style={{
          background: "white", borderRadius: 12, padding: "16px 20px",
          display: "flex", alignItems: "center", justifyContent: "space-between",
          boxShadow: "0 4px 20px rgba(62,32,0,0.12)", marginBottom: 16,
        }}>
          <div>
            <div style={{ fontSize: 11, color: "#7A5C3A", marginBottom: 4 }}>Harga Promo</div>
            <div style={{ fontSize: 26, fontWeight: 900, color: "#3E2000" }}>Rp {product.price.toLocaleString("id-ID")}</div>
            <div style={{ fontSize: 12, color: "#999", textDecoration: "line-through" }}>Rp {product.priceOri.toLocaleString("id-ID")}</div>
          </div>
          <div style={{ textAlign: "right" }}>
            <div style={{ fontSize: 20, fontWeight: 900, color: "#E8650A" }}>
              -{Math.round((1 - product.price / product.priceOri) * 100)}%
            </div>
            <div style={{ fontSize: 11, color: "#7A5C3A" }}>Hemat Rp {(product.priceOri - product.price).toLocaleString("id-ID")}</div>
          </div>
        </div>

        {/* Details */}
        <div style={{ background: "white", borderRadius: 12, padding: "16px 20px", marginBottom: 16, boxShadow: "0 4px 20px rgba(62,32,0,0.08)" }}>
          <div style={{ fontWeight: 700, fontSize: 13, color: "#3E2000", marginBottom: 12 }}>Informasi Produk</div>
          {[
            ["ðŸ·ï¸ Kode Produk", product.id],
            ["ðŸŒ¿ Bahan", product.ingredients],
            ["ðŸ“… Masa Simpan", product.expired],
            ["ðŸ“‹ Sertifikasi", product.pirt],
          ].map(([label, val]) => (
            <div key={label} style={{ display: "flex", gap: 10, padding: "8px 0", borderBottom: "1px solid #F0E6D6", fontSize: 13 }}>
              <span style={{ minWidth: 110, color: "#7A5C3A" }}>{label}</span>
              <span style={{ color: "#3E2000", fontWeight: 500 }}>{val}</span>
            </div>
          ))}
        </div>

        {/* Barcode display */}
        <div style={{ background: "white", borderRadius: 12, padding: "16px", marginBottom: 16, textAlign: "center", boxShadow: "0 4px 20px rgba(62,32,0,0.08)" }}>
          <div style={{ fontSize: 11, color: "#7A5C3A", marginBottom: 8 }}>Barcode Produk</div>
          <Barcode code={product.barcode} width={240} height={52} />
        </div>

        {/* Order Button */}
        <a href={waUrl} target="_blank" rel="noopener noreferrer" style={{
          display: "block", background: "#25D366", color: "white",
          textAlign: "center", padding: "16px", borderRadius: 12,
          fontWeight: 800, fontSize: 15, textDecoration: "none",
          marginBottom: 10, boxShadow: "0 4px 20px rgba(37,211,102,0.4)",
        }}>
          ðŸ’¬ Pesan via WhatsApp
        </a>
      </div>
    </div>
  );
}

// ---- MAIN APP ----
export default function CeciliaQRApp() {
  const [tab, setTab] = useState("generator"); // generator | scanner-sim | product
  const [selected, setSelected] = useState(null);
  const [scannedProduct, setScannedProduct] = useState(null);
  const [customProduct, setCustomProduct] = useState({
    name: "", price: "", weight: "", desc: "", barcode: "", wa: "6281234567890",
  });
  const [qrGenerated, setQrGenerated] = useState(false);
  const [activeScan, setActiveScan] = useState(null);

  // If viewing a product page (simulating QR scan result)
  if (scannedProduct) {
    return <ProductPage product={scannedProduct} onBack={() => setScannedProduct(null)} />;
  }

  const handleGenerateQR = () => {
    if (!selected && !customProduct.name) return;
    setQrGenerated(true);
  };

  const currentProduct = selected !== null ? PRODUCTS[selected] : null;
  const productUrl = currentProduct
    ? `https://ceciliasnack.id/produk/${currentProduct.id.toLowerCase()}`
    : customProduct.name
    ? `https://ceciliasnack.id/produk/custom-${customProduct.name.toLowerCase().replace(/\s+/g, "-")}`

return (
    <div style={{ minHeight: "100vh", background: "#FFF8EE", fontFamily: "'DM Sans', sans-serif", color: "#3E2000" }}>
      {/* Header */}
      <div style={{
        background: "linear-gradient(135deg,#3E2000 0%,#6B3500 60%,#E8650A 100%)",
        color: "white", padding: "28px 24px 24px", textAlign: "center",
      }}>
        <div style={{
          display: "inline-block", background: "#E8650A", fontSize: 10, letterSpacing: 3,
          padding: "5px 16px", borderRadius: 2, marginBottom: 12, fontWeight: 700,
        }}>INDI 4.0 â€” CECILIA SNACK</div>
        <h1 style={{ fontFamily: "Georgia, serif", fontSize: 32, fontWeight: 900, margin: "0 0 8px" }}>
          ðŸŸ Generator QR & Barcode
        </h1>
        <p style={{ fontSize: 14, opacity: 0.85 }}>Buat QR Code yang bisa di-scan, tampilkan info produk langsung</p>
      </div>

      {/* Tabs */}
      <div style={{ display: "flex", background: "white", borderBottom: "2px solid #F0E6D6" }}>
        {[
          { key: "generator", label: "ðŸŽ¨ Buat QR/Barcode" },
          { key: "scanner", label: "ðŸ“± Simulasi Scan" },
        ].map(t => (
          <button key={t.key} onClick={() => { setTab(t.key); setQrGenerated(false); }}
            style={{
              flex: 1, padding: "14px 8px", border: "none", cursor: "pointer",
              fontWeight: 700, fontSize: 13,
              background: tab === t.key ? "#FFF8EE" : "white",
              color: tab === t.key ? "#E8650A" : "#7A5C3A",
              borderBottom: tab === t.key ? "3px solid #E8650A" : "3px solid transparent",
            }}>
            {t.label}
          </button>
        ))}
      </div>

      {/* TAB: GENERATOR */}
      {tab === "generator" && (
        <div style={{ padding: "24px 20px", maxWidth: 700, margin: "0 auto" }}>
          <h2 style={{ fontFamily: "Georgia, serif", fontSize: 20, marginBottom: 6 }}>Pilih Produk</h2>
          <p style={{ fontSize: 13, color: "#7A5C3A", marginBottom: 16 }}>Pilih produk Cecilia Snack atau isi data custom</p>

          {/* Product Selector */}
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginBottom: 20 }}>
            {PRODUCTS.map((p, i) => (
              <div key={p.id} onClick={() => { setSelected(i); setCustomProduct({ name: "", price: "", weight: "", desc: "", barcode: "", wa: "6281234567890" }); setQrGenerated(false); }}
                style={{
                  background: selected === i ? "#FFF3E0" : "white",
                  border: selected === i ? "2px solid #E8650A" : "2px solid #F0E6D6",
                  borderRadius: 12, padding: "14px", cursor: "pointer",
                  display: "flex", alignItems: "center", gap: 10,
                  transition: "all 0.2s",
                }}>
                <span style={{ fontSize: 32 }}>{p.emoji}</span>
                <div>
                  <div style={{ fontWeight: 700, fontSize: 14 }}>{p.name}</div>
                  <div style={{ fontSize: 12, color: "#7A5C3A" }}>{p.weight} â€¢ Rp {p.price.toLocaleString("id-ID")}</div>
                </div>
              </div>
            ))}
          </div>

          {/* Custom Product Form */}
          <div style={{ background: "white", borderRadius: 14, padding: "20px", marginBottom: 20, border: "2px solid #F0E6D6" }}>
            <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 14, color: "#3E2000" }}>âœï¸ Atau Isi Produk Custom</div>
            {[
              { key: "name", label: "Nama Produk", placeholder: "cth: Keripik Tempe Pedas" },
              { key: "price", label: "Harga (Rp)", placeholder: "cth: 15000" },
              { key: "weight", label: "Berat / Ukuran", placeholder: "cth: 200g" },
              { key: "desc", label: "Deskripsi Singkat", placeholder: "cth: Keripik tempe renyah..." },
              { key: "barcode", label: "Nomor Barcode (13 digit)", placeholder: "cth: 8993012200188" },
              { key: "wa", label: "No. WhatsApp (62xxx)", placeholder: "6281234567890" },
            ].map(f => (
              <div key={f.key} style={{ marginBottom: 12 }}>
                <label style={{ fontSize: 12, fontWeight: 600, color: "#7A5C3A", display: "block", marginBottom: 4 }}>{f.label}</label>
                <input
                  type="text"
                  placeholder={f.placeholder}
                  value={customProduct[f.key]}
                  onChange={e => { setSelected(null); setCustomProduct(p => ({ ...p, [f.key]: e.target.value })); setQrGenerated(false); }}
                  style={{
                    width: "100%", padding: "10px 12px", borderRadius: 8,
                    border: "1.5px solid #E8DDD0", fontSize: 14, outline: "none",
                    fontFamily: "inherit", color: "#3E2000", background: "#FFFDF8",
                    boxSizing: "border-box",
                  }}
                />
              </div>
            ))}
          </div>

          {/* Generate Button */}
          <button onClick={handleGenerateQR}
            disabled={!selected && selected !== 0 && !customProduct.name}
            style={{
              width: "100%", padding: "16px", background: "#E8650A", color: "white",
              border: "none", borderRadius: 12, fontWeight: 800, fontSize: 16,
              cursor: "pointer", marginBottom: 24,
              opacity: (!selected && selected !== 0 && !customProduct.name) ? 0.5 : 1,
            }}>
            ðŸŽ¯ Generate QR Code & Barcode
          </button>


          {/* Generated Output */}
          {qrGenerated && (currentProduct || customProduct.name) && (() => {
            const prod = currentProduct || {
              id: "CUSTOM",
              name: customProduct.name,
              price: parseInt(customProduct.price) || 0,
              priceOri: parseInt(customProduct.price) || 0,
              weight: customProduct.weight,
              desc: customProduct.desc,
              emoji: "ðŸ¿",
              bg: "linear-gradient(135deg,#FFF3E0,#FFE0B2)",
              halal: false,
              pirt: "-",
              expired: "-",
              ingredients: "-",
              barcode: customProduct.barcode || "8993012200100",
              wa: customProduct.wa,
            };
            const url = `https://ceciliasnack.id/produk/${prod.id.toLowerCase()}`;

            return (
              <div style={{ background: "white", borderRadius: 16, padding: "24px", boxShadow: "0 8px 32px rgba(62,32,0,0.12)" }}>
                <div style={{ textAlign: "center", marginBottom: 20 }}>
                  <div style={{ fontSize: 11, letterSpacing: 3, color: "#E8650A", fontWeight: 700, marginBottom: 8 }}>HASIL GENERATE</div>
                  <h3 style={{ fontFamily: "Georgia, serif", fontSize: 22, margin: "0 0 4px" }}>{prod.name}</h3>
                  <div style={{ fontSize: 13, color: "#7A5C3A" }}>{prod.weight} â€¢ Rp {prod.price.toLocaleString("id-ID")}</div>
                </div>

                {/* QR Code */}
                <div style={{ textAlign: "center", marginBottom: 20, background: "#FFFDF8", borderRadius: 12, padding: 20 }}>
                  <div style={{ fontSize: 12, fontWeight: 700, color: "#7A5C3A", marginBottom: 12, letterSpacing: 1 }}>ðŸ“± QR CODE â€” BISA DI-SCAN!</div>
                  <QRCode url={url} size={160} product={prod} />
                  <div style={{ fontSize: 11, color: "#7A5C3A", marginTop: 10, wordBreak: "break-all", padding: "0 10px" }}>
                    ðŸ”— {url}
                  </div>
                  <div style={{ marginTop: 10, fontSize: 12, background: "#E8F5E9", color: "#1A5C2A", padding: "8px 12px", borderRadius: 8, fontWeight: 600 }}>
                    âœ… Scan QR di atas untuk melihat halaman produk
                  </div>
                </div>

                {/* Barcode */}
                <div style={{ textAlign: "center", background: "#FFFDF8", borderRadius: 12, padding: "16px", marginBottom: 16 }}>
                  <div style={{ fontSize: 12, fontWeight: 700, color: "#7A5C3A", marginBottom: 10, letterSpacing: 1 }}>ðŸ“Š BARCODE PRODUK</div>
                  <div style={{ background: "white", display: "inline-block", padding: "12px 16px", borderRadius: 8, border: "1.5px solid #E8DDD0" }}>
                    <Barcode code={prod.barcode} width={220} height={56} />
                  </div>
                </div>

                {/* Label Preview */}
                <div style={{ border: "2px dashed #E8650A", borderRadius: 12, padding: 16, marginBottom: 16 }}>
                  <div style={{ fontSize: 11, letterSpacing: 2, color: "#E8650A", fontWeight: 700, marginBottom: 10 }}>ðŸ·ï¸ PREVIEW LABEL KEMASAN</div>
                  <div style={{
                    background: prod.bg, borderRadius: 10, padding: "16px",
                    display: "flex", gap: 14, alignItems: "center",
                  }}>
                    <span style={{ fontSize: 48 }}>{prod.emoji}</span>
                    <div style={{ flex: 1 }}>
                      <div style={{ fontFamily: "Georgia, serif", fontWeight: 900, fontSize: 16, color: "#3E2000" }}>{prod.name}</div>
                      <div style={{ fontSize: 11, color: "#E8650A", fontWeight: 700, letterSpacing: 1 }}>CECILIA SNACK</div>
                      <div style={{ fontSize: 20, fontWeight: 900, color: "#3E2000", margin: "4px 0" }}>Rp {prod.price.toLocaleString("id-ID")}</div>
                      <div style={{ display: "flex", gap: 6 }}>
                        {prod.halal && <span style={{ background: "#1A5C2A", color: "white", fontSize: 9, fontWeight: 700, padding: "2px 6px", borderRadius: 3 }}>HALAL</span>}
                        <span style={{ background: "#3E2000", color: "white", fontSize: 9, fontWeight: 700, padding: "2px 6px", borderRadius: 3 }}>PIRT</span>
                      </div>
                    </div>
                    <div>
                      <QRCode url={url} size={70} product={prod} />
                      <div style={{ fontSize: 8, color: "#7A5C3A", textAlign: "center", marginTop: 3 }}>Scan untuk info</div>
                    </div>
                  </div>
                </div>

                {/* Simulate scan button */}
                <button onClick={() => setScannedProduct(currentProduct || { ...prod, id: "CUSTOM" })}
                  style={{
                    width: "100%", padding: "14px", background: "#3E2000", color: "white",
                    border: "none", borderRadius: 12, fontWeight: 800, fontSize: 14, cursor: "pointer",
                  }}>
                  ðŸ“± Simulasikan Hasil Scan QR â†’
                </button>
              </div>
            );
          })()}
        </div>
      )}


      {/* TAB: SCANNER SIMULATOR */}
      {tab === "scanner" && (
        <div style={{ padding: "24px 20px", maxWidth: 700, margin: "0 auto" }}>
          <h2 style={{ fontFamily: "Georgia, serif", fontSize: 20, marginBottom: 6 }}>Simulasi Scan QR</h2>
          <p style={{ fontSize: 13, color: "#7A5C3A", marginBottom: 20 }}>
            Tap produk untuk melihat tampilan halaman yang muncul saat QR di-scan konsumen
          </p>

          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            {PRODUCTS.map((p, i) => {
              const url = `https://ceciliasnack.id/produk/${p.id.toLowerCase()}`;
              return (
                <div key={p.id} style={{
                  background: "white", borderRadius: 14, overflow: "hidden",
                  boxShadow: "0 4px 20px rgba(62,32,0,0.10)", border: "1.5px solid #F0E6D6",
                }}>
                  <div style={{ display: "flex", gap: 0 }}>
                    {/* Product Info */}
                    <div style={{ flex: 1, padding: "16px 16px" }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
                        <span style={{ fontSize: 36 }}>{p.emoji}</span>
                        <div>
                          <div style={{ fontWeight: 800, fontSize: 15 }}>{p.name}</div>
                          <div style={{ fontSize: 12, color: "#E8650A", fontWeight: 600 }}>{p.weight} â€¢ Rp {p.price.toLocaleString("id-ID")}</div>
                        </div>
                      </div>
                      <div style={{ marginBottom: 10 }}>
                        <QRCode url={url} size={90} product={p} />
                        <div style={{ fontSize: 9, color: "#7A5C3A", textAlign: "center", marginTop: 4 }}>QR Bisa Di-scan Langsung</div>
                      </div>
                      <div style={{ background: "#F5E6C8", borderRadius: 8, padding: "6px 10px", marginBottom: 8 }}>
                        <Barcode code={p.barcode} width={160} height={36} />
                      </div>
                      <button onClick={() => setScannedProduct(p)}
                        style={{
                          width: "100%", padding: "10px", background: "#E8650A", color: "white",
                          border: "none", borderRadius: 8, fontWeight: 700, fontSize: 12, cursor: "pointer",
                        }}>
                        ðŸ“± Lihat Halaman Produk â†’
                      </button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div style={{
            marginTop: 24, background: "#E8F5E9", borderRadius: 12, padding: "16px",
            border: "1.5px solid #A5D6A7",
          }}>
            <div style={{ fontWeight: 700, fontSize: 13, color: "#1A5C2A", marginBottom: 6 }}>ðŸ’¡ Cara Pakai QR Code Asli</div>
            <ol style={{ fontSize: 12, color: "#3E2000", paddingLeft: 16, lineHeight: 2 }}>
              <li>Generate QR di tab "Buat QR/Barcode"</li>
              <li>Screenshot atau download gambar QR</li>
              <li>Print dan tempel ke kemasan produk</li>
              <li>Konsumen scan â†’ langsung dapat info produk!</li>
            </ol>
          </div>
        </div>
      )}

      {/* Footer */}
      <div style={{
        background: "#3E2000", color: "rgba(255,255,255,0.7)",
        padding: "24px", textAlign: "center", marginTop: 40,
      }}>
        <div style={{ color: "#FFD580", fontFamily: "Georgia, serif", fontSize: 18, marginBottom: 4 }}>Cecilia Snack Ã— INDI 4.0</div>
        <div style={{ fontSize: 12 }}>Digitalisasi UMKM â€¢ QR Code & Barcode Generator</div>
      </div>
    </div>
  );
}
