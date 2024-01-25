import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirmation_email(recipient_email, username):
    sender_email = "agritechserviceorg@gmail.com"
    password = "yvoq mzmv qmjr ahoi"
    subject = "Account Confirmation"
    body = f"Hello {username},\n\nThank you for creating an account!\n\nBest regards,\nAgriTech Team"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())

