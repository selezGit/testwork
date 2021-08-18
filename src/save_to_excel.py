from openpyxl import Workbook, load_workbook
from openpyxl.styles.numbers import (FORMAT_CURRENCY_EUR_SIMPLE,
                                     FORMAT_CURRENCY_USD_SIMPLE,
                                     FORMAT_NUMBER_00)
from openpyxl.utils import get_column_letter

from src.core import config


def save_to_excel(data, offset, exchange):
    try:
        wb = load_workbook(config.FILE_NAME)
    except FileNotFoundError:
        wb = Workbook()
    ws = wb.active

    if 'EUR' in exchange:
        currency = FORMAT_CURRENCY_EUR_SIMPLE
    else:
        currency = FORMAT_CURRENCY_USD_SIMPLE

    ws.cell(column=offset+1, row=1, value='Дата').fill = config.BASE
    ws.cell(column=offset+2, row=1, value='Курс').fill = config.BASE
    ws.cell(column=offset+3, row=1, value='Изменение').fill = config.BASE

    for row, date in enumerate(data.keys()):
        exchange_rate = float(data[date][0]['value'])
        difference = exchange_rate - float(data[date][1]['value'])
        color = config.RED if difference <= 0 else config.GREEN

        ws.cell(column=offset+1, row=row+2, value=date).fill = config.BASE
        cell_rate = ws.cell(column=offset+2, row=row+2, value=exchange_rate)
        cell_rate.fill = config.BASE
        cell_rate.number_format = currency

        cell_diff = ws.cell(column=offset+3, row=row+2, value=difference)
        cell_diff.fill = color
        cell_diff.number_format = currency

    # авто выравнивание
    for i in range(1, ws.max_column+1):
        ws.column_dimensions[get_column_letter(i)].bestFit = True
        ws.column_dimensions[get_column_letter(i)].auto_size = True

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
            result = eur/usd
        except:
            result = ''

        res_col = ws.cell(column=7, row=index+1, value=result)
        res_col.fill = config.BASE
        res_col.number_format = FORMAT_NUMBER_00

    wb.save(config.FILE_NAME)

    return index+1



