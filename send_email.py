
import smtplib
from email.mime.text import MIMEText
sender='swethamadhaviyadagiri2001@gmail.com'
receivers=['yadagiriswetha9959@gmail.com']
port=1025
msg=MIMEText("this is test mail")
msg['Subject']='test mail'
msg['From']='swethamadhaviyadagiri2001@gmail.com'
msg['To']='yadagiriswetha9959@gmail.com'
with smtplib.SMTP('localhost',port)as server:
    server.ehlo()
    #server.login(sender,'1234567890')
    server.sendmail(sender,receivers,msg.as_string())
    print("Successfully sent mail")