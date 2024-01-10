import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(line, html_content):
    # Email sending code here
    my_email = 'radeel.service@gmail.com'
    my_email_password = 'radeelservice1234'
    client_email =  line[8]

    message = MIMEMultipart()
    message['From'] = my_email
    message['To'] = client_email
    message['Subject'] = "Facture d'Eau et d'Életricité"

    # Attach HTML content
    message.attach(MIMEText(html_content, 'html'))

    # Rest of email sending code here
    # ...
