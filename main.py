import os

from src.core import config
from src.parser import get_data
from src.save_to_excel import save_to_excel, update_data
from src.send_message import send_message
from src.utils import format_data, get_dates

if __name__ == '__main__':
    if os.path.exists(config.FILE_NAME):
        os.remove(config.FILE_NAME)

    now, last_month = get_dates()
    for offset, exchange in enumerate(config.PARSE_LIST):
        URN = f'&currency={exchange}&moment_start={last_month}&moment_end={now}'
        raw_data = get_data(URN)
        save_to_excel(format_data(raw_data), offset*3, exchange)
    send_message(update_data())
