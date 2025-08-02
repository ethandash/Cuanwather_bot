# file: app.py
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Ambil token dari environment variable (aman!)
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN tidak ditemukan! Cek di Cyclic.sh")

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(
        f"Hai {user.first_name}! 🌟\n"
        "Aku CuanWatcher — bot pencari peluang crypto!\n"
        "Perintah:\n"
        "• /airdrop → Cek airdrop terbaru\n"
        "• /faucet → Faucet gratis\n"
        "• /help → Bantuan"
    )

def airdrop(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🔍 Airdrop Terbaru:\n"
        "1. Proyek X - Hadiah $500 → [Daftar di sini](https://example.com)\n"
        "2. Token Y - Untuk pengguna wallet → [Klik sini](https://example2.com)\n\n"
        "💡 *Fitur otomatis akan datang!*"
    )

def faucet(update: Update, context: CallbackContext):
    update.message.reply_text(
        "💧 Faucet Gratis:\n"
        "• https://faucet1.net\n"
        "• https://testnet-faucet.com\n\n"
        "Gunakan dengan bijak!"
    )

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Gunakan: /start, /airdrop, /faucet")

# Main
def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("airdrop", airdrop))
    dp.add_handler(CommandHandler("faucet", faucet))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
