# Built-in modules
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from sys import exit
from random import choice

# Third-party modules
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

# Local modules
from email_content import EmailContent
from email_accounts import ACCOUNTS


def send_email(session: SMTP_SSL, sender: str, recipients: list[str],
               mime_content: MIMEText) -> None:
    """
    Send an email using the provided SMTP_SSL session.
    """

    session.sendmail(sender, recipients, mime_content.as_string())



# parse command-line arguments here

email_content = EmailContent()

# randomly choose an account
account = choice(ACCOUNTS)

# set up e-mail content
mime_content = MIMEText(email_content.body)
mime_content['Subject'] = email_content.subject
mime_content['From'] = email_content.sender
mime_content['To'] = ', '.email_content.recipients

# set up SMTP session
session = SMTP_SSL('smtp.gmail.com', SMTP_SSL_PORT)
session.login(account.address, account.password)

for _ in range(no_of_emails):
    send_email(session, account.address, email_content.recipients,
               mime_content)
    print("E-mail sent succesfully.")
