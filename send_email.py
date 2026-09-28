
import os
import smtplib
from email.mime.text import MIMEText


def send_email():
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    subject = "Learn.Inspire.Grow."

    message = """
Hello,

I hope you are doing well.

This email has been sent using a Python-based email
automation script.

This project demonstrates how Python can be used to:
- Connect to an SMTP server
- Authenticate securely using an application password
- Create an email message programmatically
- Send an automated email to a recipient

I am building practical skills in Python automation
as part of my Data Analytics learning journey.

Thank you.

Best regards,
Python Email Automation Project
"""

    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = sender_email
    email["To"] = recipient_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(
            sender_email,
            [recipient_email],
            email.as_string()
        )

    print("Email sent successfully!")


if __name__ == "__main__":
    send_email()

