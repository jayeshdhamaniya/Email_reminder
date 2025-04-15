import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
        server.quit()
        print("✅ Reminder email sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)

def schedule_reminder(subject, body, time_str):
    schedule.every().day.at(time_str).do(send_email, subject, body)
    print(f"📅 Reminder set for {time_str}: {subject}")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Example Usage
if __name__ == "__main__":
    schedule_reminder("Drink Water", "Time to hydrate! 💧", "12:00")
    schedule_reminder("Stretch!", "Take 2 minutes to stretch and relax. 🧘", "15:00")
    run_scheduler()
