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
               content: MIMEText) -> None:
    """
    Send an email using the provided SMTP_SSL session.
    """

    session.sendmail(sender, recipients, content.as_string())



# parse command-line arguments here

email_content = EmailContent()

# randomly choose an account
account = choice(ACCOUNTS)

# set up e-mail content
msg = MIMEText(email_content.body)
msg['Subject'] = email_content.subject
msg['From'] = email_content.sender
msg['To'] = ', '.email_content.recipients

# set up SMTP session
session = SMTP_SSL('smtp.gmail.com', SMTP_SSL_PORT)
session.login(account.address, account.password)
