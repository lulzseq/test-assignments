import inspect
from datetime import datetime

from api import ApiBasic
from database import Database
from ..config import DB_USERNAME, DB_PASSWORD, DB_NAME, TABLE_NAME

db = Database(DB_USERNAME, DB_PASSWORD, DB_NAME, TABLE_NAME)


class Ozon(ApiBasic):

    def __init__(self, client_id: str, api_key: str):
        self.host = 'https://api-seller.ozon.ru'
        self.api_key = api_key
        self.client_id = client_id
        self.headers = {
            'Client-Id': self.client_id,
            'Api-Key': self.api_key,
            'Content-Type': 'application/json'
        }

    def get_all_actions(self):
        method = 'v1/actions'
        response = ApiBasic._send_request('GET', self.host, method, headers=self.headers)
        db.write_log(datetime.now(), inspect.stack()[0][3], method, response)
        return response

    def get_available_actions(self):
        method = 'v1/actions/candidates'
        response = ApiBasic._send_request('POST', self.host, method, headers=self.headers)
        db.write_log(datetime.now(), inspect.stack()[0][3], method, response)
        return response

    def add_item_to_actions(self, product_list: list):
        method = '/v1/actions/products/activate'
        params = {
            'action_id': 60564,
            'products': product_list
        }
        response = ApiBasic._send_request('POST', self.host, method, headers=self.headers, params=params)
        db.write_log(datetime.now(), inspect.stack()[0][3], method, response)
        return response

    def remove_item_from_actions(self, product_ids_list: list) -> object:
        method = '/v1/actions/products/deactivate'
        params = {
            'action_id': 66011,
            'product_ids': product_ids_list
        }
        response = ApiBasic._send_request('POST', self.host, method, headers=self.headers, params=params)
        db.write_log(datetime.now(), inspect.stack()[0][3], method, response)
        return response
