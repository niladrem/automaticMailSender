from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def sendMail(fromAddr, toAddr, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        server = smtplib.SMTP(config['SERVER']['HOST'], config['SERVER']['PORT'])
        server.ehlo()
        server.starttls()
        server.ehlo
        
        server.login(config['SERVER']['LOGIN'], config['SERVER']['PASSWORD'])
        text = msg.as_string()
        server.sendmail(fromAddr, toAddr, text)
        return True
    except Exception as e:
        print(str(e))
        return False



