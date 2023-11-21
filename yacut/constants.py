import re
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Pattern

STRING: str = "".join((ascii_uppercase, ascii_lowercase, digits))

PATTERN: str = r"^[A-Za-z0-9]{1,16}$"
MATCH: Pattern[str] = re.compile(PATTERN)
