import json
import logging

import requests
import xmltodict

from src.core import config


def get_data(URN):

    resp = requests.get(f'{config.BASE_URL}{URN}')

    if resp.status_code != 200:
        logging.error(
            f'error - {resp.text} status code - {resp.status_code}'
        )
    else:
        response = xmltodict.parse(resp.content)
        return json.loads(json.dumps(response['rtsdata']['rates']['rate']))
