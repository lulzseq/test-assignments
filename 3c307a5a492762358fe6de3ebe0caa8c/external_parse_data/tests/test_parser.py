import pytest
from ..packages.parser import *
from ..src.marketplaces_data import market_dict
from ..src.url_list import urls

parser = Parser(urls[0], market_dict)


class TestParser():

    def test_open_browser(self):
        result = parser.open_browser()
        assert isinstance(type(result), type(None))

    def test_load_page(self):
        result = parser.load_page(urls[0])
        assert isinstance(type(result), str)

    def test_get_elements(self):
        html = parser.load_page(urls[0])
        result = parser.get_elements(html)
        assert isinstance(type(result), tuple)
