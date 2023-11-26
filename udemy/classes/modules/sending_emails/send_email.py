# Sending emails with python

# Imports
import os
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv

load_dotenv()

# Template path
EMAIL_TEMPLATE = pathlib.Path(__file__).parent / 'email_template.html'

# Sender data
sender_email = os.getenv('SENDER_EMAIL', '')
sender_password = os.getenv('SENDER_PASSWORD', '')

# Receiver data
RECEIVER = 'kaikeoliveira414@gmail.com'

# Server
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = sender_email
SMTP_PASSWORD = sender_password

# Message

print(f'E-mail: {sender_email}')
print(f'Password: {sender_password}')
print(f'Template: {EMAIL_TEMPLATE}')

with open(EMAIL_TEMPLATE, 'r', encoding='utf-8') as template:
    template_text = template.read()
    email_template = Template(template_text)
    email_text = email_template.substitute(name='Kaike')

# Transform email message to MIMEMultipart
mime_multpart = MIMEMultipart()
mime_multpart['from'] = sender_email
mime_multpart['to'] = RECEIVER
mime_multpart['subject'] = 'E-mail subject'

email_body = MIMEText(email_text, 'html', 'utf-8')
mime_multpart.attach(email_body)

# Send email
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.send_message(mime_multpart)
    print('Email sent successfully')
