import requests


class ApiBasic:

    def _send_request(self, http_method, host, method, headers=None, params=None, json=None, response_type=None):
        response = requests.request(http_method, f'{host}/{method}', params=params, headers=headers, json=json)

        if response.status_code != 200:
            raise HttpException(response.status_code, response.text)

        if response_type == 'json':
            response = response.json()

        return response


class HttpException(Exception):
    def __init__(self, status: int, message: str = '') -> None:
        self.status = status
        self.message = message

    def __str__(self) -> str:
        return f'ERROR: {self.status}\n{self.message}'
