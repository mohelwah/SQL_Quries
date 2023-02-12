# Simple Mail Transfer Protocol (SMTP)
import smtplib

# import os.path
from os.path import basename

# import MIME (Multipurpose Internet Mail Extensions) Multipart email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import message

# set server parmeters
severUserName = "smtp-relay.sendinblue.com"
port = 587
userName = "moh.elwah@gmail.com"
password = "dOw0b3tEzNDncPgT"

# set Sender information
from_addr = 'moh.elwah@gmail.com' # put your emil here
to_addr = 'moh.elwah@gmail.com'   # change to abc.xyz@gmail.com
subject = "Results for sql Query"
content = "please see the attchments"

# login to smtplib server
server = smtplib.SMTP(severUserName, 587)
server.login(userName, password)

# constrac the message 
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

# set the query file names
filename = ['query1.csv','query2.csv','query3.csv','query4.csv']

# loop for sending queries files
for i in range(len(filename)):
    with open(str(filename[i]), 'r') as f:
        attachment = MIMEApplication(f.read(), Name=basename(str(filename[i])))
        attachment['Content-Disposition'] = 'attachment; filname="{}"'.format(basename(str(filename[i])))
        msg.attach(attachment)

# send the message
server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])

