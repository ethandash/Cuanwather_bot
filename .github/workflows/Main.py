# app.py - Versi minimal, pasti jalan
import os
from telegram import Bot
import asyncio

# Ambil token dari environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_test_message():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Error: Token atau Chat ID kosong!")
        return
    
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="🟢 CuanWatcher: Bot berhasil jalan! 🎉\n\nIni pesan uji coba pertama."
        )
        print("Pesan berhasil dikirim!")
    except Exception as e:
        print("Gagal kirim pesan:", e)

if __name__ == "__main__":
    asyncio.run(send_test_message())
