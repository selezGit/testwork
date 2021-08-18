import os

from openpyxl.styles import PatternFill

BASE_URL = 'https://www.moex.com/export/derivatives/currency-rate.aspx?language=ru'
FILE_NAME = 'test.xlsx'
PARSE_LIST = ['USD/RUB', 'EUR/RUB']

# patterns

BASE = PatternFill(start_color='00FFCC99',
                   end_color='00FFCC99',
                   fill_type='solid',)

RED = PatternFill(start_color='00FF0000',
                  end_color='00FF0000',
                  fill_type='solid',)

GREEN = PatternFill(start_color='0000FF00',
                    end_color='0000FF00',
                    fill_type='solid',)

# email
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
