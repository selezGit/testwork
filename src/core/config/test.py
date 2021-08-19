from .base import *  # noqa

EXCHANGE = 'USD/RUB'
MOMENТ_START = '2021-07-19'
MOMENT_END = '2021-08-19'

TEST_URN = (
    f'&currency={EXCHANGE}&moment_start={MOMENТ_START}&moment_end={MOMENT_END}'
)


TEST_RAW_DATA = [
    {'@moment': f'{MOMENТ_START} 18:44:00', '@value': 'one value'},
    {'@moment': f'{MOMENТ_START} 13:45:00', '@value': 'second value'},
    {'@moment': f'{MOMENT_END} 13:45:00', '@value': 'third value'},
]

TEST_CLEARED_DICT = {
    '2021-07-19': [
        {'time': '18:44:00', 'value': 'one value'},
        {'time': '13:45:00', 'value': 'second value'},
    ],
    '2021-08-19': [{'time': '13:45:00', 'value': 'third value'}],
}
