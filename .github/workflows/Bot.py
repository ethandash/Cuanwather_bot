# bot.py - Bot Telegram untuk kirim info airdrop
import os
import requests
from telegram import Bot
import asyncio

# Ambil token dari environment
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # ID kamu (bisa dari @userinfobot)

# Info airdrop (nanti bisa dari web scraping atau API)
def get_airdrop_info():
    return """
🔍 **Airdrop Terbaru!**
1. **Project X** - Hadiah $1000
   📌 [Daftar di sini](https://example.com)
   ⏳ Batas: 24 jam lagi

2. **Token Y** - Untuk pengguna DeFi
   📌 [Klik untuk ikut](https://example2.com)

💡 *Bot ini dijalankan otomatis tiap jam.*
"""

async def send_telegram_message():
    bot = Bot(token=TELEGRAM_TOKEN)
    message = get_airdrop_info()
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')

if __name__ == "__main__":
    asyncio.run(send_telegram_message())
