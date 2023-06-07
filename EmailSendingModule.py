import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, COMMASPACE
import os
#pass = tlrqrwlogevtafip

#message body
def send_email(from_addr, to_addr, subject, files, body):
    # it creates a server
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    # this commands ensures a secure data transfer
    connection.ehlo()
    connection.starttls()
    # this command is used for login
    connection.login(user="mdrehan4650@gmail.com", password="tlrqrwlogevtafip")
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = COMMASPACE.join(to_addr)
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(body))
    if(files is not None):
        for file in files:
            with open(f"{file.name}", "rb") as f:
                part = MIMEApplication(f.read(),
                Name = f"{file.name}")
            part['Content-Disposition'] = f'attachment; filename="{file.name}"'
            msg.attach(part)

    connection.sendmail(from_addr, to_addr, msg.as_string())
    # it is used to close the connection
    connection.close()

    print("Done")


