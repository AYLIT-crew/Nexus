# Local modules
from sys import exit

def fatal_error(message: str) -> None:
    """
    Prints the error message to the user and exits the program.
    """

    print(f"Error: {message}")
    exit(1)