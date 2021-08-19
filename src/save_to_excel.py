from openpyxl import worksheet
from openpyxl.utils import get_column_letter

from src.core import config
from src.utils import connect_to_wb


@connect_to_wb
def save_to_excel(
    ws: worksheet,
    cleared_dict: dict,
    offset: int,
    exchange: str,
) -> None:
    ws.cell(
        column=offset + 1,
        row=1,
        value='Дата',
    ).style = config.HEADER_STYLE
    ws.cell(
        column=offset + 2,
        row=1,
        value=f'Курс {exchange}',
    ).style = config.HEADER_STYLE

    ws.cell(
        column=offset + 3,
        row=1,
        value='Изменение',
    ).style = config.HEADER_STYLE

    for row, date in enumerate(cleared_dict.keys()):
        try:
            exchange_rate = float(cleared_dict[date][0]['value'])
            difference = exchange_rate - float(cleared_dict[date][1]['value'])
            color = config.RED_FILL if difference <= 0 else config.GREEN_FILL
        except ValueError:
            exchange_rate = float(cleared_dict[date][1]['value'])
            difference = 0
            color = config.BASE_FILL
        except IndexError:
            exchange_rate = float(cleared_dict[date][0]['value'])
            difference = 0
            color = config.BASE_FILL

        ws.cell(
            column=offset + 1,
            row=row + 2,
            value=date,
        ).style = config.BASE_STYLE

        cell_rate = ws.cell(
            column=offset + 2,
            row=row + 2,
            value=exchange_rate,
        )
        cell_rate.style = config.BASE_STYLE
        cell_rate.number_format = f'₽{config.NUMBER_FORMAT}'

        cell_diff = ws.cell(
            column=offset + 3,
            row=row + 2,
            value=difference,
        )
        cell_diff.number_format = f'₽{config.NUMBER_FORMAT}'
        cell_diff.border = config.THIN_BORDER
        cell_diff.fill = color


@connect_to_wb
def update_data(ws: worksheet) -> int:
    for index, row in enumerate(ws.iter_rows()):
        if index == 0:
            continue
        usd, eur = 0, 0
        for cell in row:
            if cell.column == 2:
                usd = cell.value
            elif cell.column == 5:
                eur = cell.value
        try:
            mid_market_rate = eur / usd
        except ZeroDivisionError:
            mid_market_rate = 0

        res_col = ws.cell(
            column=7,
            row=index + 1,
            value=mid_market_rate,
        )
        res_col.number_format = config.NUMBER_FORMAT
        res_col.style = config.BASE_STYLE

    ws.cell(column=7, row=1, value='Средний курс').style = config.HEADER_STYLE

    for column_cells in ws.columns:
        length = max(len(str(cell.value) or '') for cell in column_cells)
        ws.column_dimensions[
            get_column_letter(column_cells[0].column)
        ].width = (length * config.RIGHT_INDENT)

    return index + 1
