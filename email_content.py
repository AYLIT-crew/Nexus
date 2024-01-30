# Built-in modules
from dataclasses import dataclass

@dataclass
class EmailContent:
    sender: str
    recipients: list[str]
    body: str = ""
    subject: str = ""
