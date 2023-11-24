import random

from .constants import STRING
from .models import URLMap
from .constants import AUTOGEN_SHORT_URL_LEN


def get_unique_short_id() -> str:
    while True:
        short_url: str = ''.join(random.choices(population=STRING, k=AUTOGEN_SHORT_URL_LEN))
        if not check_original(short_url):
            return short_url


def check_original(target: str):
    obj: URLMap = URLMap.query.filter_by(short=target).first()
    if obj:
        return obj.original
