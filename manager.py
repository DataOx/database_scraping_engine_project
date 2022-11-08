import logging

from DAO_module.dao_postgres import DaoPostgres
from config import URL
from google_api_module.module_google_api import GoogleAPI
from parser_module.parser import Parser
from scraper_module.scraper import Scraper

parser = Parser()
scraper = Scraper(URL)
storage = DaoPostgres()
spreadsheet = GoogleAPI()


def application_launch():
    if storage.table_is_empty():
        data_list = parser.get_cleaned_data(scraper.all_data)
    else:
        data_list = parser.get_cleaned_data(scraper.current_data)

    storage.save_all(data_list)

    logging.info(f"received records from the site: {len(data_list)} (last two days)")

    for_google_sheet = storage.get_non_saved_data()

    spreadsheet.append_data(for_google_sheet)

    logging.info(f"added to spreadsheet successfully new records: {len(for_google_sheet)}")

    storage.update_all(for_google_sheet)


if __name__ == '__main__':
    application_launch()
