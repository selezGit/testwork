import json
import logging
from typing import Optional

import requests
import xmltodict

from src.core import config


def get_data(urn: str) -> Optional[dict]:
    resp = requests.get(f'{config.BASE_URL}{urn}')

    if resp.status_code != 200:
        logging.error(f'error - {resp.text} status code - {resp.status_code}')
    else:
        response = xmltodict.parse(resp.content)
        try:
            return json.loads(json.dumps(response['rtsdata']['rates']['rate']))
        except TypeError:
            return None
