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
#date time variable
now= datetime.datetime.today.strftime("%H:%M:%S %d-%m-%Y")

#email function  
# def gmail_send(subject, message, from_mail, to, password):
#     global link
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(from_mail, password)
#     msg            = EmailMessage()
#     message        = f'{message}'
#     msg.set_content(message)
#     msg['Subject'] = subject
#     msg['From']    = from_mailread()
#     msg['To']      = to
#     server.send_message(msg)

with open ("journal.txt","r") as f:
    file_contents=f.read()
print(file_contents)    
#Stores entries in a diary

print(Fore.LIGHTCYAN_EX+"")
tprint("Awesome Journal",font="random")
print("" + Style.RESET_ALL)


#display current journal
#art gui
new_entry= input("Enter diary entry here >>>")
if new_entry!="":
    with open("journal.txt","a") as file:
        file.write(now + "" + new_entry + "\n")
'''elif'''        
