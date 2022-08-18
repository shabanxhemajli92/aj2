import os
import time
import datetime
import smtplib
from email.mime.multipart import*
from email.mime.text      import*
from colorama import *
from art  import *
from email.message    import EmailMessage

# initialzing colorama
init()


#email function  
def gmail_send(subject, message, from_mail, to, password):
    global link
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    msg            = EmailMessage()
    message        = f'{message}'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = from_mail
    msg['To']      = to
    server.send_message(msg)

with open("copy.txt","w") as file:
    file.write("Your text here")
 