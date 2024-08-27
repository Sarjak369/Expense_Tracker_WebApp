
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage


path = '/Users/sarjak/Desktop/My_Projects/Projects_2024/expense_tracker/'
fileAttach = 'income.csv'

# Load the variables from the .env file
load_dotenv(
    r'/Users/sarjak/Desktop/My_Projects/Projects_2024/expense_tracker/.env')


# Retrieve email credentials from environment variables
FROM1 = os.environ['FROM1']
TO1 = os.environ['TO1']
# Make sure this matches the key in your .env file
password1 = os.environ['PASSWORD']

# Print values for debugging
# print(password1, TO1, FROM1)

###### EMAIL   ########

SUBJECT = 'Expense Tracker Data  ' + fileAttach + ' email sent Successfully!'
password = password1

email = EmailMessage()
email['Subject'] = SUBJECT
email['From'] = FROM1
email['To'] = TO1

with open(path + fileAttach, 'rb') as content_file:
    content = content_file.read()
    email.add_attachment(content, maintype='application',
                         subtype='pdf', filename=fileAttach)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(FROM1, password)
s.send_message(email)
s.quit()
print('Email sent for file with attachment: ' + fileAttach)
