#!/usr/bin/env python3

import os
from email.message import EmailMessage
import ssl
import smtplib


email_sender ='globaltechcoporation@gmail.com'
email_password =os.environ.get("EMAIL_PASSWORD")
email_receiver ='hermannpougoue1@gmail.com'
subject = "Check out my new function"
body = """
    Create a forwarded port mapping which allows access to a specific port
  within the machine from a port on the host machine. In the example below,
  accessing "localhost:8080" will access port 80 on the guest machine.
  NOTE: This will enable public access to the opened port
  config.vm.network "forwarded_port", guest: 80, host: 8080
"""

email = EmailMessage()

email['From'] = email_sender
email['To']   = email_receiver
email['Subject'] =subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver,email.as_string())