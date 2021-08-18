from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

from src.core import config


def save_to_excel(data, offset, exchange):
    try:
        wb = load_workbook(config.FILE_NAME)
    except FileNotFoundError:
        wb = Workbook()

    ws = wb.active

    if 'EUR' in exchange:
        currency = '#,#####0.0000€'
    else:
        currency = '#,#####0.0000$'

    ws.cell(
        column=offset + 1,
        row=1,
        value='Дата',
    ).style = config.HEADER_STYLE
    ws.cell(
        column=offset + 2,
        row=1,
        value='Курс',
    ).style = config.HEADER_STYLE

    ws.cell(
        column=offset + 3,
        row=1,
        value='Изменение',
    ).style = config.HEADER_STYLE

    for row, date in enumerate(data.keys()):
        exchange_rate = float(data[date][0]['value'])
        difference = exchange_rate - float(data[date][1]['value'])

        color = config.RED if difference <= 0 else config.GREEN

        cell_date = ws.cell(
            column=offset + 1, row=row + 2, value=date
        ).style = config.BASE_STYLE
        cell_date.number_format = currency

        cell_rate = ws.cell(
            column=offset + 2,
            row=row + 2,
            value=exchange_rate,
        ).style = config.BASE_STYLE
        cell_rate.number_format = currency

        cell_diff = ws.cell(column=offset + 3, row=row + 2, value=difference)
        cell_diff.number_format = currency
        cell_diff.border = config.THIN_BORDER
        cell_diff.fill = color

    wb.save(config.FILE_NAME)


def update_data():
    wb = load_workbook(config.FILE_NAME)
    ws = wb.active
    for index, row in enumerate(ws.iter_rows()):
        usd, eur = 0, 0
        for cell in row:
            if cell.column == 2:
                usd = cell.value
            elif cell.column == 5:
                eur = cell.value
        try:
            mid_market_rate = eur / usd
        except:
            mid_market_rate = ''

        res_col = ws.cell(
            column=7,
            row=index + 1,
            value=mid_market_rate,
        ).style = config.BASE_STYLE
        res_col.number_format = '#,#####0.00000'

    ws.cell(column=7, row=1, value='Средний курс').style = config.HEADER_STYLE

    # авто выравнивание
    for i in range(1, ws.max_column + 1):
        ws.column_dimensions[get_column_letter(i)].bestFit = True
        ws.column_dimensions[get_column_letter(i)].auto_size = True

    wb.save(config.FILE_NAME)

    return index + 1
