import asyncio

from config import CLIENT_ID, API_KEY
from packages.ozon import Ozon
from src.products import product_list, product_ids_list


async def main():
    ozon = Ozon(CLIENT_ID, API_KEY)

    await ozon.get_all_actions()
    await ozon.get_available_actions()
    await ozon.add_item_to_actions(product_list)
    await ozon.remove_item_from_actions(product_ids_list)


if __name__ == '__main__':
    asyncio.run(main())

# TODO: async
