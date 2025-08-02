# .github/workflows/airdrop-bot.yml
name: 🚀 CuanWatcher Bot

on:
  workflow_dispatch:  # Bisa dijalankan manual
  schedule:
    - cron: '0 * * * *'  # Jalankan tiap jam (pada menit ke-0)

jobs:
  send-airdrop:
    name: 📬 Kirim Airdrop Update
    runs-on: ubuntu-latest

    steps:
      - name: 🔁 Checkout kode
        uses: actions/checkout@v4

      - name: 🐍 Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: 📦 Install dependensi
        run: |
          pip install --upgrade pip
          pip install python-telegram-bot

      - name: 🤖 Jalankan bot
        run: python app.py
        env:
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
