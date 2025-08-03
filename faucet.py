# faucet.py - Daftar faucet gratis
FAUCET_LIST = [
    {"name": "FreeBNB", "url": "https://freebnb.io", "interval": "1 jam"},
    {"name": "BscCoin", "url": "https://bsc.coinfaucet.io", "interval": "1 jam"},
    {"name": "Crypto Faucet", "url": "https://cryptofaucet.io", "interval": "6 jam"}
]

def get_faucet_list():
    """Kembalikan pesan faucet dalam format Markdown"""
    msg = "💧 **Faucet Aktif (Claim Manual)**\n\n"
    for f in FAUCET_LIST:
        msg += f"🔹 [{f['name']}]({f['url']})\n⏱️ Setiap {f['interval']}\n\n"
    msg += "💡 *Bot akan notif tiap jam. Kamu yang claim ya!*"
    return msg
