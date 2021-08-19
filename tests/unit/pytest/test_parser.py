import pytest

from src.core import config
from src.parser import get_data


@pytest.mark.parametrize(
    'urn,expected', [('wrong_urn', None), (' ', None), (1, None)]
)
def test_get_data_fail(urn, expected):
    assert get_data(urn) == expected


def test_get_data_success():
    assert type(get_data(config.TEST_URN)) == list
