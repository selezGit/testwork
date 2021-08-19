
from src.core import config
from src.utils import format_data, get_morphy

import pytest


@pytest.mark.parametrize('colls_count,expected',
                         [(1, 'строка'),
                          (2, 'строки'),
                          (5, 'строк'),
                          (101, 'строка')])
def test_get_morphy(colls_count, expected):
    assert get_morphy(colls_count) == expected


@pytest.mark.parametrize('raw_data,expected',
                         [([], None),
                          ({}, None),
                          (1, None),
                          (config.TEST_RAW_DATA, config.TEST_CLEARED_DICT)])
def test_foramat_data(raw_data, expected):
    assert format_data(raw_data) == expected
