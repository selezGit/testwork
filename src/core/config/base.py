import os

from openpyxl.styles import NamedStyle, PatternFill
from openpyxl.styles.borders import Border, Side
from openpyxl.styles.fonts import Font


BASE_URL = (
    'https://www.moex.com/export/derivatives/currency-rate.aspx?language=ru'
)
FILE_NAME = 'test.xlsx'
PARSE_LIST = ['USD/RUB', 'EUR/RUB']

# openpyxl styles
HEADER = PatternFill(
    start_color='4169E1',
    end_color='4169E1',
    fill_type='solid',
)

BASE = PatternFill(
    start_color='E0FFFF',
    end_color='E0FFFF',
    fill_type='solid',
)

RED = PatternFill(
    start_color='F08080',
    end_color='F08080',
    fill_type='solid',
)

GREEN = PatternFill(
    start_color='C2D69B',
    end_color='C2D69B',
    fill_type='solid',
)


THIN_BORDER = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin'),
)

HEADER_STYLE = NamedStyle(
    name='header', border=THIN_BORDER, fill=HEADER, font=Font(color='00FFFFFF')
)
BASE_STYLE = NamedStyle(name='base', border=THIN_BORDER, fill=BASE)
RED_STYLE = NamedStyle(name='red', border=THIN_BORDER, fill=RED)
GREEN_STYLE = NamedStyle(
    name='green',
    border=THIN_BORDER,
    fill=GREEN,
)


# email
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
