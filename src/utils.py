from datetime import datetime

from dateutil.relativedelta import relativedelta


def get_dates():
    current_date = datetime.today()
    past_date = current_date - relativedelta(months=1)
    return current_date.date(), past_date.date()


def format_data(raw_data):
    data = {}
    for i in raw_data:
        date_string, time_string = i['@moment'].split(' ')
        data.setdefault(date_string, [{
            'time': '-',
            'value': '-'
        }]).append({'time': time_string, 'value': i['@value']})

        if len(data[date_string]) > 2:
            del data[date_string][0]

    return data