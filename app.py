# app.py - Bot Telegram otomatis (untuk GitHub Actions)
import os
import asyncio
from telegram import Bot

# Ambil token dari environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Pesan airdrop (nanti bisa diambil dari web)
def get_airdrop_message():
    return """
🔍 **CuanWatcher - Airdrop Update!**
1. **Project X** - Hadiah $500
   📌 [Daftar sekarang](https://example.com)
   ⏳ Batas: 24 jam lagi

2. **Token Y** - Untuk pengguna wallet
   📌 [Klik di sini](https://example2.com)

💡 *Dikirim otomatis tiap jam oleh GitHub Actions.*
"""

async def send_message():
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=get_airdrop_message(),
        parse_mode='Markdown'
    )

if __name__ == "__main__":
    asyncio.run(send_message())
