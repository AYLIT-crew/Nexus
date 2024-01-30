# Built-in modules
from dataclasses import dataclass

@dataclass
class EmailContent:
    body: str
    subject: str
    sender: str
    recipients: list[str]
