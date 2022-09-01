import asyncio

from config import CLIENT_ID, API_KEY
from packages.ozon import Ozon
from src.products import product_list, product_ids_list


async def main():
    ozon = Ozon(CLIENT_ID, API_KEY)

    print(f'get_all_actions: {ozon.get_all_actions()}')
    print(f'get_available_actions: {ozon.get_available_actions()}')
    print(f'add_item_to_actions: {ozon.add_item_to_actions(product_list)}')
    print(f'remove_item_from_actions: {ozon.remove_item_from_actions(product_ids_list)}')


if __name__ == '__main__':
    main()

# TODO: async
