import smtplib
from email.message import EmailMessage

import pymorphy2

from src.core import config

login = config.EMAIL_LOGIN
password = config.EMAIL_PASSWORD
server = smtplib.SMTP_SSL(config.SMTP_SERVER,
                          config.SMTP_PORT)

server.login(config.EMAIL_LOGIN,
             config.EMAIL_PASSWORD)


def send_message(colls_count):
    morph = pymorphy2.MorphAnalyzer()

    message = EmailMessage()
    message["From"] = login
    message["To"] = ",".join([login])
    message["Subject"] = f'Отчёт'

    string = morph.parse('строка')[0]
    normal_word = string.make_agree_with_number(colls_count).word

    message.set_content(f'''
        Работа скрипта завершена, результат: {colls_count} {normal_word}
    ''')

    with open(config.FILE_NAME, 'rb') as f:
        file_data = f.read()
        message.add_attachment(file_data, maintype="application",
                               subtype="xlsx", filename=config.FILE_NAME)

    server.send_message(message)
