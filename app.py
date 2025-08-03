# app.py - CuanWatcher v3.0
import os
import asyncio
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Import modul
try:
    from wallet import get_balance_bsc, get_transactions_bsc
    from airdrop import get_latest_airdrops
    from pajak import hitung_pajak
except Exception as e:
    print("Error import:", e)

# Setup
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🤖 **CuanWatcher v3.0**\n"
        "Asisten crypto otomatis dari MasDonk.\n\n"
        "Perintah:\n"
        "• /saldo → Cek saldo BSC\n"
        "• /tx → Transaksi terakhir\n"
        "• /airdrop → Airdrop terbaru\n"
        "• /pajak 20000000 → Cek pajak"
    )

async def saldo(update: Update, context: CallbackContext):
    bal = get_balance_bsc()
    await update.message.reply_text(f"💰 Saldo: {bal}")

async def tx(update: Update, context: CallbackContext):
    txs = get_transactions_bsc()
    msg = "🔄 **Transaksi Terakhir**\n" + "\n".join(txs)
    await update.message.reply_text(msg)

async def airdrop(update: Update, context: CallbackContext):
    ads = get_latest_airdrops()
    if not ads:
        await update.message.reply_text("❌ Gagal ambil data airdrop.")
        return
    msg = "🔔 **Airdrop Terbaru!**\n\n"
    for ad in ads:
        msg += f"📌 [{ad['title']}]({ad['link']})\n📅 {ad['published']}\n\n"
    msg += "💡 Dikirim oleh CuanWatcher"
    await update.message.reply_text(msg, parse_mode='Markdown')

async def pajak(update: Update, context: CallbackContext):
    try:
        untung = float(context.args[0])
        result = hitung_pajak(untung)
        msg = (
            f"📊 Keuntungan: Rp {untung:,.0f}\n"
            f"🔹 Status: {result['status']}\n"
            f"🔹 {result['pesan']}"
        )
        await update.message.reply_text(msg)
    except:
        await update.message.reply_text("Gunakan: /pajak 20000000")

# Jalankan otomatis (GitHub Actions)
def main():
    if not TOKEN or not CHAT_ID:
        print("TOKEN atau CHAT_ID kosong!")
        return

    bot = Bot(token=TOKEN)

    async def send_daily_airdrop():
        ads = get_latest_airdrops()
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

    asyncio.run(send_daily_airdrop())

if __name__ == "__main__":
    main()
