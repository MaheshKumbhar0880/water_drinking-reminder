import configparser
import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Email configuration
email_sender = config['email']['EMAIL_USER']
email_password = config['email']['EMAIL_PASS']
email_receiver = config['email']['EMAIL_RECEIVER']
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Usually 587 for TLS or 465 for SSL


# Email content
subject = "Hourly Reminder of Yoga, water drinking!"
body = "Remember to drink water and do face yoga!"

def send_email():
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the job every hour
schedule.every().hour.do(send_email)

print("Reminder service started.")
while True:
    schedule.run_pending()
    time.sleep(1)
