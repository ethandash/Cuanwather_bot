# app.py - CuanWatcher v2.0
# Bot Telegram otomatis: Airdrop + Pajak Planner
import os
import asyncio
import feedparser
from datetime import datetime
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# === SETUP BOT ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TELEGRAM_TOKEN or not CHAT_ID:
    raise ValueError("TELEGRAM_TOKEN atau CHAT_ID tidak ditemukan!")

# === FUNGSI: Ambil Airdrop dari RSS ===
def get_latest_airdrops():
    try:
        feed = feedparser.parse("https://airdrops.io/feed/")
        message = "🔍 **Airdrop Terbaru dari Airdrops.io**\n\n"
        count = 0

        for entry in feed.entries:
            if count >= 5:
                break
            title = entry.title
            link = entry.link
            try:
                pub_date = datetime(*entry.published_parsed[:6])
                age = (datetime.now() - pub_date).days
            except:
                age = "?"
            
            message += f"📌 **{title}**\n"
            message += f"🗓️ {age} hari lalu\n"
            message += f"🔗 [Daftar di sini]({link})\n\n"
            count += 1

        message += "💡 *Dikirim otomatis oleh CuanWatcher — bot dari MasDonk.*"
        return message
    except Exception as e:
        return f"❌ Gagal ambil data airdrop: {str(e)}"

# === FUNGSI: Hitung Pajak ===
def hitung_pajak_keuntungan(keuntungan):
    ptkp = 54_000_000  # PTKP tahunan
    if keuntungan < ptkp:
        return f"✅ AMAN! Keuntungan kamu masih di bawah PTKP (Rp {ptkp:,}). Belum perlu bayar pajak."
    else:
        pajak = (keuntungan - ptkp) * 0.15
        return f"⚠️ Harus lapor. Pajak terutang: Rp {pajak:,.0f}"

# === COMMAND BOT ===
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Hai! Aku CuanWatcher 🤖\n"
        "Bot pencari peluang crypto dari MasDonk.\n\n"
        "Perintah:\n"
        "• /airdrop → Cek airdrop terbaru\n"
        "• /pajak 10000000 → Cek pajak dari keuntungan (dalam IDR)"
    )

async def airdrop(update: Update, context: CallbackContext):
    message = get_latest_airdrops()
    await update.message.reply_text(message, parse_mode='Markdown')

async def pajak(update: Update, context: CallbackContext):
    try:
        jumlah = float(context.args[0])
        hasil = hitung_pajak_keuntungan(jumlah)
        await update.message.reply_text(f"📊 Keuntungan: Rp {jumlah:,.0f}\n\n{hasil}")
    except:
        await update.message.reply_text("Gunakan: /pajak 50000000")

# === JALANKAN BOT ===
def main():
    bot = Bot(token=TELEGRAM_TOKEN)

    # Untuk polling manual (karena kita pakai GitHub Actions)
    async def send_airdrop():
        message = get_latest_airdrops()
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode='Markdown')

    # Jalankan kirim airdrop
    asyncio.run(send_airdrop())

if __name__ == "__main__":
    main()
