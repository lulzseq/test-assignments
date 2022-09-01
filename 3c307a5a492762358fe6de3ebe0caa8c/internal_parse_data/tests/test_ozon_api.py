from ..config import CLIENT_ID, API_KEY
from ..packages.ozon import *
from ..src.products import product_list, product_ids_list

ozon = Ozon(CLIENT_ID, API_KEY)


class TestOzonApi:

    def test_get_all_actions(self):
        result = ozon.get_all_actions()
        assert 'result' in result

    def test_get_available_actions(self):
        result = ozon.get_available_actions()
        assert 'result' in result

    def test_add_item_to_actions(self):
        result = ozon.add_item_to_actions(product_list)
        assert 'result' in result

    def test_remove_item_from_actions(self):
        result = ozon.remove_item_from_actions(product_ids_list)
        assert 'result' in result
