# app.py - CuanWatcher v4.0
import os
import asyncio
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Import modul
try:
    from airdrop import get_active_airdrops
    from wallet import get_balance_bsc
    from faucet import get_faucet_list
except Exception as e:
    print("Error import:", e)

# Setup
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# === COMMAND BOT ===
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🤖 **CuanWatcher v4.0**\n"
        "Asisten crypto dari MasDonk.\n\n"
        "Perintah:\n"
        "• /airdrop → Airdrop aktif\n"
        "• /saldo → Saldo wallet\n"
        "• /faucet → Faucet gratis\n"
        "• /scam [deskripsi] → Deteksi scam"
    )

async def airdrop(update: Update, context: CallbackContext):
    ads = get_active_airdrops()
    if not ads:
        await update.message.reply_text("❌ Gagal ambil data airdrop.")
        return
    msg = "🎁 **Airdrop Aktif (< 7 hari)**\n\n"
    for ad in ads:
        msg += f"📌 [{ad['title']}]({ad['link']})\n"
        msg += f"🗓️ {ad['age']} hari lalu\n"
        msg += f"📝 {ad['summary']}\n\n"
    msg += "💡 Dikirim oleh CuanWatcher"
    await update.message.reply_text(msg, parse_mode='Markdown')

async def saldo(update: Update, context: CallbackContext):
    bal = get_balance_bsc()
    await update.message.reply_text(f"💰 Saldo BSC: {bal}")

async def faucet(update: Update, context: CallbackContext):
    msg = get_faucet_list()
    await update.message.reply_text(msg, parse_mode='Markdown')

async def scam(update: Update, context: CallbackContext):
    try:
        description = ' '.join(context.args)
        if not description:
            await update.message.reply_text("Gunakan: /scam [deskripsi proyek]")
            return

        # Simulasi deteksi scam (nanti bisa pakai Qwen API)
        desc_low = description.lower()
        if any(word in desc_low for word in ['private key', 'seed phrase', 'send to win', 'claim now!', 'free money']):
            result = "⚠️ **WASPADA! Kemungkinan SCAM**\n\n" \
                     "❌ Meminta private key / seed\n" \
                     "❌ Janji hadiah besar\n" \
                     "❌ Tautan mencurigakan\n\n" \
                     "💡 Jangan daftar, bisa kehilangan dana!"
        else:
            result = "✅ **Terlihat aman**\n\n" \
                     "Tapi tetap waspada. Cek tim, whitepaper, dan komunitas."

        await update.message.reply_text(result)
    except:
        await update.message.reply_text("Error. Gunakan: /scam [deskripsi]")

# === JALANKAN OTOMATIS (GitHub Actions) ===
def main():
    if not TOKEN or not CHAT_ID:
        print("TOKEN atau CHAT_ID kosong!")
        return

    bot = Bot(token=TOKEN)

    async def send_daily_update():
        # Kirim airdrop harian
        ads = get_active_airdrops()
        if not ads:
            return
        msg = "🔔 **Update Airdrop Harian!**\n\n"
        for ad in ads:
            msg += f"📌 [{ad['title']}]({ad['link']})\n"
        msg += "\n💡 Dikirim oleh CuanWatcher"
        try:
            await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode='Markdown')
        except Exception as e:
            print("Gagal kirim:", e)

    asyncio.run(send_daily_update())

if __name__ == "__main__":
    main()
