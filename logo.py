from termcolor import colored as cl
from pyfiglet import figlet_format as ff

def print_logo() -> None:
    """
    Print the program's logo to the screen.
    """

    print(cl('-'*30, 'red'))
    print(cl(ff('Nexus')+'\n\t-A mail bomber program.\n\t-An AYLIT Production.\n\t-v1.0', 'red'))
    print(cl('-'*30, 'red'))
    print('\n')

    

