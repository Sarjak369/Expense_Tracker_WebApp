# AppEmail_old.py
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

ENV_FILE_PATH = ".env"
if os.path.exists(ENV_FILE_PATH):
    load_dotenv(ENV_FILE_PATH)
else:
    print(f"Warning: .env file not found at {ENV_FILE_PATH}")

EMAIL_FROM = os.getenv("FROM")
EMAIL_PASSWORD = os.getenv("PASSWORD")


def send_email_with_csv(file_path: str, file_name: str, recipient_email: str):
    try:
        if not EMAIL_FROM or not EMAIL_PASSWORD:
            raise ValueError("Email credentials (FROM, PASSWORD) are missing.")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        email = EmailMessage()
        email['Subject'] = f"Exported File: {file_name}"
        email['From'] = EMAIL_FROM
        email['To'] = recipient_email
        email.set_content("Please find the attached CSV file.")

        with open(file_path, 'rb') as f:
            email.add_attachment(
                f.read(),
                maintype='text',
                subtype='csv',
                filename=file_name
            )

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_FROM, EMAIL_PASSWORD)
            smtp.send_message(email)

        print(f"Email sent successfully to {recipient_email}.")

    except Exception as e:
        print(f"Failed to send email: {e}")
