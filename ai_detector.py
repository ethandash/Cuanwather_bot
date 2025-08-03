from openai import OpenAI
import os

# Ambil dari config
from config import QWEN_API_KEY, QWEN_BASE_URL, QWEN_MODEL

client = OpenAI(api_key=QWEN_API_KEY, base_url=QWEN_BASE_URL)

def deteksi_scam_ai(pesan):
    """
    Kirim pesan ke Qwen untuk analisis scam
    """
    prompt = f"""
    Kamu adalah ahli keamanan crypto. Analisis deskripsi proyek berikut:
    
    "{pesan}"
    
    Jawab dalam format:
    1. Status: [SCAM / AMAN / WASPADA]
    2. Indikator: (sebutkan 1-3 tanda bahaya atau keamanan)
    3. Rekomendasi: (Abaikan / Cek tim / Jangan kirim dana / dll)
    
    Gunakan bahasa Indonesia. Maksimal 100 kata.
    """
    
    try:
        response = client.chat.completions.create(
            model=QWEN_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Gagal analisis: {str(e)}"
