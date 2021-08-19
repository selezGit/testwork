import smtplib
from email.message import EmailMessage

from src.core import config
from src.utils import get_morphy


login = config.EMAIL_LOGIN
password = config.EMAIL_PASSWORD
server = smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT)
server.login(config.EMAIL_LOGIN, config.EMAIL_PASSWORD)


def send_message(colls_count: int) -> None:
    message = EmailMessage()
    message['From'] = login
    message['To'] = ','.join([login])
    message['Subject'] = 'Report'

    message.set_content(
        f'''
        Работа скрипта завершена,
        результат: {colls_count} {get_morphy(colls_count)}
    '''
    )

    with open(config.FILE_NAME, 'rb') as f:
        file_data = f.read()
        message.add_attachment(
            file_data,
            maintype='application',
            subtype='xlsx',
            filename=config.FILE_NAME,
        )

    server.send_message(message)
