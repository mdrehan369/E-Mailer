# import smtplib
# #pass = tlrqrwlogevtafip
# # it creates a server
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# # this commands ensures a secure data transfer
# connection.ehlo()
# connection.starttls()
# # this command is used for login
# connection.login(user="mdrehan4650@gmail.com", password="tlrqrwlogevtafip")
# # this command is used to send mail
# connection.sendmail("mdrehan4650@gmail.com", "mdrehan9007@gmail.com", "Test Mail")
# # it is used to close the connection
# connection.close()

import smtplib
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
#pass = tlrqrwlogevtafip
# it creates a server
connection = smtplib.SMTP("smtp.gmail.com", 587)
# this commands ensures a secure data transfer
connection.ehlo()
connection.starttls()
# this command is used for login
connection.login(user="mdrehan4650@gmail.com", password="tlrqrwlogevtafip")
#message body

msg = MIMEMultipart()
msg["From"] = "mdrehan4650@gmail.com"
msg["To"] = "mdrehan9007@gmail.com"
msg["Subject"] = "subject by test email"
msg["Date"] = formatdate(localtime=True)
msg.attach(MIMEText("Text message by test email"))
with open("basic design.png", "rb") as f:
    part = MIMEApplication(f.read(),
    Name = "basic design.png")
part['Content-Disposition'] = 'attachment; filename="basic design.png"'
msg.attach(part)

with open("text.txt", "rb") as f:
    part = MIMEApplication(f.read(),
    Name = "text.txt")
part['Content-Disposition'] = 'attachment; filename="text.txt"'
msg.attach(part)

connection.sendmail("mdrehan4650@gmail.com", "mdrehan9007@gmail.com", msg.as_string())
# it is used to close the connection
connection.close()

print("Done")


