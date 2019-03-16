import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.utils.html import strip_tags


def create_message(subject, sender, to):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    return msg


def create_body_attach(html_msg, create_msg):
    html_text = html_msg
    plain_text = strip_tags(html_text)

    part1 = MIMEText(plain_text, 'plain')
    part2 = MIMEText(html_text, 'html')

    create_msg.attach(part1)
    create_msg.attach(part2)

    return create_msg


def send_message(username, password, create_msg_body):
    host = "smtp.gmail.com"
    port = 587
    mail = smtplib.SMTP(host, port, timeout=60)
    mail.ehlo()
    mail.starttls()

    recepient = [create_msg_body["To"]]

    mail.login(username, password)
    mail.sendmail(create_msg_body["From"], recepient, create_msg_body.as_string())
    mail.quit()
