name: 🧪 Auto-Claim Testnet
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:

jobs:
  claim:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install Dependencies
        run: |
          pip install --upgrade pip
          pip install selenium requests
      - name: Jalankan Bot
        run: python auto_testnet.py
        env:
          WALLET_ADDRESS: ${{ secrets.WALLET_ADDRESS }}
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
