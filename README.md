# Python Email Automation

A Python-based project that automates email sending using Gmail's SMTP server.

## Objective

To automate email communication using Python while keeping authentication credentials secure.

## What I Built

* Connected Python to Gmail SMTP server
* Established a secure TLS connection
* Authenticated using a Gmail App Password
* Created and sent an email programmatically
* Used environment variables to keep credentials outside the source code

## Tech Stack

* Python
* `smtplib`
* `email.mime`
* Gmail SMTP
* Environment Variables

## How It Works

```text
Python Script
     ↓
SMTP Connection
     ↓
TLS Authentication
     ↓
Create Email
     ↓
Send Email
```

## How to Run

Set these environment variables:

```text
SENDER_EMAIL=your_email@gmail.com
EMAIL_APP_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient_email@gmail.com
```

Then run:

```bash
python send_email.py
```

Expected output:

```text
Email sent successfully!
```

## Output

### Successful Execution

[View email_sent.png](email_sent.png)

### Received Email

[View email_received.png](email_received.png)

## Security

Credentials are not stored directly in the source code. Environment variables and a Gmail App Password are used for authentication.
