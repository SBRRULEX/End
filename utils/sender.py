# utils/sender.py

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from utils.logger import log_message
from utils.stop_flag import get_stop_flag

def start_bot(uids, msg_path, delay, login_method, credentials):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    print("🚀 SBR BOT STARTED")

    driver = webdriver.Chrome(options=options)

    try:
        if login_method == "token":
            login_with_token(driver, credentials['token'])
        else:
            login_with_email(driver, credentials['email'], credentials['password'])

        # Read messages
        with open(msg_path, 'r', encoding='utf-8') as f:
            messages = [line.strip() for line in f if line.strip()]

        for uid in uids:
            for message in messages:
                if get_stop_flag():
                    print("🛑 SBR BOT STOPPED")
                    return

                print(f"Sending to {uid} → {message}")
                send_message(driver, uid, message)
                log_message(uid, message)
                time.sleep(delay + random.randint(1, 3))  # Slight random delay

        print("✅ SBR BOT COMPLETED")

    except Exception as e:
        print(f"❌ ERROR: {e}")
    finally:
        driver.quit()

# ---------------------------

def login_with_email(driver, email, password):
    driver.get("https://mbasic.facebook.com/login")
    time.sleep(2)

    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    # 2FA check
    if "checkpoint" in driver.current_url:
        print("🔐 2FA checkpoint detected. Please resolve manually.")
        raise Exception("2FA needed.")

    print("✅ Logged in with email/password")

def login_with_token(driver, token):
    driver.get("https://mbasic.facebook.com")
    script = f"""
    document.cookie = "c_user=; path=/; domain=.facebook.com";
    document.cookie = "xs=; path=/; domain=.facebook.com";
    localStorage.setItem('token', '{token}');
    """
    driver.execute_script(script)
    driver.refresh()
    time.sleep(2)
    print("✅ Logged in using token")

# ---------------------------

def send_message(driver, uid, message):
    try:
        url = f"https://mbasic.facebook.com/messages/thread/{uid}"
        driver.get(url)
        time.sleep(2)

        textarea = driver.find_element(By.NAME, "body")
        textarea.send_keys(message)

        textarea.send_keys(Keys.TAB)
        textarea.send_keys(Keys.ENTER)

        print(f"✅ Message sent to {uid}")
    except Exception as e:
        print(f"❌ Error sending message to {uid}: {e}")
