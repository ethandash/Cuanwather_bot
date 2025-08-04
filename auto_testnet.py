# auto_testnet.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

WALLET = os.getenv("WALLET_ADDRESS")  # Simpan di GitHub Secrets

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)

def claim_bnb():
    driver = get_driver()
    try:
        driver.get("https://faucet.bnbchain.org")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(WALLET)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
        time.sleep(5)
        print("✅ BNB Testnet: Claim submitted")
        return "BNB: ✅"
    except Exception as e:
        print(f"❌ BNB: Gagal - {e}")
        return "BNB: ❌"
    finally:
        driver.quit()

def claim_polygon():
    driver = get_driver()
    try:
        driver.get("https://faucet.polygon.technology")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your address']").send_keys(WALLET)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
        time.sleep(5)
        print("✅ Polygon Testnet: Claim submitted")
        return "Polygon: ✅"
    except Exception as e:
        print(f"❌ Polygon: Gagal - {e}")
        return "Polygon: ❌"
    finally:
        driver.quit()

def claim_zksync():
    driver = get_driver()
    try:
        driver.get("https://faucet.zksync.io")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input").send_keys(WALLET)
        time.sleep(1)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "claim" in btn.text.lower():
                btn.click()
                break
        time.sleep(5)
        print("✅ zkSync Testnet: Claim submitted")
        return "zkSync: ✅"
    except Exception as e:
        print(f"❌ zkSync: Gagal - {e}")
        return "zkSync: ❌"
    finally:
        driver.quit()

def main():
    if not WALLET:
        print("❌ WALLET_ADDRESS tidak diatur!")
        return

    print(f"🚀 Mulai auto-claim testnet untuk: {WALLET[:10]}...")
    results = []

    results.append(claim_bnb())
    results.append(claim_polygon())
    results.append(claim_zksync())

    # Kirim hasil ke Telegram
    send_telegram("🧪 **Auto-Claim Testnet**\n" + "\n".join(results))

def send_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    if not token or not chat_id:
        print("❌ Telegram tidak dikonfigurasi")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        import requests
        requests.post(url, data=data)
    except:
        pass

# auto_testnet.py (v2.0)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

WALLET = os.getenv("WALLET_ADDRESS")

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)

# 🔹 BNB Chain
def claim_bnb():
    driver = get_driver()
    try:
        driver.get("https://faucet.bnbchain.org")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(WALLET)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
        time.sleep(5)
        return "BNB: ✅"
    except Exception as e:
        print(f"❌ BNB: {e}")
        return "BNB: ❌"
    finally:
        driver.quit()

# 🔹 Polygon
def claim_polygon():
    driver = get_driver()
    try:
        driver.get("https://faucet.polygon.technology")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your address']").send_keys(WALLET)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()
        time.sleep(5)
        return "Polygon: ✅"
    except Exception as e:
        print(f"❌ Polygon: {e}")
        return "Polygon: ❌"
    finally:
        driver.quit()

# 🔹 zkSync
def claim_zksync():
    driver = get_driver()
    try:
        driver.get("https://faucet.zksync.io")
        time.sleep(5)
        driver.find_element(By.XPATH, "//input").send_keys(WALLET)
        time.sleep(1)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "claim" in btn.text.lower():
                btn.click()
                break
        time.sleep(5)
        return "zkSync: ✅"
    except Exception as e:
        print(f"❌ zkSync: {e}")
        return "zkSync: ❌"
    finally:
        driver.quit()

# 🔹 SCROLL (Sepolia)
def claim_scroll():
    driver = get_driver()
    try:
        driver.get("https://sepolia.scroll.io")
        time.sleep(5)
        # Cari input wallet
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for inp in inputs:
            if "address" in inp.get_attribute("placeholder").lower():
                inp.send_keys(WALLET)
                break
        time.sleep(1)
        # Cari tombol claim
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            if "get eth" in btn.text.lower() or "claim" in btn.text.lower():
                btn.click()
                break
        time.sleep(5)
        return "Scroll: ✅"
    except Exception as e:
        print(f"❌ Scroll: {e}")
        return "Scroll: ❌"
    finally:
        driver.quit()

# 🔹 ARBITRUM (Goerli)
def claim_arbitrum():
    driver = get_driver()
    try:
        driver.get("https://faucet.quicknode.com/arbitrum/goerli")
        time.sleep(5)
        driver.find_element(By.ID, "wallet").send_keys(WALLET)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        return "Arbitrum: ✅"
    except Exception as e:
        print(f"❌ Arbitrum: {e}")
        return "Arbitrum: ❌"
    finally:
        driver.quit()

# 🔹 FUNGSI UTAMA
def main():
    if not WALLET:
        print("❌ WALLET_ADDRESS tidak diatur!")
        return

    print(f"🚀 Auto-Claim Testnet dimulai untuk: {WALLET[:10]}...")
    results = []

    results.append(claim_bnb())
    results.append(claim_polygon())
    results.append(claim_zksync())
    results.append(claim_scroll())
    results.append(claim_arbitrum())

    # Kirim hasil
    send_telegram("🧪 **Auto-Claim Testnet**\n" + "\n".join(results))

def send_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    if not token or not chat_id:
        print("❌ Telegram tidak dikonfigurasi")
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        import requests
        requests.post(url, data=data)
    except:
        pass

if __name__ == "__main__":
    main()
