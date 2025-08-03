# wallet.py - Baca saldo & transaksi dari BSC
import os
import requests

# Ambil dari environment (aman)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")
BSCSCAN_API = "https://api.bscscan.com/api"
BSCSCAN_KEY = os.getenv("BSCSCAN_KEY")

def get_balance_bsc():
    """Cek saldo BNB"""
    if not WALLET_ADDRESS or not BSCSCAN_KEY:
        return "❌ Wallet/Key belum diatur!"
    
    url = f"{BSCSCAN_API}?module=account&action=balance&address={WALLET_ADDRESS}&tag=latest&apikey={BSCSCAN_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == '1':
            bnb = int(data['result']) / 10**18
            return f"{bnb:.5f} BNB"
        else:
            return "Gagal"
    except:
        return "Offline"

def get_transactions_bsc():
    """Ambil 3 transaksi terakhir"""
    if not WALLET_ADDRESS or not BSCSCAN_KEY:
        return ["❌ Setup dulu di secrets"]
    
    url = f"{BSCSCAN_API}?module=account&action=txlist&address={WALLET_ADDRESS}&startblock=0&endblock=99999999&sort=desc&apikey={BSCSCAN_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        txs = data['result'][:3]
        result = []
        for tx in txs:
            value = int(tx['value']) / 10**18
            direction = "📤" if tx['from'].lower() == WALLET_ADDRESS.lower() else "📥"
            result.append(f"{direction} {value:.5f} BNB")
        return result
    except:
        return ["Gagal ambil data"]
