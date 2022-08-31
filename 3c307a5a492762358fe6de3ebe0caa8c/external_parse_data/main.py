from packages.database import Database
from packages.parser import Parser
from src.fill_db_data import names
from src.marketplaces_data import market_dict
from src.url_list import urls
from config import POSTGRES_NAME, POSTGRES_PASSWORD, TABLE_NAME


def main(url, db):
    parser = Parser(url, market_dict)
    parser._open_browser()
    html = parser._load_page(url)
    item_name, item_price = parser.get_elements(html)

    match_response = db.match_data(item_name)
    if len(match_response) == 0:
        db.insert_item(item_name, url, item_price)
    else:
        for row in match_response:
            if row[1] == item_name:
                db.update_item(row[0], url, item_price)

    # Captha on a new tab :(
    # updated_item_data = parser.find_on_market(item_name)
    # if len(updated_item_data) == 2:
    #     print(f'Find on markets ERROR:\n\t{updated_item_data[0]}')


if __name__ == '__main__':
    db = Database(POSTGRES_NAME, POSTGRES_PASSWORD, TABLE_NAME, names)
    db.prepare_db()

    for url in urls:
        main(url, db)

# TODO: docker-compose, connect postgres
