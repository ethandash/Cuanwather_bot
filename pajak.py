# pajak.py - Hitung pajak sesuai PMK 50/2025
PTKP = 54_000_000  # Tidak kena pajak
PPH_RATE = 0.0021  # 0,21%

def hitung_pajak(keuntungan):
    if keuntungan < PTKP:
        return {
            "status": "✅ AMAN",
            "pajak": 0,
            "pesan": f"Masih di bawah PTKP (Rp {PTKP:,})."
        }
    else:
        pajak = (keuntungan - PTKP) * PPH_RATE
        return {
            "status": "⚠️ WAJIB LAPOR",
            "pajak": pajak,
            "pesan": f"Pajak terutang: Rp {pajak:,.0f}"
        }
