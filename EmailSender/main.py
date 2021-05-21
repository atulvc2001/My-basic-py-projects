import smtplib
from email.message import EmailMessage

email = EmailMessage() ##creating object for EmailMessage
email['from'] = 'atulvc2001@gmail.com'
email['to'] = 'atvc19ec@cmrit.ac.in'
email['subject'] = 'Email sent using python'
email.set_content("Hey it works!")
password = input(str("Please enter your password: "))
with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo() ## server object
    smtp.starttls ## used to send data between server and client
    smtp.login("atulvc2001@gmail.com",password) ## login id and password of gmail
    smtp.send_message(email) ## Sending Email
    print("email sent")

