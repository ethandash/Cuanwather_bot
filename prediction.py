# prediction.py - Prediksi peluang crypto akhir 2025
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def prediksi_meledak_2025():
    prompt = """
    Berdasarkan tren crypto 2024-2025, sebutkan 5 proyek yang berpotensi meledak di akhir 2025.
    Fokus pada:
    - Proyek dengan airdrop besar
    - Testnet aktif & banyak user
    - Team kuat & roadmap jelas
    - Komunitas besar
    - Tokenomics sehat

    Format:
    1. Nama Proyek: [nama]
       Alasan: [1-2 kalimat]
       Potensi: [tinggi/sedang]
       Risiko: [rendah/sedang]
    2. ...
    """
    try:
        response = client.chat.completions.create(
            model="qwen-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Gagal prediksi: {str(e)}"

# auto_prediction.py
from datetime import datetime

def should_send_weekly():
    today = datetime.now().weekday()
    return today == 0  # Senin

# prediction.py - tambah fungsi
def cek_testnet_baru_dari_ai():
    prompt = """
    Sebutkan 5 proyek testnet crypto terbaru (bulan ini) yang berpotensi dapat airdrop.
    Fokus pada:
    - Proyek Layer 2
    - zkEVM
    - Cross-chain
    - Didukung tim besar

    Format:
    1. Nama: [nama]
       URL: [link]
       Chain: [BSC/zkSync/etc]
       Potensi Airdrop: [Tinggi/Sedang]
    """
    try:
        response = client.chat.completions.create(
            model="qwen-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Gagal: {str(e)}"
if should_send_weekly():
    result = prediksi_meledak_2025()
    send_telegram(f"📅 **Update Mingguan: Peluang 2025**\n\n{result}")

